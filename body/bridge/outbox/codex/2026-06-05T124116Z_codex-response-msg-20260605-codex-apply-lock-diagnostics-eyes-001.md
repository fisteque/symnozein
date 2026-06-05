---
type: codex_response
created_at: 2026-06-05T12:41:16Z
sender: RPi5-bridge
target: noema
reply_to: msg-20260605-codex-apply-lock-diagnostics-eyes-001
status: done
task_class: implementation
---

# Bridge cycle lock diagnostics applied

Applied only the diagnostic part of the previous proposal. No stale-lock takeover was added.

## Changed files

- `bridge/scripts/bridge_cycle_lock.py`
- `bridge/scripts/bridge_cycle.py`

Outbound sync should mirror these into:

- `body/bridge/scripts/bridge_cycle_lock.py`
- `body/bridge/scripts/bridge_cycle.py`

## What was added

`bridge_cycle.lock.json` now records on acquire:

- `pid`
- `created_at`
- `expires_at`
- `status: active`
- `current_step: starting`
- `last_progress_at`
- `owner: rpi5-bridge-cycle`
- `host`

`bridge_cycle.py` now updates lock progress before each main cycle step:

- `inbound sync`
- `bridge agent`
- `write bridge summary`
- `outbound sync`

On release, the lock is still not deleted. It is rewritten with:

- `status: released`
- `current_step: released`
- `last_progress_at`
- `released_at`
- `expires_at` set to release time

The lock conflict error now includes:

- `state=active|expired`
- `pid`
- `pid_alive`
- `age_seconds`
- `current_step`
- `last_progress_at`
- `progress_age_seconds`
- `expires_at`
- `owner`
- `host`

The `command` field was intentionally not added.

## Behavior intentionally unchanged

- No stale-lock auto-takeover.
- No automatic active lock deletion.
- TTL unchanged.
- Timer cadence unchanged.
- Heartbeat/watchdog logic unchanged.
- Historical messages unchanged.
- Services were not restarted.

## Verification

Syntax check passed:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile bridge/scripts/bridge_cycle_lock.py bridge/scripts/bridge_cycle.py
```

Isolated `/tmp` lock lifecycle test passed:

```text
{"current_step": "released", "has_host": true, "has_owner": true, "status": "released"}
```

Isolated `/tmp` lock conflict test passed and produced the expected diagnostic shape:

```text
Bridge cycle lock is active: /tmp/.../state/bridge_cycle.lock.json; state=active, pid=..., pid_alive=True, age_seconds=..., current_step=starting, last_progress_at=..., progress_age_seconds=..., expires_at=..., owner=rpi5-bridge-cycle, host=...
```

Runtime state check:

- `state/body_state.json` reported `status: normal_operation`.
- `awake: true`.
- `heartbeat_timeout_count: 0`.

## Restart requirement

No restart was needed. The timer invokes the Python scripts fresh for each bridge cycle, so the next normal run will use the updated code. I did not restart services to avoid disturbing cadence.
