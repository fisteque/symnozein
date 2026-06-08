#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import traceback
from datetime import UTC, datetime
from pathlib import Path

from bridge_cycle_lock import DEFAULT_LOCK_TTL_SECONDS, bridge_cycle_lock, update_lock_progress
from bridge_sync_common import (
    DEFAULT_PROJECT_ROOT,
    SyncError,
    add_common_args,
    ensure_inside,
)


SCRIPT_DIR = Path(__file__).resolve().parent
AGENT_ID = "rpi5-bridge-cycle"
CYCLE_ERROR_STATE = "cycle_error_state.json"
RUNTIME_LOG_NAME = "bridge.log"
LOG_ROTATE_MAX_LINES = 8000
LOG_ROTATE_RETAIN_LINES = 3000
LOG_ARCHIVE_DIR = "archive"


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_iso(value: datetime | None = None) -> str:
    return (value or utc_now()).isoformat().replace("+00:00", "Z")


def utc_stamp() -> str:
    return utc_now().strftime("%Y%m%dT%H%M%SZ")


def utc_month() -> str:
    return utc_now().strftime("%Y-%m")


def bridge_log_path(runtime_root: Path) -> Path:
    return runtime_root / "logs" / RUNTIME_LOG_NAME


def cycle_log(runtime_root: Path, message: str, level: str = "INFO") -> None:
    line = f"[{utc_iso()}] [{level}] [cycle] {message}"
    log_path = bridge_log_path(runtime_root)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)


def rotate_runtime_log_if_needed(runtime_root: Path) -> int:
    log_path = bridge_log_path(runtime_root)
    ensure_inside(log_path, runtime_root)
    if not log_path.exists():
        return 0

    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(lines) <= LOG_ROTATE_MAX_LINES:
        return 0

    retain = lines[-LOG_ROTATE_RETAIN_LINES:]
    archived = lines[: len(lines) - len(retain)]
    archive_dir = log_path.parent / LOG_ARCHIVE_DIR / utc_month()
    archive_path = archive_dir / f"bridge-{utc_stamp()}-{len(archived)}-lines.log"
    ensure_inside(archive_path, runtime_root)
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_text("\n".join(archived) + "\n", encoding="utf-8")
    log_path.write_text("\n".join(retain) + "\n", encoding="utf-8")
    return len(archived)


def atomic_write_text(path: Path, text: str, root: Path) -> None:
    ensure_inside(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, root)
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def write_cycle_state(runtime_root: Path, state: dict[str, object]) -> None:
    path = runtime_root / "state" / "bridge_cycle_state.json"
    text = json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(path, text, runtime_root)


def cycle_error_state_path(runtime_root: Path) -> Path:
    return runtime_root / "state" / CYCLE_ERROR_STATE


def load_cycle_error_state(runtime_root: Path) -> dict[str, object]:
    path = cycle_error_state_path(runtime_root)
    ensure_inside(path, runtime_root)
    if not path.exists():
        return {"version": 1}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"version": 1}
    if not isinstance(data, dict):
        return {"version": 1}
    return data


def save_cycle_error_state(runtime_root: Path, state: dict[str, object]) -> None:
    path = cycle_error_state_path(runtime_root)
    text = json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(path, text, runtime_root)


def lock_error_field(error: str, field: str) -> str | None:
    match = re.search(rf"(?:^|[,;] )({re.escape(field)})=([^,]+)", error)
    if not match:
        return None
    value = match.group(2).strip()
    return value or None


def infer_error_step(error: str, last_step: object) -> str:
    if isinstance(last_step, str) and last_step.strip():
        return last_step
    current_step = lock_error_field(error, "current_step")
    if current_step:
        return current_step
    return "unknown"


def cycle_error_fingerprint(error: str, step: str | None) -> str:
    if error.startswith("Bridge cycle lock is active:"):
        payload_data = {
            "kind": "bridge_cycle_lock_active",
            "step": step or "unknown",
            "state": lock_error_field(error, "state"),
            "pid": lock_error_field(error, "pid"),
            "pid_alive": lock_error_field(error, "pid_alive"),
            "current_step": lock_error_field(error, "current_step"),
            "owner": lock_error_field(error, "owner"),
            "host": lock_error_field(error, "host"),
        }
    else:
        payload_data = {"step": step or "unknown", "error": error}
    payload = json.dumps(
        payload_data,
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def sanitize_filename_part(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in "._-" else "-" for ch in value.strip())
    cleaned = cleaned.strip(".-")
    return cleaned[:80] or "cycle"


def render_markdown_message(frontmatter: dict[str, object], body: str) -> str:
    import yaml

    yaml_text = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body.rstrip()}\n"


