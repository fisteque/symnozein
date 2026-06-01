#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml


DEFAULT_PROJECT_ROOT = Path("/home/fiste/Noema")
DEFAULT_REPO_ROOT = DEFAULT_PROJECT_ROOT / "symnozein"
DEFAULT_RUNTIME_ROOT = DEFAULT_PROJECT_ROOT / "bridge"
DEFAULT_MAX_BYTES = 64 * 1024
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
        "path": str(runtime_root / "state" / "codex_reader_state.json"),
        "note": "Runtime-local state only. The dry-run script does not create or update this file.",
        "schema": {
            "version": 1,
            "processed": {
                "<message_id>": {
                    "message_id": "string",
                    "sha256": "sha256(content)",
                    "status": "responded|declined|needs_human|invalid|dry_run_seen",
                    "read_at": "UTC ISO-8601 timestamp",
                    "response_path": "body/bridge/outbox/codex/<file>.md or null",
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dry-run Codex inbox reader.")
    parser.add_argument("--repo-root", type=Path, default=Path(os.environ.get("NOEMA_REPO_ROOT", DEFAULT_REPO_ROOT)))
    parser.add_argument(
        "--runtime-root",
        type=Path,
        default=Path(os.environ.get("NOEMA_BRIDGE_ROOT", DEFAULT_RUNTIME_ROOT)),
    )
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    runtime_root = args.runtime_root.resolve()
    body_root = ensure_inside(repo_root / "body", repo_root)
    inbox_dir = ensure_inside(body_root / "bridge" / "inbox" / "messages" / "codex", body_root)

    result = {
        "version": 1,
        "mode": "dry_run",
        "generated_at": utc_iso(),
        "inbox_dir": inbox_dir.relative_to(repo_root).as_posix(),
        "state_spec": state_spec(runtime_root),
        "allowed_classes": sorted(ALLOWED_CLASSES),
        "messages": [inspect_message(path, inbox_dir, args.max_bytes) for path in message_paths(inbox_dir)],
        "side_effects": {
            "writes_files": False,
            "writes_outbox": False,
            "commits": False,
            "pushes": False,
        },
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    print(f"Codex inbox reader dry-run: {result['inbox_dir']}")
    print(f"State path spec: {result['state_spec']['path']}")
    print("Side effects: none")
    for item in result["messages"]:
        print(
            "- "
            f"{item.get('message_id') or '(no id)'} "
            f"class={item['class']} status={item['status']} "
            f"sha256={item.get('sha256', '(none)')} path={item['path']}"
        )
        print(f"  reason={item['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
