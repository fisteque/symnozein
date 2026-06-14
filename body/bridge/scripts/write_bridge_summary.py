#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from bridge_sync_common import DEFAULT_PROJECT_ROOT, STATE_SUMMARY, SyncError, add_common_args, ensure_inside, ensure_repo


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
    parser.add_argument("--log-lines", type=int, default=60, help="Deprecated no-op kept for compatibility.")
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


def project_relative(path: Path, project_root: Path) -> str:
    try:
        return path.resolve().relative_to(project_root.resolve()).as_posix()
    except ValueError:
        return path.name


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


def source_timestamp(data: dict[str, Any], keys: tuple[str, ...]) -> datetime | None:
    candidates: list[datetime] = []
    for key in keys:
        parsed = parse_iso_datetime(data.get(key))
        if parsed is not None:
            candidates.append(parsed)
    return max(candidates) if candidates else None


def newest_processed_timestamp(processed: dict[str, Any]) -> datetime | None:
    candidates: list[datetime] = []
    messages = processed.get("messages")
    if isinstance(messages, dict):
        for entry in messages.values():
            if isinstance(entry, dict):
                parsed = parse_iso_datetime(entry.get("processed_at"))
                if parsed is not None:
                    candidates.append(parsed)
    errors = processed.get("errors")
    if isinstance(errors, list):
        for entry in errors:
            if isinstance(entry, dict):
                parsed = parse_iso_datetime(entry.get("processed_at") or entry.get("created_at"))
                if parsed is not None:
                    candidates.append(parsed)
    return max(candidates) if candidates else None


def source_freshness_line(
    label: str,
    path: Path,
    project_root: Path,
    data: dict[str, Any],
    timestamp: datetime | None,
    now: datetime,
) -> str:
    if not path.exists():
        status = "missing"
    elif data.get("_load_error"):
        status = "invalid"
    else:
        status = "ok"
    timestamp_text = timestamp.isoformat().replace("+00:00", "Z") if timestamp is not None else "(unknown)"
    age_text = str(max(0, int((now - timestamp).total_seconds()))) if timestamp is not None else "(unknown)"
    return (
        f"- {label}: `{status}`; path: `{project_relative(path, project_root)}`; "
        f"timestamp: `{timestamp_text}`; age seconds: `{age_text}`"
    )


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


def nested_get(data: dict[str, Any], path: tuple[str, ...], default: Any = "(unknown)") -> Any:
    current: Any = data
    for key in path:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    if current is None:
        return default
    return current


def unit_state(body_health: dict[str, Any], unit: str) -> str:
    item = nested_get(body_health, ("units", "items", unit), {})
    if not isinstance(item, dict):
        return "(unknown)"
    active = item.get("ActiveState") or "(unknown)"
    sub = item.get("SubState")
    return f"{active}/{sub}" if sub else str(active)


def extend_body_health_lines(lines: list[str], body_health: dict[str, Any]) -> None:
    lines.extend(["", "## Body Health", ""])
    if not body_health:
        lines.append("- Body health: `(missing)`")
        return

    load_avg = body_health.get("load_average")
    if isinstance(load_avg, dict):
        load_text = f"{load_avg.get('1m', '(unknown)')} / {load_avg.get('5m', '(unknown)')} / {load_avg.get('15m', '(unknown)')}"
    else:
        load_text = "(unknown)"

    health_load_error = body_health.get("_load_error")
    if health_load_error:
        lines.append(f"- Body health read warning: `{health_load_error}`")

    lines.extend(
        [
            f"- Health generated at: `{body_health.get('generated_at', '(unknown)')}`",
            f"- CPU temperature C: `{body_health.get('cpu_temperature_c', '(unknown)')}`",
            f"- Load average 1m / 5m / 15m: `{load_text}`",
            f"- RAM used percent: `{nested_get(body_health, ('memory', 'used_percent'))}`",
            f"- Swap used percent: `{nested_get(body_health, ('swap', 'used_percent'))}`",
            f"- Root disk used percent: `{nested_get(body_health, ('disk', 'root', 'used_percent'))}`",
        ]
    )


def next_body_pulse_fallback() -> str:
    prague = ZoneInfo("Europe/Prague")
    now = datetime.now(prague)
    for day_offset in range(2):
        day = (now + timedelta(days=day_offset)).date()
        for hour in (0, 4, 8, 12, 16, 20):
            candidate = datetime.combine(day, datetime.min.time(), tzinfo=prague)
            candidate = candidate.replace(hour=hour)
            if candidate > now:
                return candidate.isoformat()
    return "(unknown)"


