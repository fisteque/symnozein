#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml


DEFAULT_PROJECT_ROOT = Path("/home/fiste/Noema")
PROJECT_ROOT = Path(os.environ.get("NOEMA_PROJECT_ROOT", DEFAULT_PROJECT_ROOT)).resolve()
DEFAULT_RUNTIME_ROOT = PROJECT_ROOT / "bridge"
DEFAULT_CODEX_INBOX_ROOT = PROJECT_ROOT / "codex" / "inbox"
DEFAULT_CODEX_PROCESSED_ROOT = PROJECT_ROOT / "codex" / "processed"
STATE_RELATIVE_PATH = Path("state/codex_autoreply_state.json")
OUTBOX_RELATIVE_DIR = Path("outbox/messages")
MAX_BYTES = 64 * 1024
REQUIRED_FIELDS = {"id", "type", "created_at", "sender", "target"}
VALID_TARGETS = {"codex"}
RISKY_TERMS = (
    "systemd",
    "allowlist",
    "bridge_cycle.py",
    "git push",
    "force push",
    "delete",
    "rm ",
    "rm -",
    "webhook",
    "network",
    "install",
    "commit",
    "runtime logic",
)


class WorkerError(RuntimeError):
    pass


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_iso(dt: datetime | None = None) -> str:
    return (dt or utc_now()).isoformat().replace("+00:00", "Z")


def utc_month(dt: datetime | None = None) -> str:
    return (dt or utc_now()).strftime("%Y-%m")


