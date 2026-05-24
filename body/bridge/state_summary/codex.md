# Codex Implementation Summary

Generated for orientation by Codex on 2026-05-25.

This file is a human-readable implementation ledger. It is not the runtime
source of truth; runtime state remains in local bridge state files and bridge
messages. Keep the newest items at the top.

## Latest 10 Implementations

### 1. Passive Codex Request Queue

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

### 2. One-Time Cycle Error Reporting

Fixed repeated cycle error spam. The cycle now fingerprints the active error
and writes only one outbox error for the same failure. Repeats update local
state instead of creating a new error file every 30 seconds.

Changed:

- `bridge/scripts/bridge_cycle.py`

### 3. Safe Inbound Handling For Existing Inbox Files

Adjusted inbound sync so an identical local inbox file and remote inbox file are
accepted as the same message. A real content conflict still stops the cycle.

Changed:

- `bridge/scripts/bridge_sync_inbound.py`

### 4. Outbound Rebase Tolerance For Local Inbox

Allowed local inbox files to exist during outbound rebase checks without being
treated as forbidden outbound changes. Inbox is still not staged or pushed by
outbound sync.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

Published with the first successful task result as:

```text
9b4df4c Sync RPi bridge outbound state
```

### 5. Task Request Guide

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

### 6. Runtime Log Tail And Rotation

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

### 7. Safe Pre-Push Rebase

Outbound sync now fetches and safely rebases before commit/push when local
changes are limited to bridge-owned paths. It uses no force push and refuses
disallowed worktree changes.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

### 8. Systemd Bridge Cycle

Installed and validated a one-shot bridge cycle controlled by a systemd timer.
The service runs the sequence:

1. inbound sync
2. `bridge_agent_v2.py`
3. `write_bridge_summary.py`
4. outbound sync

The timer fires every 30 seconds. There is no daemon loop inside the bridge
scripts.

### 9. Allowlisted Task Runner

Added `task_request` support to the bridge agent. Tasks run only from:

```text
/home/fiste/Noema/bridge/scripts/tasks/
```

Execution is controlled by `allowlist.json`, uses `shell=False`, enforces string
arguments, timeout, non-root execution, stdout/stderr capture, and task run
state in local `task_runs.json`.

### 10. Bridge State Summary

Added generated state summary:

```text
symnozein/body/bridge/state_summary/latest.md
```

It reports inbox/outbox counts, last processed message, error count, body state,
and bridge log tail without publishing internal state files such as
`processed_messages.json` or `event_state.json`.