def write_cycle_error_outbox(runtime_root: Path, repo_root: Path, error: str, step: str | None) -> Path:
    outbox_dir = runtime_root / "outbox" / "messages"
    ensure_inside(outbox_dir, runtime_root)
    outbox_dir.mkdir(parents=True, exist_ok=True)
    now = utc_now()
    filename = f"{now.strftime('%Y-%m-%dT%H%M%SZ')}_rpi5_cycle-error-{sanitize_filename_part(step or 'unknown')}.md"
    path = outbox_dir / filename
    counter = 1
    while path.exists():
        path = outbox_dir / f"{path.stem}-{counter}{path.suffix}"
        counter += 1
    frontmatter = {
        "id": f"cycle-error-{now.strftime('%Y%m%d-%H%M%S')}",
        "type": "error",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": "noema",
        "status": "error",
        "severity": "error",
        "step": step or "unknown",
    }
    body = "\n".join(
        [
            "Bridge cycle skoncil chybou.",
            "",
            f"- step: `{step or 'unknown'}`",
            f"- error: `{error}`",
        ]
    )
    atomic_write_text(path, render_markdown_message(frontmatter, body), runtime_root)
    return path


def report_cycle_error_once(runtime_root: Path, repo_root: Path, error: str, step: str | None) -> Path | None:
    fingerprint = cycle_error_fingerprint(error, step)
    state = load_cycle_error_state(runtime_root)
    if state.get("active_fingerprint") == fingerprint:
        count = int(state.get("repeat_count", 1)) + 1
        state.update(
            {
                "version": 1,
                "status": "repeated",
                "active_fingerprint": fingerprint,
                "last_seen_at": utc_iso(),
                "repeat_count": count,
                "step": step or "unknown",
                "error": error,
            }
        )
        save_cycle_error_state(runtime_root, state)
        cycle_log(
            runtime_root,
            f"Cycle error already reported for step={step or 'unknown'} repeat_count={count}",
            level="WARN",
        )
        return None

    outbox_path = write_cycle_error_outbox(runtime_root, repo_root, error, step)
    state.update(
        {
            "version": 1,
            "status": "active",
            "active_fingerprint": fingerprint,
            "first_seen_at": utc_iso(),
            "last_seen_at": utc_iso(),
            "repeat_count": 1,
            "step": step or "unknown",
            "error": error,
            "outbox_path": str(outbox_path),
        }
    )
    save_cycle_error_state(runtime_root, state)
    return outbox_path


def clear_cycle_error_state(runtime_root: Path) -> None:
    state = load_cycle_error_state(runtime_root)
    if state.get("active_fingerprint"):
        state.update(
            {
                "version": 1,
                "status": "cleared",
                "cleared_at": utc_iso(),
                "active_fingerprint": None,
            }
        )
        save_cycle_error_state(runtime_root, state)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one safe bridge sync cycle.")
    add_common_args(parser)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=f"Project root containing state/body_state.json. Default: {DEFAULT_PROJECT_ROOT}",
    )
    parser.add_argument("--lock-ttl-seconds", type=int, default=DEFAULT_LOCK_TTL_SECONDS)
    parser.add_argument(
        "--commit-and-push",
        action="store_true",
        help="Pass through to bridge_sync_outbound.py. This is the only cycle parameter that enables git commit and push.",
    )
    return parser.parse_args()


