#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from bridge_sync_common import DEFAULT_PROJECT_ROOT, STATE_SUMMARY, SyncError, add_common_args, ensure_inside, ensure_repo


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write a public bridge state summary without publishing internal state JSON.")
    add_common_args(parser)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=f"Project root containing state/body_state.json. Default: {DEFAULT_PROJECT_ROOT}",
    )
    parser.add_argument("--log-lines", type=int, default=20, help="Number of bridge.log tail lines to include.")
    return parser.parse_args()


def load_json(path: Path, *, tolerate_invalid: bool = False) -> dict[str, Any]:
    if not path.exists():
        return {}
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            break
        except json.JSONDecodeError as exc:
            last_error = exc
            if not tolerate_invalid or attempt == 2:
                if tolerate_invalid:
                    return {"_load_error": f"{type(exc).__name__}: {exc}"}
                raise
            time.sleep(0.1)
    else:
        if tolerate_invalid and last_error is not None:
            return {"_load_error": f"{type(last_error).__name__}: {last_error}"}
        return {}
    if not isinstance(data, dict):
        if tolerate_invalid:
            return {"_load_error": f"JSON file must contain an object: {path}"}
        raise SyncError(f"JSON file must contain an object: {path}")
    return data


def tail_lines(path: Path, limit: int) -> list[str]:
    if limit <= 0 or not path.exists():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[-limit:]


def count_markdown_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.glob("*.md") if item.is_file() and not item.name.startswith("."))


def latest_markdown_file(path: Path) -> str:
    if not path.exists():
        return "(missing)"
    files = [item for item in path.glob("*.md") if item.is_file() and not item.name.startswith(".")]
    if not files:
        return "(none)"
    latest = max(files, key=lambda item: (item.stat().st_mtime, item.name))
    return latest.name


def last_processed_message(processed: dict[str, Any]) -> tuple[str, dict[str, Any] | None]:
    messages = processed.get("messages")
    if not isinstance(messages, dict) or not messages:
        return "(none)", None
    entries: list[tuple[str, dict[str, Any]]] = [
        (str(message_id), entry)
        for message_id, entry in messages.items()
        if isinstance(entry, dict)
    ]
    if not entries:
        return "(none)", None
    entries.sort(key=lambda item: str(item[1].get("processed_at") or ""))
    return entries[-1]


def render_summary(runtime_root: Path, repo_root: Path, project_root: Path, log_lines: int) -> str:
    processed = load_json(runtime_root / "state" / "processed_messages.json")
    body_state = load_json(project_root / "state" / "body_state.json", tolerate_invalid=True)
    errors = processed.get("errors")
    if not isinstance(errors, list):
        errors = []

    last_message_id, last_message = last_processed_message(processed)
    messages = processed.get("messages")
    processed_count = len(messages) if isinstance(messages, dict) else 0
    last_error = errors[-1] if errors else None

    inbox_dir = repo_root / "body/bridge/inbox/messages"
    outbox_dir = repo_root / "body/bridge/outbox/messages"
    log_tail = tail_lines(runtime_root / "logs" / "bridge.log", log_lines)

    body_awake = body_state.get("awake", "(unknown)") if body_state else "(missing)"
    body_status = body_state.get("status", "(unknown)") if body_state else "(missing)"
    body_state_load_error = body_state.get("_load_error") if body_state else None

    lines = [
        "# Bridge State Summary",
        "",
        f"- Generated at: `{utc_iso()}`",
        f"- Inbox messages: `{count_markdown_files(inbox_dir)}`; latest: `{latest_markdown_file(inbox_dir)}`",
        f"- Outbox messages: `{count_markdown_files(outbox_dir)}`; latest: `{latest_markdown_file(outbox_dir)}`",
        f"- Last processed message: `{last_message_id}`",
        f"- Last processed status: `{last_message.get('status', '(unknown)') if last_message else '(none)'}`",
        f"- Processed count: `{processed_count}`",
        f"- Error count: `{len(errors)}`",
        f"- Last error: `{last_error.get('error', '(none)') if isinstance(last_error, dict) else '(none)'}`",
        f"- Body awake: `{body_awake}`",
        f"- Body status: `{body_status}`",
    ]

    if body_state_load_error:
        lines.append(f"- Body state read warning: `{body_state_load_error}`")

    if body_state:
        lines.extend(
            [
                f"- Body last heartbeat: `{body_state.get('last_hb', '(unknown)')}`",
                f"- Body watchdog last check: `{body_state.get('watchdog_last_check', '(unknown)')}`",
            ]
        )

    lines.extend(["", "## Bridge Log Tail", "", "```text"])
    lines.extend(log_tail or ["(no log lines)"])
    lines.extend(["```", ""])
    return "\n".join(lines)


def write_summary(runtime_root: Path, repo_root: Path, project_root: Path, log_lines: int) -> Path:
    repo_root = ensure_repo(repo_root)
    runtime_root = runtime_root.resolve()
    project_root = project_root.resolve()
    target = ensure_inside(repo_root / STATE_SUMMARY / "latest.md", repo_root)
    text = render_summary(runtime_root, repo_root, project_root, log_lines)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return target


def main() -> int:
    args = parse_args()
    try:
        target = write_summary(args.runtime_root, args.repo_root, args.project_root, args.log_lines)
        print(f"Wrote bridge summary: {target}")
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
