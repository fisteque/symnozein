#!/usr/bin/env python3

from __future__ import annotations

import json
import os
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Iterator

from bridge_sync_common import SyncError, ensure_inside


DEFAULT_LOCK_TTL_SECONDS = 15 * 60


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


def write_lock(lock_path: Path, runtime_root: Path, ttl_seconds: int) -> None:
    ensure_inside(lock_path, runtime_root)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    now = utc_now()
    data = {
        "pid": os.getpid(),
        "created_at": utc_iso(now),
        "expires_at": utc_iso(now + timedelta(seconds=ttl_seconds)),
    }
    tmp_path = lock_path.with_name(f".{lock_path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, runtime_root)
    tmp_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(lock_path)


def release_lock(lock_path: Path, runtime_root: Path) -> None:
    ensure_inside(lock_path, runtime_root)
    now = utc_now()
    data = {
        "pid": os.getpid(),
        "released_at": utc_iso(now),
        "expires_at": utc_iso(now),
        "status": "released",
    }
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
        raise SyncError(f"Bridge cycle lock is active until {existing.get('expires_at')}: {lock_path}")

    write_lock(lock_path, runtime_root, ttl_seconds)
    try:
        yield lock_path
    finally:
        current = read_lock(lock_path, runtime_root)
        if current and current.get("pid") == os.getpid():
            release_lock(lock_path, runtime_root)
