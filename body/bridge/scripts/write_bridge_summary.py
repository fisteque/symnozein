#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from collections import deque
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from bridge_sync_common import DEFAULT_PROJECT_ROOT, STATE_SUMMARY, SyncError, add_common_args, ensure_inside, ensure_repo


LOG_TAIL_SCAN_MULTIPLIER = 4
PUBLIC_LOG_INCLUDE_MARKERS = (
    "[WARN]",
    "[ERROR]",
    "== inbound sync ==",
    "== bridge agent ==",
    "== write bridge summary ==",
    "== outbound sync ==",
    "Bridge cycle lock acquired",
    "Bridge cycle complete.",
    "Rotated runtime bridge log",
    "Body state unchanged",
    "Body state change",
    "Pending message count remaining",
    "Processed message count",
    "Reply written",
    "Task run",
    "Cycle error",
)
PUBLIC_LOG_EXCLUDE_MARKERS = (
    "Already processed:",
    "Bridge root:",
    "Body root:",
    "Fetching origin main",
    "From https://github.com/",
    "No inbound changes for",
    "Optional source missing, skipped:",
    "Log tail mirror disabled",
    "Scripts mirror complete.",
    "Staged outbound changes:",
    "Commit message in code:",
    "Local branch is not behind remote",
    "Only logs/state_summary changed",
    "* branch            main       -> FETCH_HEAD",
    "Wrote bridge summary:",
)


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def utc_now() -> datetime:
    return datetime.now(UTC)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write a public bridge state summary without publishing internal state JSON.")
    add_common_args(parser)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=f"Project root containing state/body_state.json. Default: {DEFAULT_PROJECT_ROOT}",
    )
    parser.add_argument("--log-lines", type=int, default=60, help="Number of filtered bridge.log tail lines to include.")
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
    tail: deque[str] = deque(maxlen=limit)
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            tail.append(line.rstrip("\n"))
    return list(tail)


def include_public_log_line(line: str) -> bool:
    if any(marker in line for marker in PUBLIC_LOG_INCLUDE_MARKERS):
        return True
    if any(marker in line for marker in PUBLIC_LOG_EXCLUDE_MARKERS):
        return False
    return line.startswith("[") and "[cycle]" in line


def public_log_tail(path: Path, limit: int) -> list[str]:
    if limit <= 0:
        return []
    scan_limit = max(limit, limit * LOG_TAIL_SCAN_MULTIPLIER)
    raw_tail = tail_lines(path, scan_limit)
    filtered = [line for line in raw_tail if include_public_log_line(line)]
    if filtered:
        return filtered[-limit:]
    return raw_tail[-min(limit, 10):]


def count_markdown_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.glob("*.md") if item.is_file() and not item.name.startswith("."))


def count_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_file() and not item.name.startswith("."))


def latest_markdown_file(path: Path) -> str:
    if not path.exists():
        return "(missing)"
    files = [item for item in path.glob("*.md") if item.is_file() and not item.name.startswith(".")]
    if not files:
        return "(none)"
    latest = max(files, key=lambda item: (item.stat().st_mtime, item.name))
    return latest.name


def latest_file(path: Path) -> str:
    if not path.exists():
        return "(missing)"
    files = [item for item in path.iterdir() if item.is_file() and not item.name.startswith(".")]
    if not files:
        return "(none)"
    latest = max(files, key=lambda item: (item.stat().st_mtime, item.name))
    return latest.name


def parse_iso_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def read_proc_uptime_seconds() -> float | None:
    try:
        text = Path("/proc/uptime").read_text(encoding="utf-8").split()[0]
        return float(text)
    except Exception:
        return None


