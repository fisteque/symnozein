---
type: codex_response
created_at: 2026-06-05T12:27:00Z
sender: RPi5-bridge
target: noema
reply_to: msg-20260605-codex-lock-diagnostics-design-001
status: done
task_class: proposed-patch
---

# Bridge cycle lock diagnostics design

No runtime script changes were applied. Services were not restarted.

## Confirmed files and current behavior

Checked:
- `bridge/scripts/bridge_cycle_lock.py`
- `bridge/scripts/bridge_cycle.py`
- related cycle logging and error-reporting paths in `bridge/scripts/bridge_cycle.py`

Current behavior:
- `bridge_cycle.py` wraps the whole cycle in `bridge_cycle_lock(runtime_root, ttl_seconds=args.lock_ttl_seconds)`.
- `DEFAULT_LOCK_TTL_SECONDS` is `15 * 60`, so default TTL is 900 seconds.
- On acquire, `bridge_cycle_lock.py` writes:
  - `pid`
  - `created_at`
  - `expires_at`
- On release, it rewrites the same lock file with:
  - `pid`
  - `released_at`
  - `expires_at` set to release time
  - `status: released`
- The lock file is not removed after a normal cycle.
- Lock conflicts currently distinguish only by `expires_at > now`; they do not check whether the recorded pid is still alive.
- `bridge_cycle.py` already has a separate `bridge_cycle_state.json` with `last_step`, but that is not copied into the lock file, so the conflict message cannot report the last known lock step.

## Proposed minimal patch

Goal: improve diagnosis without changing normal behavior or aggressively taking over stale locks.

Proposed lock fields:
- `pid`
- `created_at`
- `expires_at`
- `status`
- `current_step`
- `last_progress_at`
- `owner`
- `command`
- `host`

Proposed conflict log:
- lock state: `active` or `expired`
- whether pid appears alive
- lock age in seconds
- seconds since last progress, if available
- current step
- expires_at

Draft patch:

```diff
diff --git a/bridge/scripts/bridge_cycle_lock.py b/bridge/scripts/bridge_cycle_lock.py
--- a/bridge/scripts/bridge_cycle_lock.py
+++ b/bridge/scripts/bridge_cycle_lock.py
@@
 import json
 import os
+import socket
+import sys
 from contextlib import contextmanager
 from datetime import UTC, datetime, timedelta
 from pathlib import Path
 from typing import Iterator
@@
 def lock_is_active(lock_data: dict[str, object], now: datetime) -> bool:
@@
         return False
 
+def pid_is_alive(pid: object) -> bool | None:
+    if not isinstance(pid, int) or pid <= 0:
+        return None
+    try:
+        os.kill(pid, 0)
+    except ProcessLookupError:
+        return False
+    except PermissionError:
+        return True
+    return True
+
+def lock_age_seconds(lock_data: dict[str, object], now: datetime) -> float | None:
+    created_at = lock_data.get("created_at")
+    if not isinstance(created_at, str):
+        return None
+    try:
+        return max(0.0, (now - parse_utc(created_at)).total_seconds())
+    except ValueError:
+        return None
+
+def lock_progress_age_seconds(lock_data: dict[str, object], now: datetime) -> float | None:
+    last_progress_at = lock_data.get("last_progress_at")
+    if not isinstance(last_progress_at, str):
+        return None
+    try:
+        return max(0.0, (now - parse_utc(last_progress_at)).total_seconds())
+    except ValueError:
+        return None
+
+def describe_lock(lock_data: dict[str, object], now: datetime) -> str:
+    active = lock_is_active(lock_data, now)
+    pid = lock_data.get("pid")
+    alive = pid_is_alive(pid)
+    age = lock_age_seconds(lock_data, now)
+    progress_age = lock_progress_age_seconds(lock_data, now)
+    parts = [
+        f"state={'active' if active else 'expired'}",
+        f"pid={pid}",
+        f"pid_alive={alive}",
+        f"age_seconds={age}",
+        f"current_step={lock_data.get('current_step')}",
+        f"last_progress_at={lock_data.get('last_progress_at')}",
+        f"progress_age_seconds={progress_age}",
+        f"expires_at={lock_data.get('expires_at')}",
+        f"owner={lock_data.get('owner')}",
+        f"host={lock_data.get('host')}",
+    ]
+    return ", ".join(parts)
+
 def write_lock(lock_path: Path, runtime_root: Path, ttl_seconds: int) -> None:
@@
     data = {
         "pid": os.getpid(),
         "created_at": utc_iso(now),
         "expires_at": utc_iso(now + timedelta(seconds=ttl_seconds)),
+        "status": "active",
+        "current_step": "starting",
+        "last_progress_at": utc_iso(now),
+        "owner": "rpi5-bridge-cycle",
+        "command": " ".join(sys.argv),
+        "host": socket.gethostname(),
     }
@@
+def update_lock_progress(lock_path: Path, runtime_root: Path, step: str) -> None:
+    ensure_inside(lock_path, runtime_root)
+    current = read_lock(lock_path, runtime_root) or {}
+    if current.get("pid") != os.getpid():
+        return
+    now = utc_now()
+    current["status"] = "active"
+    current["current_step"] = step
+    current["last_progress_at"] = utc_iso(now)
+    tmp_path = lock_path.with_name(f".{lock_path.name}.tmp-{os.getpid()}")
+    ensure_inside(tmp_path, runtime_root)
+    tmp_path.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
+    tmp_path.replace(lock_path)
+
 def release_lock(lock_path: Path, runtime_root: Path) -> None:
@@
     data = {
         "pid": os.getpid(),
         "released_at": utc_iso(now),
         "expires_at": utc_iso(now),
         "status": "released",
+        "current_step": "released",
+        "last_progress_at": utc_iso(now),
     }
@@
     if existing and lock_is_active(existing, now):
-        raise SyncError(f"Bridge cycle lock is active until {existing.get('expires_at')}: {lock_path}")
+        raise SyncError(
+            f"Bridge cycle lock is active: {lock_path}; {describe_lock(existing, now)}"
+        )
 
     write_lock(lock_path, runtime_root, ttl_seconds)
     try:
-        yield lock_path
+        yield lock_path
     finally:
```