def run_step(
    runtime_root: Path,
    name: str,
    args: list[str],
    *,
    env: dict[str, str] | None = None,
    log_stdout: bool = True,
) -> None:
    cycle_log(runtime_root, f"== {name} ==")
    result = subprocess.run(
        args,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    if result.stdout and log_stdout:
        cycle_log(runtime_root, result.stdout.rstrip())
    if result.stderr:
        cycle_log(runtime_root, result.stderr.rstrip(), level="ERROR")
    if result.returncode != 0:
        raise SyncError(f"Step failed ({name}) with exit code {result.returncode}")


def main() -> int:
    args = parse_args()
    runtime_root = args.runtime_root.resolve()
    repo_root = args.repo_root.resolve()
    project_root = args.project_root.resolve()

    common = [
        "--runtime-root",
        str(runtime_root),
        "--repo-root",
        str(repo_root),
        "--remote",
        args.remote,
        "--branch",
        args.branch,
    ]

    outbound = [str(SCRIPT_DIR / "bridge_sync_outbound.py"), *common]
    if args.commit_and_push:
        outbound.append("--commit-and-push")
    agent_env = os.environ.copy()
    agent_env.update(
        {
            "NOEMA_BRIDGE_ROOT": str(runtime_root),
            "NOEMA_PROJECT_ROOT": str(project_root),
            "NOEMA_BODY_ROOT": str(repo_root / "body"),
        }
    )

    state: dict[str, object] = {
        "version": 1,
        "started_at": utc_iso(),
        "finished_at": None,
        "status": "running",
        "last_step": None,
        "error": None,
        "commit_and_push": bool(args.commit_and_push),
    }

    try:
        ensure_inside(runtime_root, runtime_root)
        with bridge_cycle_lock(runtime_root, ttl_seconds=args.lock_ttl_seconds) as lock_path:
            archived_lines = rotate_runtime_log_if_needed(runtime_root)
            if archived_lines:
                cycle_log(
                    runtime_root,
                    f"Rotated runtime bridge log: archived_lines={archived_lines} retain_lines={LOG_ROTATE_RETAIN_LINES}",
                )
            cycle_log(runtime_root, f"Bridge cycle lock acquired: {lock_path}")
            write_cycle_state(runtime_root, state)
            state["last_step"] = "inbound sync"
            write_cycle_state(runtime_root, state)
            update_lock_progress(lock_path, runtime_root, "inbound sync")
            run_step(runtime_root, "inbound sync", [str(SCRIPT_DIR / "bridge_sync_inbound.py"), *common])
            state["last_step"] = "bridge agent"
            write_cycle_state(runtime_root, state)
            update_lock_progress(lock_path, runtime_root, "bridge agent")
            run_step(
                runtime_root,
                "bridge agent",
                [sys.executable, str(SCRIPT_DIR / "bridge_agent_v2.py")],
                env=agent_env,
                log_stdout=False,
            )
            state["last_step"] = "write bridge summary"
            write_cycle_state(runtime_root, state)
            update_lock_progress(lock_path, runtime_root, "write bridge summary")
            run_step(
                runtime_root,
                "write bridge summary",
                [
                    str(SCRIPT_DIR / "write_bridge_summary.py"),
                    *common,
                    "--project-root",
                    str(project_root),
                ],
            )
            state["last_step"] = "outbound sync"
            write_cycle_state(runtime_root, state)
            update_lock_progress(lock_path, runtime_root, "outbound sync")
            run_step(runtime_root, "outbound sync", outbound)
            cycle_log(runtime_root, "Bridge cycle complete.")
            if not args.commit_and_push:
                cycle_log(runtime_root, "No commit/push was performed. Use --commit-and-push to enable outbound commit and push.")
            state["status"] = "ok"
            state["finished_at"] = utc_iso()
            write_cycle_state(runtime_root, state)
            clear_cycle_error_state(runtime_root)
        return 0
    except SyncError as exc:
        error = str(exc)
        cycle_log(runtime_root, error, level="ERROR")
        cycle_log(runtime_root, traceback.format_exc().rstrip(), level="ERROR")
        state["status"] = "error"
        state["finished_at"] = utc_iso()
        state["error"] = error
        try:
            error_step = infer_error_step(error, state.get("last_step"))
            state["last_step"] = error_step
            write_cycle_state(runtime_root, state)
            outbox_path = report_cycle_error_once(
                runtime_root,
                repo_root,
                error,
                error_step,
            )
            if outbox_path is not None:
                cycle_log(runtime_root, f"Cycle error outbox written: {outbox_path}")
        except Exception as error_exc:
            cycle_log(runtime_root, f"Failed to write cycle error state/outbox: {error_exc}", level="ERROR")
        print(f"WARN: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