def ensure_inside(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise WorkerError(f"Path outside allowed root: {path}")
    return resolved_path


def atomic_write_text(path: Path, text: str, allowed_root: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_path = ensure_inside(path, allowed_root)
    tmp_path = ensure_inside(safe_path.with_name(f".{safe_path.name}.tmp-{os.getpid()}"), allowed_root)
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(safe_path)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slug(value: str, limit: int = 80) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip(".-")
    return (safe or "no-id")[:limit]


def project_relative(path: Path) -> str:
    resolved = path.resolve()
    if resolved == PROJECT_ROOT or PROJECT_ROOT in resolved.parents:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    return str(resolved)


def load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise WorkerError(f"JSON state is not an object: {path}")
    return data


def save_json(path: Path, data: dict[str, Any], allowed_root: Path) -> None:
    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", allowed_root)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise WorkerError("missing_frontmatter")
    try:
        frontmatter_text, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise WorkerError("unclosed_frontmatter") from exc
    try:
        data = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError as exc:
        raise WorkerError(f"invalid_yaml: {exc}") from exc
    if not isinstance(data, dict):
        raise WorkerError("frontmatter_not_object")
    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        raise WorkerError(f"missing_required_fields: {', '.join(missing)}")
    return data, body


def render_markdown(frontmatter: dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body.rstrip()}\n"


def codex_inbox_paths(inbox_dir: Path) -> list[Path]:
    if not inbox_dir.exists():
        return []
    paths: list[Path] = []
    for path in sorted(inbox_dir.glob("*.md")):
        if path.name.startswith(".") or path.is_symlink() or not path.is_file():
            continue
        paths.append(ensure_inside(path, inbox_dir))
    return paths


def classify(frontmatter: dict[str, Any], body: str) -> tuple[str, str]:
    if str(frontmatter.get("type") or "") != "codex_request":
        return "invalid", "type_is_not_codex_request"
    if str(frontmatter.get("target") or "") not in VALID_TARGETS:
        return "needs_human", "target_is_not_codex"

    payload = "\n".join(
        [
            str(frontmatter.get("id") or ""),
            str(frontmatter.get("sender") or ""),
            str(frontmatter.get("created_at") or ""),
            body,
        ]
    ).lower()
    if any(term in payload for term in RISKY_TERMS):
        return "needs_human", "contains_runtime_or_write_risk_terms"
    return "stub_written", "safe_stub_only_phase"


def read_request(path: Path, inbox_dir: Path) -> dict[str, Any]:
    safe_path = ensure_inside(path, inbox_dir)
    content = safe_path.read_bytes()
    if len(content) > MAX_BYTES:
        raise WorkerError(f"file_too_large:{len(content)}>{MAX_BYTES}")
    text = content.decode("utf-8")
    frontmatter, body = parse_frontmatter(text)
    message_id = str(frontmatter["id"])
    status, reason = classify(frontmatter, body)
    return {
        "path": safe_path,
        "path_rel": project_relative(safe_path),
        "sha256": sha256_bytes(content),
        "frontmatter": frontmatter,
        "body": body,
        "message_id": message_id,
        "status": status,
        "reason": reason,
    }


def select_one_request(inbox_dir: Path, requested_file: Path | None) -> dict[str, Any]:
    if requested_file is not None:
        path = ensure_inside((inbox_dir / requested_file).resolve() if not requested_file.is_absolute() else requested_file, inbox_dir)
        if not path.exists():
            raise WorkerError(f"request_file_not_found: {path}")
        return read_request(path, inbox_dir)

    paths = codex_inbox_paths(inbox_dir)
    if not paths:
        raise WorkerError("no_pending_codex_requests")
    if len(paths) > 1:
        raise WorkerError("multiple_pending_codex_requests; use --file")
    return read_request(paths[0], inbox_dir)


def response_path(outbox_dir: Path, message_id: str, now: datetime) -> Path:
    stamp = now.strftime("%Y-%m-%dT%H%M%SZ")
    stem = f"{stamp}_codex-autoreply-{slug(message_id)}"
    candidate = ensure_inside(outbox_dir / f"{stem}.md", outbox_dir)
    index = 2
    while candidate.exists():
        candidate = ensure_inside(outbox_dir / f"{stem}-{index}.md", outbox_dir)
        index += 1
    return candidate


def render_stub_response(request: dict[str, Any], now: datetime) -> str:
    message_id = str(request["message_id"])
    status = str(request["status"])
    frontmatter = {
        "id": f"codex-autoreply-{now.strftime('%Y%m%d-%H%M%S')}-{slug(message_id)}",
        "type": "codex_response",
        "created_at": utc_iso(now),
        "sender": "codex-autoreply-worker",
        "target": "noema",
        "reply_to": message_id,
        "status": status,
        "source_path": request["path_rel"],
        "source_sha256": request["sha256"],
        "mode": "stub",
    }
    if status == "stub_written":
        body = [
            f"Codex request `{message_id}` was received by the autoreply worker.",
            "",
            "This is a stub response. Automatic model execution is not enabled in this phase.",
            "",
            f"Reason: `{request['reason']}`",
        ]
    else:
        body = [
            f"Codex request `{message_id}` was not auto-answered.",
            "",
            "The request needs human/Codex review before an automatic answer is safe.",
            "",
            f"Reason: `{request['reason']}`",
        ]
    return render_markdown(frontmatter, "\n".join(body))


def unique_archive_path(processed_root: Path, filename: str, sha256: str, now: datetime) -> Path:
    month_root = ensure_inside(processed_root / utc_month(now), processed_root)
    candidate = ensure_inside(month_root / filename, processed_root)
    if not candidate.exists():
        return candidate
    candidate = ensure_inside(month_root / f"{Path(filename).stem}.{sha256[:12]}{Path(filename).suffix}", processed_root)
    index = 2
    while candidate.exists():
        candidate = ensure_inside(month_root / f"{candidate.stem}-{index}{candidate.suffix}", processed_root)
        index += 1
    return candidate


def archive_request(request: dict[str, Any], processed_root: Path, now: datetime) -> Path:
    source = ensure_inside(request["path"], request["path"].parent)
    target = unique_archive_path(processed_root, source.name, str(request["sha256"]), now)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(target))
    return target


def process_once(
    request: dict[str, Any],
    runtime_root: Path,
    processed_root: Path,
    *,
    write_stub: bool,
) -> dict[str, Any]:
    now = utc_now()
    state_path = ensure_inside(runtime_root / STATE_RELATIVE_PATH, runtime_root)
    outbox_dir = ensure_inside(runtime_root / OUTBOX_RELATIVE_DIR, runtime_root)
    processed_root = processed_root.resolve()
    state = load_json(state_path, {"version": 1, "processed": {}, "errors": []})
    state.setdefault("version", 1)
    state.setdefault("processed", {})
    state.setdefault("errors", [])

    message_id = str(request["message_id"])
    existing = state["processed"].get(message_id)
    if existing and existing.get("sha256") == request["sha256"]:
        return {
            "status": "already_processed",
            "message_id": message_id,
            "response_path": existing.get("response_path"),
            "archive_path": existing.get("archive_path"),
        }
    if existing and existing.get("sha256") != request["sha256"]:
        raise WorkerError("message_id_sha256_conflict")

    if not write_stub:
        return {
            "status": "would_process",
            "message_id": message_id,
            "request_status": request["status"],
            "reason": request["reason"],
            "would_write_outbox": True,
            "would_archive": True,
        }

    outbox_path = response_path(outbox_dir, message_id, now)
    atomic_write_text(outbox_path, render_stub_response(request, now), outbox_dir)
    archive_path = archive_request(request, processed_root, now)
    entry = {
        "message_id": message_id,
        "sha256": request["sha256"],
        "status": request["status"],
        "reason": request["reason"],
        "processed_at": utc_iso(now),
        "source_path": request["path_rel"],
        "response_path": project_relative(outbox_path),
        "archive_path": project_relative(archive_path),
        "mode": "stub",
    }
    state["processed"][message_id] = entry
    save_json(state_path, state, runtime_root)
    return entry


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process one local Codex inbox request into bridge outbox.")
    parser.add_argument("--inbox-root", type=Path, default=Path(os.environ.get("NOEMA_CODEX_INBOX", DEFAULT_CODEX_INBOX_ROOT)))
    parser.add_argument(
        "--processed-root",
        type=Path,
        default=Path(os.environ.get("NOEMA_CODEX_PROCESSED", DEFAULT_CODEX_PROCESSED_ROOT)),
    )
    parser.add_argument("--runtime-root", type=Path, default=Path(os.environ.get("NOEMA_BRIDGE_ROOT", DEFAULT_RUNTIME_ROOT)))
    parser.add_argument("--file", type=Path, help="Process a specific inbox file. Relative paths are resolved inside inbox-root.")
    parser.add_argument("--write-stub", action="store_true", help="Write one stub response and archive the request.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    inbox_dir = args.inbox_root.resolve()
    runtime_root = args.runtime_root.resolve()
    processed_root = args.processed_root.resolve()
    try:
        request = select_one_request(inbox_dir, args.file)
        result = process_once(request, runtime_root, processed_root, write_stub=args.write_stub)
        output = {
            "version": 1,
            "mode": "write_stub" if args.write_stub else "dry_run",
            "generated_at": utc_iso(),
            "request": {
                "path": request["path_rel"],
                "message_id": request["message_id"],
                "sha256": request["sha256"],
                "status": request["status"],
                "reason": request["reason"],
            },
            "result": result,
            "side_effects": {
                "writes_outbox": bool(args.write_stub),
                "archives_request": bool(args.write_stub),
                "commits": False,
                "pushes": False,
            },
        }
        if args.json:
            print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
        else:
            print(f"codex_autoreply_worker mode={output['mode']}")
            print(f"request={request['path_rel']} message_id={request['message_id']}")
            print(f"status={request['status']} reason={request['reason']}")
            print(f"result={result}")
        return 0
    except WorkerError as exc:
        output = {
            "version": 1,
            "mode": "write_stub" if args.write_stub else "dry_run",
            "generated_at": utc_iso(),
            "error": str(exc),
        }
        if args.json:
            print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
        else:
            print(f"ERROR: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