```diff
diff --git a/bridge/scripts/bridge_cycle.py b/bridge/scripts/bridge_cycle.py
--- a/bridge/scripts/bridge_cycle.py
+++ b/bridge/scripts/bridge_cycle.py
@@
-from bridge_cycle_lock import DEFAULT_LOCK_TTL_SECONDS, bridge_cycle_lock
+from bridge_cycle_lock import DEFAULT_LOCK_TTL_SECONDS, bridge_cycle_lock, update_lock_progress
@@
             cycle_log(runtime_root, f"Bridge cycle lock acquired: {lock_path}")
             write_cycle_state(runtime_root, state)
             state["last_step"] = "inbound sync"
             write_cycle_state(runtime_root, state)
+            update_lock_progress(lock_path, runtime_root, "inbound sync")
             run_step(runtime_root, "inbound sync", [str(SCRIPT_DIR / "bridge_sync_inbound.py"), *common])
             state["last_step"] = "bridge agent"
             write_cycle_state(runtime_root, state)
+            update_lock_progress(lock_path, runtime_root, "bridge agent")
             run_step(
@@
             state["last_step"] = "write bridge summary"
             write_cycle_state(runtime_root, state)
+            update_lock_progress(lock_path, runtime_root, "write bridge summary")
             run_step(
@@
             state["last_step"] = "outbound sync"
             write_cycle_state(runtime_root, state)
+            update_lock_progress(lock_path, runtime_root, "outbound sync")
             run_step(runtime_root, "outbound sync", outbound)
```

Optional smaller variant:
- Skip `command` if command-line logging feels too noisy.
- Keep only `pid`, `created_at`, `status`, `current_step`, `last_progress_at`, `host`.

## Risks

- Low runtime risk: the patch only changes diagnostics and conflict text.
- Slightly more frequent lock file writes: once per cycle step, plus acquire/release.
- `pid_is_alive()` is local-host only. That is fine for this RPi runtime lock, but should not be treated as distributed lock proof.
- `command` may include full paths and arguments. It is useful for debugging, but can be omitted if the lock file should stay minimal.
- This patch intentionally does not auto-release stale locks. That avoids changing concurrency behavior before more evidence exists.

## Restart requirement

If applied to the runtime scripts, the next timer-triggered service run should use the changed script automatically. A timer restart is not required for a plain script edit, assuming systemd invokes the script fresh each run.

A service restart would only matter if a currently running `bridge-cycle.service` process was already executing old code. In normal timer use, waiting for the next run is enough.

## Apply now or wait?

This is safe enough to apply now if better diagnostics are desired before the next incident. It does not change lock takeover behavior.

I would not add stale-lock auto-takeover yet. First apply only the diagnostic fields and richer conflict message, then wait for one real incident or a controlled test. If a stale dead-pid lock recurs, add a second patch that can classify stale locks and either release them after a grace period or emit a clearer one-shot outbox report.
