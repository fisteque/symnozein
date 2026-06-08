#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import socket
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Iterator

from bridge_sync_common import SyncError, ensure_inside


DEFAULT_LOCK_TTL_SECONDS = 15 * 60
LOCK_OWNER = "rpi5-bridge-cycle"


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_iso(value: datetime | None = None) -> str:
    return (value or utc_now()).isoformat().replace("+00:00", "Z")


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def read_lock(lock_path: Path, runtime_root: Path) -> dict[str, object] | None:
    ensure_inside(lock_path, runtime_root)
    if not lock_path.exists():
        return None
    with lock_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SyncError(f"Invalid lock file content: {lock_path}")
    return data


def lock_is_active(lock_data: dict[str, object], now: datetime) -> bool:
    expires_at = lock_data.get("expires_at")
    if not isinstance(expires_at, str):
        return False
    try:
        return parse_utc(expires_at) > now
    except ValueError:
        return False


def pid_is_alive(pid: object) -> bool | None:
    if not isinstance(pid, int) or pid <= 0:
        return None
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def lock_age_seconds(lock_data: dict[str, object], now: datetime) -> float | None:
    created_at = lock_data.get("created_at")
    if not isinstance(created_at, str):
        return None
    try:
        return max(0.0, (now - parse_utc(created_at)).total_seconds())
    except ValueError:
        return None


def lock_progress_age_seconds(lock_data: dict[str, object], now: datetime) -> float | None:
    last_progress_at = lock_data.get("last_progress_at")
    if not isinstance(last_progress_at, str):
        return None
    try:
        return max(0.0, (now - parse_utc(last_progress_at)).total_seconds())
    except ValueError:
        return None


def describe_lock(lock_data: dict[str, object], now: datetime) -> str:
    active = lock_is_active(lock_data, now)
    return ", ".join(
        [
            f"state={'active' if active else 'expired'}",
            f"pid={lock_data.get('pid')}",
            f"pid_alive={pid_is_alive(lock_data.get('pid'))}",
            f"age_seconds={lock_age_seconds(lock_data, now)}",
            f"current_step={lock_data.get('current_step')}",
            f"last_progress_at={lock_data.get('last_progress_at')}",
            f"progress_age_seconds={lock_progress_age_seconds(lock_data, now)}",
            f"expires_at={lock_data.get('expires_at')}",
            f"owner={lock_data.get('owner')}",
            f"host={lock_data.get('host')}",
        ]
    )


def lock_is_reclaimable(lock_data: dict[str, object], now: datetime) -> bool:
    return (
        lock_is_active(lock_data, now)
        and lock_data.get("status") == "active"
        and lock_data.get("owner") == LOCK_OWNER
        and lock_data.get("host") == socket.gethostname()
        and pid_is_alive(lock_data.get("pid")) is False
    )


def write_lock(lock_path: Path, runtime_root: Path, ttl_seconds: int) -> None:
    ensure_inside(lock_path, runtime_root)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    now = utc_now()
    data = {
        "pid": os.getpid(),
        "created_at": utc_iso(now),
        "expires_at": utc_iso(now + timedelta(seconds=ttl_seconds)),
        "status": "active",
        "current_step": "starting",
        "last_progress_at": utc_iso(now),
        "owner": LOCK_OWNER,
        "host": socket.gethostname(),
    }
    tmp_path = lock_path.with_name(f".{lock_path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, runtime_root)
    tmp_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(lock_path)


def update_lock_progress(lock_path: Path, runtime_root: Path, step: str) -> None:
    ensure_inside(lock_path, runtime_root)
    current = read_lock(lock_path, runtime_root) or {}
    if current.get("pid") != os.getpid():
        return
    current["status"] = "active"
    current["current_step"] = step
    current["last_progress_at"] = utc_iso()
    tmp_path = lock_path.with_name(f".{lock_path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, runtime_root)
    tmp_path.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(lock_path)


def release_lock(lock_path: Path, runtime_root: Path) -> None:
    ensure_inside(lock_path, runtime_root)
    now = utc_now()
    data = read_lock(lock_path, runtime_root) or {}
    data["pid"] = os.getpid()
    data.setdefault("created_at", utc_iso(now))
    data.setdefault("owner", LOCK_OWNER)
    data.setdefault("host", socket.gethostname())
    data["released_at"] = utc_iso(now)
    data["expires_at"] = utc_iso(now)
    data["status"] = "released"
    data["current_step"] = "released"
    data["last_progress_at"] = utc_iso(now)
    tmp_path = lock_path.with_name(f".{lock_path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, runtime_root)
    tmp_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(lock_path)


@contextmanager
def bridge_cycle_lock(
    runtime_root: Path,
    *,
    ttl_seconds: int = DEFAULT_LOCK_TTL_SECONDS,
) -> Iterator[Path]:
    lock_path = runtime_root / "state" / "bridge_cycle.lock.json"
    existing = read_lock(lock_path, runtime_root)
    now = utc_now()
    if existing and lock_is_active(existing, now):
        if not lock_is_reclaimable(existing, now):
            raise SyncError(f"Bridge cycle lock is active: {lock_path}; {describe_lock(existing, now)}")

    write_lock(lock_path, runtime_root, ttl_seconds)
    try:
        yield lock_path
    finally:
        current = read_lock(lock_path, runtime_root)
        if current and current.get("pid") == os.getpid():
            release_lock(lock_path, runtime_root)
