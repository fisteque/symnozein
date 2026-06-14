#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
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
MAX_CODEX_RESPONSE_BYTES = 128 * 1024
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
NEGATION_MARKERS = (
    "do not",
    "does not",
    "don't",
    "dont",
    "not require",
    "nesmi",
    "nesmí",
    "nemen",
    "neměň",
    "nemaz",
    "neinstal",
    "nerestart",
    "necommit",
    "nepush",
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


def safety_filtered_payload(payload: str) -> str:
    lines: list[str] = []
    for line in payload.splitlines():
        stripped = line.strip()
        if any(marker in stripped for marker in NEGATION_MARKERS):
            continue
        lines.append(line)
    return "\n".join(lines)


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
    if any(term in safety_filtered_payload(payload) for term in RISKY_TERMS):
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


def response_frontmatter(request: dict[str, Any], now: datetime, *, status: str, mode: str) -> dict[str, Any]:
    message_id = str(request["message_id"])
    return {
        "id": f"codex-autoreply-{now.strftime('%Y%m%d-%H%M%S')}-{slug(message_id)}",
        "type": "codex_response",
        "created_at": utc_iso(now),
        "sender": "codex-autoreply-worker",
        "target": "noema",
        "reply_to": message_id,
        "status": status,
        "source_path": request["path_rel"],
        "source_sha256": request["sha256"],
        "mode": mode,
    }


def render_stub_response(request: dict[str, Any], now: datetime) -> str:
    message_id = str(request["message_id"])
    status = str(request["status"])
    frontmatter = response_frontmatter(request, now, status=status, mode="stub")
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


def codex_prompt(request: dict[str, Any]) -> str:
    frontmatter = request["frontmatter"]
    body = str(request["body"]).strip()
    return "\n".join(
        [
            "You are Codex running as a constrained Noema bridge autoreply worker.",
            "",
            "Task:",
            "- Answer the single codex_request below.",
            "- Do not edit files.",
            "- You may inspect local files read-only under /home/fiste/Noema when needed to answer.",
            "- Do not run commands except read-only inspection needed for the request.",
            "- Do not commit, push, delete, install, restart services, or change runtime state.",
            "- Return only the answer text that should be delivered to Noema.",
            "- Keep the answer concise and audit-friendly.",
            "",
            "Request frontmatter:",
            "```yaml",
            yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip(),
            "```",
            "",
            "Request body:",
            "```markdown",
            body or "(empty)",
            "```",
        ]
    )


def run_codex_exec(
    request: dict[str, Any],
    runtime_root: Path,
    *,
    codex_bin: str,
    model: str | None,
    timeout_seconds: int,
) -> str:
    state_dir = ensure_inside(runtime_root / "state", runtime_root)
    state_dir.mkdir(parents=True, exist_ok=True)
    output_path = ensure_inside(
        state_dir / f".codex-autoreply-output-{os.getpid()}-{slug(str(request['message_id']), 32)}.md",
        runtime_root,
    )
    prompt = codex_prompt(request)
    cmd = [
        codex_bin,
        "exec",
        "-c",
        'approval_policy="never"',
        "--sandbox",
        "read-only",
        "--cd",
        str(PROJECT_ROOT),
        "--output-last-message",
        str(output_path),
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append("-")
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout_seconds,
            check=False,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "").strip()
            raise WorkerError(f"codex_exec_failed:{result.returncode}: {detail[:1000]}")
        if not output_path.exists():
            raise WorkerError("codex_exec_missing_output")
        response_bytes = output_path.read_bytes()
        if len(response_bytes) > MAX_CODEX_RESPONSE_BYTES:
            raise WorkerError(f"codex_response_too_large:{len(response_bytes)}>{MAX_CODEX_RESPONSE_BYTES}")
        response = response_bytes.decode("utf-8").strip()
        if not response:
            raise WorkerError("codex_response_empty")
        return response
    except subprocess.TimeoutExpired as exc:
        raise WorkerError(f"codex_exec_timeout:{timeout_seconds}") from exc
    finally:
        try:
            output_path.unlink()
        except FileNotFoundError:
            pass


def render_codex_response(request: dict[str, Any], now: datetime, answer: str) -> str:
    frontmatter = response_frontmatter(request, now, status="answered", mode="codex_exec")
    body = [
        answer.strip(),
        "",
        "---",
        "",
        f"source_request: `{request['message_id']}`",
        f"source_sha256: `{request['sha256']}`",
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
    run_codex: bool,
    allow_needs_human: bool,
    codex_bin: str,
    model: str | None,
    timeout_seconds: int,
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

    if not write_stub and not run_codex:
        return {
            "status": "would_process",
            "message_id": message_id,
            "request_status": request["status"],
            "reason": request["reason"],
            "would_write_outbox": True,
            "would_archive": True,
        }

    outbox_path = response_path(outbox_dir, message_id, now)
    mode = "stub"
    final_status = request["status"]
    if run_codex:
        if request["status"] == "needs_human" and not allow_needs_human:
            raise WorkerError("request_needs_human; rerun with --allow-needs-human after review")
        answer = run_codex_exec(
            request,
            runtime_root,
            codex_bin=codex_bin,
            model=model,
            timeout_seconds=timeout_seconds,
        )
        rendered = render_codex_response(request, now, answer)
        mode = "codex_exec"
        final_status = "answered"
    else:
        rendered = render_stub_response(request, now)
    atomic_write_text(outbox_path, rendered, outbox_dir)
    archive_path = archive_request(request, processed_root, now)
    entry = {
        "message_id": message_id,
        "sha256": request["sha256"],
        "status": final_status,
        "reason": request["reason"],
        "processed_at": utc_iso(now),
        "source_path": request["path_rel"],
        "response_path": project_relative(outbox_path),
        "archive_path": project_relative(archive_path),
        "mode": mode,
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
    parser.add_argument("--run-codex", action="store_true", help="Run codex exec read-only and write its final answer.")
    parser.add_argument("--allow-needs-human", action="store_true", help="Allow codex exec for requests classified as needs_human.")
    parser.add_argument("--codex-bin", default=os.environ.get("NOEMA_CODEX_BIN", "codex"))
    parser.add_argument("--model", default=os.environ.get("NOEMA_CODEX_MODEL"))
    parser.add_argument("--timeout-seconds", type=int, default=int(os.environ.get("NOEMA_CODEX_TIMEOUT_SECONDS", "300")))
    parser.add_argument("--quiet-empty", action="store_true", help="Exit 0 when the Codex inbox has no pending request.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def mode_name(args: argparse.Namespace) -> str:
    if args.run_codex:
        return "run_codex"
    if args.write_stub:
        return "write_stub"
    return "dry_run"


def main() -> int:
    args = parse_args()
    inbox_dir = args.inbox_root.resolve()
    runtime_root = args.runtime_root.resolve()
    processed_root = args.processed_root.resolve()
    try:
        if args.write_stub and args.run_codex:
            raise WorkerError("--write-stub and --run-codex are mutually exclusive")
        request = select_one_request(inbox_dir, args.file)
        result = process_once(
            request,
            runtime_root,
            processed_root,
            write_stub=args.write_stub,
            run_codex=args.run_codex,
            allow_needs_human=args.allow_needs_human,
            codex_bin=args.codex_bin,
            model=args.model,
            timeout_seconds=args.timeout_seconds,
        )
        output = {
            "version": 1,
            "mode": mode_name(args),
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
                "writes_outbox": bool(args.write_stub or args.run_codex),
                "archives_request": bool(args.write_stub or args.run_codex),
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
        if args.quiet_empty and str(exc) == "no_pending_codex_requests":
            output = {
                "version": 1,
                "mode": mode_name(args),
                "generated_at": utc_iso(),
                "status": "idle",
                "message": "no_pending_codex_requests",
                "side_effects": {
                    "writes_outbox": False,
                    "archives_request": False,
                    "commits": False,
                    "pushes": False,
                },
            }
            if args.json:
                print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
            else:
                print("codex_autoreply_worker idle: no pending Codex requests")
            return 0
        output = {
            "version": 1,
            "mode": mode_name(args),
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
