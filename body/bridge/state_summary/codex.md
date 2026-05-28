# Codex Implementation Summary

Generated for orientation by Codex on 2026-05-25.

This file is a human-readable implementation ledger. It is not the runtime
source of truth; runtime state remains in local bridge state files and bridge
messages. Keep the newest items at the top.

## Latest Implementations

### 1. Known Bridge Limits Anchor

Added an operational anchor for known bridge limits:

```text
body/bridge/state_summary/known_limits.md
```

Updated the task request guide to link that anchor before proposing new tasks or
input layers:

```text
body/bridge/scripts/tasks/TASK_REQUESTS.md
```

Purpose: separate verified state, proposals, the user's current safety/proxy
role, transport gaps, and dead-end assumptions before future bridge work.

Verified: the files exist in the repo mirror under `symnozein/body/bridge/`,
the task guide link matches the body-relative path used by bridge docs, and no
runtime task was needed or started.

### 2. Body State Atomic Writes And Bridge Cycle Recovery

Fixed a race where `state/body_state.json` could be observed as empty while it
was being rewritten by heartbeat/watchdog. The public bridge summary now also
tolerates a transient invalid read so a temporary body-state read problem does
not fail the whole bridge cycle.

Changed:

- `core/hb/heartbeat.py`
- `core/watchdog/state_watchdog.py`
- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

Operational work:

- stopped the bridge cycle timer while debugging;
- synced `symnozein` to clear non-bridge dirty index files that blocked
  outbound sync;
- restarted `noema-heartbeat.service` and `noema-watchdog.service` so they use
  atomic writes;
- ran a one-shot bridge cycle successfully and pushed pending outbox backlog,
  including the missing task result for `msg-20260527-task-sync-body-001`;
- restarted `bridge-cycle.timer` and verified repeated clean timer cycles.

Verified:

- `body_state.json` remains valid JSON after service restart;
- `write_bridge_summary.py` no longer crashes on an empty temporary
  `body_state.json`;
- latest bridge cycle state is `status: ok`, `error: null`.

Published as:

```text
46dc635 Sync RPi bridge outbound state
```

### 3. Passive Codex Request Queue

Added a passive `codex_request` path. Noema can send a request to the bridge
inbox, and the bridge agent creates a pending Codex item in:

```text
/home/fiste/Noema/symnozein/body/bridge/outbox/codex/
```

The agent does not call Codex, does not call an API, and does not execute a
task. Codex responses are written later by Codex with `author: Codex`.

Changed:

- `bridge/scripts/bridge_agent_v2.py`
- `bridge/scripts/bridge_sync_common.py`
- `bridge/scripts/bridge_sync_outbound.py`
- `bridge/scripts/tasks/TASK_REQUESTS.md`

Verified in `/tmp`: a `codex_needed` file was created with
`status: pending_codex` and no task execution.

Published as:

```text
e99d8e7 Sync RPi bridge outbound state
```

### 4. One-Time Cycle Error Reporting

Fixed repeated cycle error spam. The cycle now fingerprints the active error
and writes only one outbox error for the same failure. Repeats update local
state instead of creating a new error file every 30 seconds.

Changed:

- `bridge/scripts/bridge_cycle.py`

### 5. Safe Inbound Handling For Existing Inbox Files

Adjusted inbound sync so an identical local inbox file and remote inbox file are
accepted as the same message. A real content conflict still stops the cycle.

Changed:

- `bridge/scripts/bridge_sync_inbound.py`

### 6. Outbound Rebase Tolerance For Local Inbox

Allowed local inbox files to exist during outbound rebase checks without being
treated as forbidden outbound changes. Inbox is still not staged or pushed by
outbound sync.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

Published with the first successful task result as:

```text
9b4df4c Sync RPi bridge outbound state
```

### 7. Task Request Guide

Added a task invocation guide beside the allowlist and wrappers:

```text
bridge/scripts/tasks/TASK_REQUESTS.md
```

It documents `task_request` format, allowlist rules, environment variables,
audit outputs, wrapper shape, and forbidden patterns.

Published as:

```text
5036923 Sync RPi bridge outbound state
```

### 8. Runtime Log Tail And Rotation

Stopped publishing the full bridge log to GitHub. Outbound sync now publishes:

```text
symnozein/body/bridge/logs/bridge_tail.log
```

Runtime `bridge/logs/bridge.log` rotates after 5000 lines, retaining 3000 lines.
Archives are stored under:

```text
bridge/logs/archive/YYYY-MM/
```

Published across:

```text
72740cc Sync RPi bridge outbound state
aade471 Sync RPi bridge outbound state
```

### 9. Safe Pre-Push Rebase

Outbound sync now fetches and safely rebases before commit/push when local
changes are limited to bridge-owned paths. It uses no force push and refuses
disallowed worktree changes.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

### 10. Systemd Bridge Cycle

Installed and validated a one-shot bridge cycle controlled by a systemd timer.
The service runs the sequence:

1. inbound sync
2. `bridge_agent_v2.py`
3. `write_bridge_summary.py`
4. outbound sync

The timer fires every 30 seconds. There is no daemon loop inside the bridge
scripts.

### 11. Allowlisted Task Runner

Added `task_request` support to the bridge agent. Tasks run only from:

```text
/home/fiste/Noema/bridge/scripts/tasks/
```

Execution is controlled by `allowlist.json`, uses `shell=False`, enforces string
arguments, timeout, non-root execution, stdout/stderr capture, and task run
state in local `task_runs.json`.
