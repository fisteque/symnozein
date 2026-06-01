#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml


DEFAULT_PROJECT_ROOT = Path("/home/fiste/Noema")
DEFAULT_REPO_ROOT = DEFAULT_PROJECT_ROOT / "symnozein"
DEFAULT_RUNTIME_ROOT = DEFAULT_PROJECT_ROOT / "bridge"
DEFAULT_MAX_BYTES = 64 * 1024
STATE_RELATIVE_PATH = Path("state/codex_reader_state.json")
OUTBOX_RELATIVE_DIR = Path("body/bridge/outbox/codex")
SAFE_STUB_CLASSES = {
    "design_review",
    "documentation_review",
    "status_summary",
    "safety_review",
}
ALLOWED_CLASSES = {
    "design_review",
    "documentation_review",
    "status_summary",
    "safety_review",
    "needs_human",
    "invalid",
}
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
    "write response",
    "write to outbox",
    "commit",
    "runtime logic",
)


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def ensure_inside(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise ValueError(f"Path outside allowed root: {path}")
    return resolved_path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def slug(value: str, limit: int = 80) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip(".-")
    return (safe or "no-id")[:limit]


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {"version": 1, "processed": {}, "errors": []}
    with state_path.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    if not isinstance(state, dict):
        raise ValueError("codex reader state is not a JSON object")
    state.setdefault("version", 1)
    state.setdefault("processed", {})
    state.setdefault("errors", [])
    if not isinstance(state["processed"], dict) or not isinstance(state["errors"], list):
        raise ValueError("codex reader state has invalid processed/errors shape")
    return state


def save_state(state_path: Path, state: dict[str, Any]) -> None:
    atomic_write_text(state_path, json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def parse_frontmatter(text: str) -> tuple[dict[str, Any] | None, str, str | None]:
    if not text.startswith("---\n"):
        return None, text, "missing_frontmatter"
    try:
        frontmatter_text, body = text[4:].split("\n---\n", 1)
    except ValueError:
        return None, text, "unclosed_frontmatter"
    try:
        data = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError as exc:
        return None, body, f"invalid_yaml: {exc}"
    if not isinstance(data, dict):
        return None, body, "frontmatter_not_object"
    return data, body, None


def classify(frontmatter: dict[str, Any] | None, body: str, parse_error: str | None) -> tuple[str, str]:
    if parse_error or frontmatter is None:
        return "invalid", parse_error or "invalid_frontmatter"

    message_type = str(frontmatter.get("type") or "")
    if message_type != "codex_request":
        return "invalid", "type_is_not_codex_request"

    target = str(frontmatter.get("target") or "")
    if target not in {"codex", "rpi5-bridge-agent", "rpi5-bridge"}:
        return "needs_human", "target_is_not_a_standard_codex_target"

    payload = "\n".join(
        [
            str(frontmatter.get("id") or ""),
            str(frontmatter.get("sender") or ""),
            str(frontmatter.get("created_at") or ""),
            json.dumps(frontmatter.get("codex") or {}, ensure_ascii=False, sort_keys=True),
            body,
        ]
    ).lower()

    if any(term in payload for term in RISKY_TERMS):
        if "dry-run" in payload or "dry run" in payload:
            return "design_review", "dry_run_design_request_with_runtime_boundaries"
        return "needs_human", "contains_runtime_or_write_risk_terms"

    if any(term in payload for term in ("design", "navrh", "architektur", "reader", "dry-run", "dry run")):
        return "design_review", "design_or_architecture_request"
    if any(term in payload for term in ("document", "documentation", "docs", "dokument")):
        return "documentation_review", "documentation_request"
    if any(term in payload for term in ("status", "summary", "stav", "prehled")):
        return "status_summary", "status_or_summary_request"
    if any(term in payload for term in ("safety", "bezpec", "risk", "rizik")):
        return "safety_review", "safety_or_risk_request"
    return "needs_human", "unknown_request_class"


def message_paths(inbox_dir: Path) -> list[Path]:
    if not inbox_dir.exists():
        return []
    paths: list[Path] = []
    for path in sorted(inbox_dir.glob("*.md")):
        if path.name.startswith(".") or path.is_symlink() or not path.is_file():
            continue
        paths.append(ensure_inside(path, inbox_dir))
    return paths


def inspect_message(path: Path, inbox_dir: Path, max_bytes: int) -> dict[str, Any]:
    safe_path = ensure_inside(path, inbox_dir)
    rel_path = f"body/bridge/inbox/messages/codex/{safe_path.name}"
    size = safe_path.stat().st_size
    if size > max_bytes:
        return {
            "path": rel_path,
            "status": "skipped",
            "class": "invalid",
            "reason": f"file_too_large:{size}>{max_bytes}",
            "would_write": False,
        }

    content = safe_path.read_bytes()
    sha256 = sha256_bytes(content)
    text = content.decode("utf-8", errors="replace")
    frontmatter, body, parse_error = parse_frontmatter(text)
    request_class, reason = classify(frontmatter, body, parse_error)
    item = {
        "path": rel_path,
        "sha256": sha256,
        "status": "would_read" if request_class != "invalid" else "invalid",
        "class": request_class,
        "reason": reason,
        "would_write": False,
        "would_response_path": None,
    }
    if frontmatter:
        item.update(
            {
                "message_id": json_safe(frontmatter.get("id")),
                "type": json_safe(frontmatter.get("type")),
                "sender": json_safe(frontmatter.get("sender")),
                "target": json_safe(frontmatter.get("target")),
                "created_at": json_safe(frontmatter.get("created_at")),
            }
        )
    return item


def state_spec(runtime_root: Path) -> dict[str, Any]:
    return {
        "path": str(runtime_root / STATE_RELATIVE_PATH),
        "note": "Runtime-local state only. Dry-run mode does not create or update this file.",
        "schema": {
            "version": 1,
            "processed": {
                "<message_id>": {
                    "message_id": "string",
                    "sha256": "sha256(content)",
                    "status": "stub_written|needs_human|invalid|conflict",
                    "task_class": "design_review|documentation_review|status_summary|safety_review|needs_human|invalid",
                    "read_at": "UTC ISO-8601 timestamp",
                    "response_path": "body/bridge/outbox/codex/<file>.md or null",
                    "source_path": "body/bridge/inbox/messages/codex/<file>.md",
                }
            },
            "errors": [
                {
                    "message_id": "string or null",
                    "path": "body-relative path",
                    "error": "string",
                    "error_at": "UTC ISO-8601 timestamp",
                }
            ],
        },
    }


def stub_status(task_class: str) -> str:
    if task_class in SAFE_STUB_CLASSES:
        return "stub_written"
    if task_class == "invalid":
        return "invalid"
    return "needs_human"


def render_stub_response(item: dict[str, Any], status: str, read_at: str) -> str:
    message_id = str(item.get("message_id") or "")
    task_class = str(item["class"])
    frontmatter = {
        "type": "codex_response",
        "author": "Codex Reader",
        "sender": "codex-reader",
        "target": "noema",
        "reply_to": message_id,
        "status": status,
        "task_class": task_class,
        "source_sha256": item.get("sha256"),
        "source_path": item.get("path"),
        "created_at": read_at,
    }
    body = [
        f"Request `{message_id}` was detected and classified as `{task_class}`.",
        "",
    ]
    if status == "stub_written":
        body.extend(
            [
                "This is only a reader stub. Real Codex processing and a final answer are still needed.",
                "",
                f"Classification reason: {item.get('reason')}",
            ]
        )
    elif status == "needs_human":
        body.extend(
            [
                "This request needs a human decision before Codex processing continues.",
                "",
                f"Classification reason: {item.get('reason')}",
            ]
        )
    else:
        body.extend(
            [
                "This request could not be processed as a normal Codex request.",
                "",
                f"Classification reason: {item.get('reason')}",
            ]
        )
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True) + "---\n\n" + "\n".join(body) + "\n"


def unique_response_path(outbox_dir: Path, message_id: str, timestamp: str) -> Path:
    stem = f"{timestamp.replace(':', '').replace('-', '')}_codex-reader-stub-{slug(message_id)}"
    candidate = outbox_dir / f"{stem}.md"
    index = 2
    while candidate.exists():
        candidate = outbox_dir / f"{stem}-{index}.md"
        index += 1
    return ensure_inside(candidate, outbox_dir)


def process_messages(
    messages: list[dict[str, Any]],
    repo_root: Path,
    runtime_root: Path,
) -> dict[str, Any]:
    state_path = ensure_inside(runtime_root / STATE_RELATIVE_PATH, runtime_root)
    outbox_dir = ensure_inside(repo_root / OUTBOX_RELATIVE_DIR, repo_root)
    state = load_state(state_path)
    processed = state["processed"]
    errors = state["errors"]
    results: list[dict[str, Any]] = []

    for item in messages:
        read_at = utc_iso()
        message_id = item.get("message_id")
        if not message_id:
            error = {
                "message_id": None,
                "path": item["path"],
                "error": "missing_message_id",
                "error_at": read_at,
            }
            errors.append(error)
            results.append({**item, "write_status": "invalid", "response_path": None, "error": error["error"]})
            continue

        message_id = str(message_id)
        existing = processed.get(message_id)
        if existing:
            if existing.get("sha256") == item.get("sha256"):
                results.append(
                    {
                        **item,
                        "write_status": "already_processed",
                        "response_path": existing.get("response_path"),
                    }
                )
                continue

            error = {
                "message_id": message_id,
                "path": item["path"],
                "error": "message_id_sha256_conflict",
                "error_at": read_at,
                "previous_sha256": existing.get("sha256"),
                "new_sha256": item.get("sha256"),
            }
            errors.append(error)
            processed[message_id] = {
                "message_id": message_id,
                "sha256": item.get("sha256"),
                "status": "conflict",
                "task_class": item["class"],
                "read_at": read_at,
                "response_path": None,
                "source_path": item["path"],
                "previous_sha256": existing.get("sha256"),
            }
            results.append({**item, "write_status": "conflict", "response_path": None, "error": error["error"]})
            continue

        status = stub_status(str(item["class"]))
        response_rel_path: str | None = None
        response_path: Path | None = None
        if status in {"stub_written", "needs_human", "invalid"}:
            timestamp = read_at.replace("+00:00", "Z").replace("Z", "")
            response_path = unique_response_path(outbox_dir, message_id, timestamp)
            response_rel_path = response_path.relative_to(repo_root).as_posix()
            if not response_rel_path.startswith(f"{OUTBOX_RELATIVE_DIR.as_posix()}/"):
                raise ValueError(f"Generated response outside allowed outbox: {response_rel_path}")
            atomic_write_text(response_path, render_stub_response(item, status, read_at))

        processed[message_id] = {
            "message_id": message_id,
            "sha256": item.get("sha256"),
            "status": status,
            "task_class": item["class"],
            "read_at": read_at,
            "response_path": response_rel_path,
            "source_path": item["path"],
        }
        results.append({**item, "write_status": status, "response_path": response_rel_path})

    save_state(state_path, state)
    return {
        "state_path": str(state_path),
        "messages": results,
        "state": state,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Codex inbox reader.")
    parser.add_argument("--repo-root", type=Path, default=Path(os.environ.get("NOEMA_REPO_ROOT", DEFAULT_REPO_ROOT)))
    parser.add_argument(
        "--runtime-root",
        type=Path,
        default=Path(os.environ.get("NOEMA_BRIDGE_ROOT", DEFAULT_RUNTIME_ROOT)),
    )
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    parser.add_argument("--write-stub", action="store_true", help="Write manual stub responses and runtime-local state.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    runtime_root = args.runtime_root.resolve()
    body_root = ensure_inside(repo_root / "body", repo_root)
    inbox_dir = ensure_inside(body_root / "bridge" / "inbox" / "messages" / "codex", body_root)

    messages = [inspect_message(path, inbox_dir, args.max_bytes) for path in message_paths(inbox_dir)]
    result = {
        "version": 1,
        "mode": "write_stub" if args.write_stub else "dry_run",
        "generated_at": utc_iso(),
        "inbox_dir": inbox_dir.relative_to(repo_root).as_posix(),
        "state_spec": state_spec(runtime_root),
        "allowed_classes": sorted(ALLOWED_CLASSES),
        "messages": messages,
        "side_effects": {
            "writes_files": bool(args.write_stub),
            "writes_outbox": bool(args.write_stub),
            "commits": False,
            "pushes": False,
        },
    }

    if args.write_stub:
        write_result = process_messages(messages, repo_root, runtime_root)
        result["messages"] = write_result["messages"]
        result["state_path"] = write_result["state_path"]

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    print(f"Codex inbox reader {result['mode']}: {result['inbox_dir']}")
    print(f"State path spec: {result['state_spec']['path']}")
    if args.write_stub:
        print("Side effects: writes runtime-local state and codex outbox stubs only")
    else:
        print("Side effects: none")
    for item in result["messages"]:
        print(
            "- "
            f"{item.get('message_id') or '(no id)'} "
            f"class={item['class']} status={item['status']} "
            f"write_status={item.get('write_status', 'none')} "
            f"sha256={item.get('sha256', '(none)')} path={item['path']}"
        )
        if item.get("response_path"):
            print(f"  response_path={item['response_path']}")
        print(f"  reason={item['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
