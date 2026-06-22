# Bridge Scripts

This document describes the bridge scripts mirrored under:

```text
body/bridge/scripts/
```

Runtime source lives on the RPi under:

```text
/home/fiste/Noema/bridge/scripts/
```

Related runtime systemd units live under:

```text
/home/fiste/Noema/bridge/systemd/
```

The GitHub mirror keeps bridge-facing unit files under:

```text
body/bridge/systemd/
```

This directory is included in the outbound sync allowlist so service/timer file
updates do not need a manual commit path.

Current mirrored unit files:

- `codex-autoreply.service`
- `codex-autoreply.timer`
- `noema-body-pulse.service`
- `noema-body-pulse.timer`
- `bridge-cycle.service`
- `bridge-cycle.timer`
- `bridge-watchdog.service`
- `bridge-watchdog.timer`

The bridge is intentionally narrow: it moves messages between the local runtime,
the GitHub tape, and local state files. Body heartbeat/watchdog is separate.

Safety boundaries are summarized in `body/bridge/docs/safety_model.md`.
The public summary contract is in `body/bridge/docs/latest_contract.md`.

## Main Cycle

### `bridge_cycle.py`

Runs one complete bridge cycle:

```text
inbound sync -> bridge agent -> write bridge summary -> outbound sync
```

It is the systemd `bridge-cycle.service` entrypoint. The service is oneshot and
is normally triggered by `bridge-cycle.timer`.

Important behavior:

- acquires `bridge/state/bridge_cycle.lock.json`;
- writes `bridge/state/bridge_cycle_state.json`;
- updates lock progress before each step;
- rotates the runtime bridge log;
- deduplicates repeated cycle errors through `cycle_error_state.json`;
- writes cycle error messages to outbox when needed.

It only commits/pushes when called with:

```text
--commit-and-push
```

### `bridge_cycle_lock.py`

Owns the cycle lock helper used by `bridge_cycle.py`.

Important behavior:

- creates an active lock with PID, owner, host, current step, and expiry;
- updates `current_step` and `last_progress_at`;
- releases the lock at the end of the cycle;
- may reclaim a stale active local bridge-cycle lock only when the PID is dead;
- never overwrites a live PID lock.

## Sync

### `bridge_sync_inbound.py`

Fetches GitHub `body/bridge/inbox/messages/` into the local repo mirror and
hydrates the runtime inbox:

```text
symnozein/body/bridge/inbox/messages/ -> bridge/inbox/messages/
```

Important behavior:

- mirrors inbound deletions from GitHub into the repo mirror;
- copies only new/unprocessed Markdown messages into the runtime inbox;
- uses `bridge/state/processed_messages.json` to avoid replaying messages that
  remain on the GitHub tape;
- treats `pending` as retryable and terminal statuses as already handled.

Inbound is copy-only toward runtime. It does not publish anything.

### `bridge_sync_outbound.py`

Mirrors outbound runtime state to the GitHub tape and optionally commits/pushes.

Important behavior:

- publishes runtime outbox messages from `bridge/outbox/messages/` to
  `body/bridge/outbox/messages/`;
- after successful push, archives published runtime outbox messages under
  `bridge/outbox/published/YYYY-MM/`;
- mirrors bridge scripts and state summary;
- mirrors bridge-facing systemd unit files under `body/bridge/systemd/`;
- rejects forbidden paths and Python bytecode cache files;
- safely rebases before push without force-push;
- stashes allowed outbound paths and local-only inbox paths during pre-push
  rebase, so GitHub-side inbox deletions do not block sync;
- does not push runtime state JSON, locks, logs, or inbox mirror changes.

Use `--dry-run` to inspect without writing. Use `--commit-and-push` for the
normal bridge cycle publish path.

### `bridge_sync_common.py`

Shared constants and helpers for sync scripts.

Includes:

- default roots and remote/branch names;
- bridge repo path constants;
- git command wrapper;
- path safety helpers;
- status parsing helpers.

It is not intended as a standalone entrypoint.

### `mirror_scripts_to_repo.py`

Copies local runtime scripts into the repo mirror:

```text
bridge/scripts/ -> symnozein/body/bridge/scripts/
```