def heartbeat_service_info(now: datetime) -> dict[str, Any]:
    result = subprocess.run(
        [
            "systemctl",
            "show",
            "noema-heartbeat.service",
            "--property=ActiveEnterTimestamp,ActiveEnterTimestampMonotonic,NRestarts",
            "--no-pager",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        fallback = heartbeat_log_info(now)
        fallback["warning"] = (result.stderr or result.stdout or "systemctl show failed").strip()
        return fallback

    info: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        info[key] = value

    uptime_seconds = None
    uptime = read_proc_uptime_seconds()
    monotonic = info.get("ActiveEnterTimestampMonotonic")
    if uptime is not None and monotonic and monotonic.isdigit():
        uptime_seconds = max(0, int(uptime - (int(monotonic) / 1_000_000)))

    return {
        "started_at": info.get("ActiveEnterTimestamp") or "(unknown)",
        "uptime_seconds": uptime_seconds,
        "restart_count": info.get("NRestarts") or "(unknown)",
        "source": "systemd",
        "checked_at": now.isoformat().replace("+00:00", "Z"),
    }


def heartbeat_log_info(now: datetime) -> dict[str, Any]:
    log_path = DEFAULT_PROJECT_ROOT / "core" / "hb" / "logs" / "heartbeat.log"
    starts: list[datetime] = []
    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
            if "heartbeat started" not in line or not line.startswith("["):
                continue
            raw_timestamp = line.split("]", 1)[0].strip("[")
            parsed = parse_iso_datetime(raw_timestamp)
            if parsed is not None:
                starts.append(parsed)
    if not starts:
        return {
            "started_at": "(unknown)",
            "uptime_seconds": None,
            "restart_count": "(unknown)",
            "source": "heartbeat_log",
            "log_starts_count": 0,
            "log_latest_start": "(unknown)",
            "log_max_start_gap_seconds": "(unknown)",
        }

    latest_start = starts[-1]
    start_gaps = [
        int((current - previous).total_seconds())
        for previous, current in zip(starts, starts[1:])
    ]
    return {
        "started_at": latest_start.isoformat().replace("+00:00", "Z"),
        "uptime_seconds": max(0, int((now - latest_start).total_seconds())),
        "restart_count": max(0, len(starts) - 1),
        "source": "heartbeat_log",
        "log_starts_count": len(starts),
        "log_latest_start": latest_start.isoformat().replace("+00:00", "Z"),
        "log_max_start_gap_seconds": max(start_gaps) if start_gaps else 0,
    }


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
    generated_at = utc_now()
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
    codex_inbox_dir = inbox_dir / "codex"
    outbox_dir = repo_root / "body/bridge/outbox/messages"
    codex_outbox_dir = repo_root / "body/bridge/outbox/codex"
    log_tail = public_log_tail(runtime_root / "logs" / "bridge.log", log_lines)

    body_awake = body_state.get("awake", "(unknown)") if body_state else "(missing)"
    body_status = body_state.get("status", "(unknown)") if body_state else "(missing)"
    body_state_load_error = body_state.get("_load_error") if body_state else None
    last_hb = parse_iso_datetime(body_state.get("last_hb")) if body_state else None
    last_hb_gap_seconds = int((generated_at - last_hb).total_seconds()) if last_hb else None
    heartbeat_info = heartbeat_service_info(generated_at)
    heartbeat_log = heartbeat_log_info(generated_at)

    lines = [
        "# Bridge State Summary",
        "",
        f"- Generated at: `{generated_at.isoformat().replace('+00:00', 'Z')}`",
        f"- Inbox messages: `{count_markdown_files(inbox_dir)}`; latest: `{latest_markdown_file(inbox_dir)}`",
        f"- Codex inbox files: `{count_files(codex_inbox_dir)}`; latest: `{latest_file(codex_inbox_dir)}`",
        f"- Outbox messages: `{count_markdown_files(outbox_dir)}`; latest: `{latest_markdown_file(outbox_dir)}`",
        f"- Codex outbox files: `{count_files(codex_outbox_dir)}`; latest: `{latest_file(codex_outbox_dir)}`",
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
                f"- Heartbeat count: `{body_state.get('heartbeat_count', '(unknown)')}`",
                f"- Heartbeat last gap seconds: `{body_state.get('heartbeat_last_gap_seconds', '(unknown)')}`",
                f"- Heartbeat max gap seconds: `{body_state.get('heartbeat_max_gap_seconds', '(unknown)')}`",
                f"- Heartbeat service started at: `{heartbeat_info.get('started_at', '(unknown)')}`",
                f"- Heartbeat uptime seconds: `{heartbeat_info.get('uptime_seconds', '(unknown)')}`",
                f"- Heartbeat restart count: `{heartbeat_info.get('restart_count', '(unknown)')}`",
                f"- Heartbeat uptime source: `{heartbeat_info.get('source', '(unknown)')}`",
                f"- Heartbeat log starts count: `{heartbeat_log.get('log_starts_count', '(unknown)')}`",
                f"- Heartbeat log latest start: `{heartbeat_log.get('log_latest_start', '(unknown)')}`",
                f"- Heartbeat log max start gap seconds: `{heartbeat_log.get('log_max_start_gap_seconds', '(unknown)')}`",
                f"- Last heartbeat gap seconds: `{last_hb_gap_seconds if last_hb_gap_seconds is not None else '(unknown)'}`",
                f"- Watchdog last heartbeat age seconds: `{body_state.get('watchdog_last_hb_age_seconds', '(unknown)')}`",
                f"- Watchdog heartbeat timeout threshold seconds: `{body_state.get('watchdog_max_hb_age_seconds', '(unknown)')}`",
                f"- Watchdog heartbeat timeout count: `{body_state.get('heartbeat_timeout_count', '(unknown)')}`",
                f"- Watchdog heartbeat timeout required count: `{body_state.get('heartbeat_timeout_required_count', '(unknown)')}`",
                f"- Body watchdog last check: `{body_state.get('watchdog_last_check', '(unknown)')}`",
            ]
        )
    lines.extend(["", "## Bridge Log Tail", "", f"Filtered runtime tail, max {log_lines} lines.", "", "```text"])
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