def next_timer_elapse(unit: str) -> str:
    fallback = next_body_pulse_fallback() if unit == "noema-body-pulse.timer" else "(unknown)"
    result = subprocess.run(
        [
            "systemctl",
            "show",
            unit,
            "--property=NextElapseUSecRealtime",
            "--no-pager",
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        return fallback
    for line in result.stdout.splitlines():
        if not line.startswith("NextElapseUSecRealtime="):
            continue
        value = line.split("=", 1)[1].strip()
        return value or fallback
    return fallback


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing_frontmatter")
    try:
        frontmatter_block, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("unclosed_frontmatter") from exc
    import yaml

    data = yaml.safe_load(frontmatter_block) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter_not_object")
    return data, body


def count_needs_human_codex_requests(codex_inbox_dir: Path) -> int:
    if not codex_inbox_dir.exists():
        return 0
    try:
        from codex_autoreply_worker import classify
    except Exception:
        classify = None

    count = 0
    for path in sorted(codex_inbox_dir.glob("*.md")):
        if path.name.startswith(".") or not path.is_file():
            continue
        try:
            frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            status = classify(frontmatter, body)[0] if classify is not None else "needs_human"
        except Exception:
            status = "needs_human"
        if status == "needs_human":
            count += 1
    return count


def render_summary(runtime_root: Path, repo_root: Path, project_root: Path, log_lines: int) -> str:
    generated_at = utc_now()
    processed_path = runtime_root / "state" / "processed_messages.json"
    body_state_path = project_root / "state" / "body_state.json"
    body_health_path = project_root / "state" / "body_health.json"
    sync_state_path = runtime_root / "state" / "bridge_sync_state.json"
    pulse_state_path = runtime_root / "state" / "body_pulse_state.json"
    processed = load_json(processed_path, tolerate_invalid=True)
    body_state = load_json(body_state_path, tolerate_invalid=True)
    body_health = load_json(body_health_path, tolerate_invalid=True)
    sync_state = load_json(sync_state_path, tolerate_invalid=True)
    pulse_state = load_json(pulse_state_path, tolerate_invalid=True)
    errors = processed.get("errors")
    if not isinstance(errors, list):
        errors = []

    last_message_id, last_message = last_processed_message(processed)
    messages = processed.get("messages")
    processed_count = len(messages) if isinstance(messages, dict) else 0
    last_error = errors[-1] if errors else None

    inbox_dir = runtime_root / "inbox/messages"
    codex_inbox_dir = project_root / "codex/inbox"
    outbox_dir = runtime_root / "outbox/messages"

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
        f"- Body awake: `{body_awake}`",
        f"- Body status: `{body_status}`",
    ]

    if body_state_load_error:
        lines.append(f"- Body state read warning: `{body_state_load_error}`")

    if body_state:
        lines.extend(
            [
                "",
                "## Body Heartbeat",
                "",
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
    else:
        lines.extend(["", "## Body Heartbeat", "", "- Body heartbeat: `(missing)`"])
    extend_body_health_lines(lines, body_health)
    lines.extend(
        [
            "",
            "## Bridge Sync",
            "",
            f"- Last inbound sync: `{sync_state.get('last_inbound_sync', '(missing)')}`",
            f"- Last outbound sync: `{sync_state.get('last_outbound_sync', '(missing)')}`",
            f"- Last outbound sync status: `{sync_state.get('last_outbound_sync_status', '(missing)')}`",
            f"- Last outbound commit: `{sync_state.get('last_outbound_commit', '(missing)')}`",
            "",
            "## Queues",
            "",
            f"- Bridge inbox pending: `{count_markdown_files(inbox_dir)}`",
            f"- Bridge outbox pending: `{count_markdown_files(outbox_dir)}`",
            f"- Codex runtime inbox files: `{count_files(codex_inbox_dir)}`",
            f"- Needs human count: `{count_needs_human_codex_requests(codex_inbox_dir)}`",
            f"- Last processed message: `{last_message_id}`",
            f"- Last processed status: `{last_message.get('status', '(unknown)') if last_message else '(none)'}`",
            f"- Processed count: `{processed_count}`",
            f"- Error count: `{len(errors)}`",
            f"- Last error: `{last_error.get('error', '(none)') if isinstance(last_error, dict) else '(none)'}`",
            "",
            "## Pulse",
            "",
            f"- Current pulse status: `{pulse_state.get('current_pulse_status', '(none)')}`",
            f"- Current pulse started: `{pulse_state.get('current_pulse_started_at', '(none)')}`",
            f"- Last body pulse: `{pulse_state.get('last_body_pulse', '(missing)')}`",
            f"- Last pulse commit: `{pulse_state.get('last_pulse_commit', '(missing)')}`",
            f"- Next scheduled pulse: `{next_timer_elapse('noema-body-pulse.timer')}`",
            "",
            "## Source Freshness",
            "",
            source_freshness_line(
                "Body state",
                body_state_path,
                project_root,
                body_state,
                source_timestamp(body_state, ("last_hb", "watchdog_last_check")),
                generated_at,
            ),
            source_freshness_line(
                "Body health",
                body_health_path,
                project_root,
                body_health,
                source_timestamp(body_health, ("generated_at",)),
                generated_at,
            ),
            source_freshness_line(
                "Processed messages",
                processed_path,
                project_root,
                processed,
                newest_processed_timestamp(processed),
                generated_at,
            ),
            source_freshness_line(
                "Bridge sync state",
                sync_state_path,
                project_root,
                sync_state,
                source_timestamp(sync_state, ("last_outbound_sync", "last_inbound_sync")),
                generated_at,
            ),
            source_freshness_line(
                "Body pulse state",
                pulse_state_path,
                project_root,
                pulse_state,
                source_timestamp(pulse_state, ("last_body_pulse", "last_pulse_check")),
                generated_at,
            ),
        ]
    )
    lines.append("")
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