It does not delete repo files. Outbound sync uses this helper.

## Agent And Messages

### `bridge_agent_v2.py`

Processes runtime inbox messages from:

```text
bridge/inbox/messages/
```

Important behavior:

- validates Markdown frontmatter;
- checks target against `rpi5-bridge-agent` / `rpi5-bridge`;
- records message state in `bridge/state/processed_messages.json`;
- writes replies or task results to runtime outbox;
- turns `codex_request` into a local Codex queue item under
  `/home/fiste/Noema/codex/inbox/`;
- archives processed runtime inbox files under
  `bridge/inbox/processed/YYYY-MM/`;
- archives invalid runtime inbox files with an `invalid-` prefix after recording
  an error.

`pending_codex` is terminal for the bridge agent after the request is written to
the local Codex queue.

### `codex_inbox_reader.py`

Reads local Codex request files from:

```text
/home/fiste/Noema/codex/inbox/
```

This reader does not call Codex automatically. It can emit a dry-run JSON report
and can write manual stub responses with `--write-stub`. Automatic Codex
execution is handled separately by `codex_autoreply_worker.py`.

Stub responses go to:

```text
bridge/outbox/messages/
```

Reader state is runtime-local:

```text
bridge/state/codex_reader_state.json
```

### `codex_autoreply_worker.py`

Processes exactly one local Codex inbox request per run:

```text
/home/fiste/Noema/codex/inbox/
```

It supports:

- dry-run inspection by default;
- `--write-stub` to write one `codex_response` stub into
  `bridge/outbox/messages/`;
- `--run-codex` to call `codex exec` in read-only, non-interactive mode and
  write the final Codex answer into `bridge/outbox/messages/`;
- archival of the source request into
  `/home/fiste/Noema/codex/processed/YYYY-MM/` only after the outbox response is
  written successfully.

Worker state is runtime-local:

```text
bridge/state/codex_autoreply_state.json
```

It does not commit, push, start services, or process more than one request per
run. Requests classified as `needs_human` require explicit
`--allow-needs-human` before `--run-codex` will execute.

The safety classifier treats real requests for risky actions such as commits,
pushes, installs, deletes, restarts, and runtime logic changes as
`needs_human`. Explicit negative safety instructions such as "do not commit" or
"does not require edits, commits, pushes..." are filtered before that risky-term
check, so read-only orientation requests are not blocked just because they state
their safety boundaries.

For timer use it also supports `--quiet-empty`, where an empty Codex inbox exits
successfully with an idle JSON result.

In `--run-codex` mode the worker prompt permits read-only inspection of local
files under `/home/fiste/Noema` when needed to answer a request. It still
forbids edits, commits, pushes, deletes, installs, service restarts, and runtime
state changes; the wrapper remains the only writer to the bridge outbox and
Codex processed archive.

## Summary And Watchdog

### `write_bridge_summary.py`

Writes the public bridge summary:

```text
body/bridge/state_summary/latest.md
```

It renders stable public sections for body heartbeat, body health, bridge sync,
queues, pulse, and source freshness. The summary is derived from selected local
state files such as `state/body_state.json`, `state/body_health.json`,
`bridge/state/processed_messages.json`, `bridge/state/bridge_sync_state.json`,
and `bridge/state/body_pulse_state.json`.

`latest.md` is intentionally a compact public status panel. It must not become a
log dump, raw runtime export, or historical archive; see
`body/bridge/docs/latest_contract.md`.

The full runtime log remains local and is not included in `latest.md`. Raw
runtime JSON, locks, queue archives, and log tails are not published.

### `bridge_watchdog.py`

Local observer for bridge health. It watches the bridge as a cycle path, not
body liveness:

```text
bridge-cycle.timer -> bridge_cycle.py -> inbound sync -> agent -> summary -> outbound sync
```

Important behavior:

- reads `bridge_cycle_state.json`, `bridge_cycle.lock.json`, and
  `cycle_error_state.json`;
- may read a small safe subset of systemd status fields;
- detects missing cycles, stale summaries, stuck running cycles, stale locks,
  stalled steps, and active cycle errors;
- writes primary local incident records under `bridge/incidents/YYYY-MM/`;
- may write a runtime outbox message as a best-effort publish attempt when
  outbox publication is enabled;
- does not restart services, delete locks, reclaim locks, change timers, or do
  git housekeeping.

Current installed first-phase service mode is:

```text
bridge_watchdog.py --no-outbox --json
```

In this mode the service writes only local state and incident records. It does
not write `bridge/outbox/messages/`.

## Systemd Units

### `codex-autoreply.service`

Runs the Codex autoreply worker as a oneshot service:

```text
/usr/bin/python3 /home/fiste/Noema/bridge/scripts/codex_autoreply_worker.py --run-codex --quiet-empty --json
```

The installed command intentionally does not include `--allow-needs-human`, so
riskier requests remain in the Codex inbox for manual review.

Writable paths are limited to:

- `/home/fiste/Noema/bridge/state`
- `/home/fiste/Noema/bridge/outbox/messages`
- `/home/fiste/Noema/codex/inbox`
- `/home/fiste/Noema/codex/processed`
- `/home/fiste/.codex`

### `codex-autoreply.timer`

Triggers `codex-autoreply.service` every 60 seconds.

The timer is prepared but should be manually tested before enable/start.

### `noema-body-pulse.service`

Runs a scheduled public body pulse by refreshing
`body/bridge/state_summary/latest.md`, committing exactly that file, and pushing
it to the GitHub tape with:

```text
Pulse body state to tape
```

Before refreshing `latest.md`, a real pulse records local
`bridge/state/body_pulse_state.json` fields showing the current pulse is
running. After a successful push it records the resulting pulse commit hash.
Dry-run mode does not update persistent pulse state.

It does not mirror runtime logs, locks, raw `state/body_health.json`, outbox
messages, or unrelated dirty paths.

### `noema-body-pulse.timer`

Triggers `noema-body-pulse.service` six times daily in `Europe/Prague`:

```text
00:00, 04:00, 08:00, 12:00, 16:00, 20:00
```

### `bridge-cycle.service`

Runs one bridge cycle as a oneshot service:

```text
/usr/bin/python3 /home/fiste/Noema/bridge/scripts/bridge_cycle.py --commit-and-push
```

The installed service uses `TimeoutStartSec=90` and writes within
`/home/fiste/Noema` because a full cycle touches runtime queues, local state,
the repo mirror, and Git metadata.

### `bridge-cycle.timer`

Triggers `bridge-cycle.service` every 30 seconds.

This is the main bridge cadence. It is separate from the body heartbeat/watchdog
services and separate from the bridge watchdog timer.

### `bridge-watchdog.service`

Runs the bridge watchdog as a oneshot observer. The installed service uses a
narrow writable scope:

- `/home/fiste/Noema/bridge/state`
- `/home/fiste/Noema/bridge/incidents`

### `bridge-watchdog.timer`

Triggers `bridge-watchdog.service` every 60 seconds.

The watchdog timer is separate from `bridge-cycle.timer` and does not change
bridge cycle cadence.

## Utility Scripts

### `git_askpass.py`

Small helper for git authentication when `GITHUB_USER` and `GITHUB_TOKEN` are
available in the environment.

It is used by outbound push logic through `GIT_ASKPASS`.

### `sync_body_without_bridge.py`

Fetches and restores `body/` content except `body/bridge/`.

This is a narrow maintenance helper, not part of the normal bridge cycle.

### `sync_symnozein_without_bridge.py`

Fetches and restores repo content except `body/bridge/`.

This is a narrow maintenance helper, not part of the normal bridge cycle.

## Task Scripts

Task scripts live under:

```text
bridge/scripts/tasks/
```

They are invoked only through `task_request` messages and the allowlist:

```text
bridge/scripts/tasks/allowlist.json
```

Current allowlisted tasks:

- `example_task`
- `mirror_scripts_to_repo`
- `sync_body_without_bridge`
- `sync_symnozein_without_bridge`

Task execution is constrained by the bridge agent: no shell invocation, explicit
string arguments, timeout, stdout/stderr capture, and local task run state.

## Legacy Scripts

Legacy scripts under:

```text
bridge/scripts/legacy/
```

are retained for history and reference. They are not the current bridge cycle
path.
