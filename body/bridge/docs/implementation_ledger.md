# Codex Implementation Summary

Generated for orientation by Codex on 2026-05-25.

This file is a human-readable implementation ledger. It is not the runtime
source of truth; runtime state remains in local bridge state files and bridge
messages. Keep the newest items at the top.

## Latest Implementations

### Codex Autoreply Read-Only Commit/Push Context

Adjusted `codex_autoreply_worker.py` classification so read-only questions about
commit or push state do not get blocked as write-risk requests.

The worker still blocks actual commit/push requests and other runtime-changing
instructions. It now filters narrow evidence-gathering phrases such as
"last commit", "commit hash", "read-only ... push", and "nebylo co pushnout"
before scanning for risky terms.

This fixed a pending pulse-state check request that asked for the last pulse
commit and whether anything needed pushing. After the change, the request
classified as `stub_written`, `codex-autoreply.service` ran `codex exec`, the
request was archived under `codex/processed/YYYY-MM/`, and the response was
published through the normal bridge outbox path.

### Current Pulse State Before Summary Refresh

Adjusted `body_pulse_to_tape.py` so a real pulse records local
`current_pulse_status: running` and `current_pulse_started_at` before
`write_bridge_summary.py` refreshes `latest.md`.

This lets the pulse commit's own public `latest.md` show that the current pulse
is in progress, instead of only showing the previous completed pulse from
`body_pulse_state.json`. After a successful push, the script records
`last_body_pulse` and `last_pulse_commit`, then clears the current-pulse fields.

The pulse still uses a one-commit model: the current commit hash cannot be
included in the same `latest.md` that creates that commit, so it appears in the
next summary. Dry-run mode does not update persistent pulse state.

### Codex Autoreply Safety-Negation Filter

Adjusted `codex_autoreply_worker.py` classification so explicit safety
prohibitions do not trigger `needs_human` by themselves.

The worker still treats actual requests for risky actions such as commits,
pushes, installs, deletes, restarts, and runtime logic changes as
`needs_human`. It now filters negated safety-boundary lines such as "do not
commit" and "does not require edits, commits, pushes..." before scanning for
risky terms.

This fixed a false positive where a read-only self-check request stayed in
`codex/inbox/` because it listed forbidden actions as things not to do. After
the change, the request classified as `stub_written`, was processed by
`codex-autoreply.service`, archived under `codex/processed/YYYY-MM/`, and the
response was published to the main outbox tape.

### Structured Latest Summary And Source Freshness

Restructured `body/bridge/state_summary/latest.md` into stable public sections:

```text
Bridge State Summary
Body Heartbeat
Body Health
Bridge Sync
Queues
Pulse
Source Freshness
```

The summary now reads local-only sync and pulse state:

```text
bridge/state/bridge_sync_state.json
bridge/state/body_pulse_state.json
```

Inbound and outbound sync scripts update `bridge_sync_state.json` outside dry-run
mode. `body_pulse_to_tape.py` records pulse status and the last successful pulse
commit in `body_pulse_state.json`; dry-run does not update this state.

`Source Freshness` shows compact public freshness diagnostics for the local
source files used to build `latest.md`, without publishing raw runtime JSON,
locks, logs, queue archives, or log tails.

`Next scheduled pulse` uses `noema-body-pulse.timer` when systemd is reachable
and falls back to the fixed six-times-daily Europe/Prague pulse schedule when a
manual run cannot access the systemd bus.

Follow-up diagnosis found a second systemd edge case: `systemctl show` can
return successfully with an empty `NextElapseUSecRealtime=` value. The summary
writer now treats that empty value the same as a failed systemd lookup and uses
the fixed pulse schedule fallback instead of publishing `(unknown)`.

Seeded local-only `bridge/state/body_pulse_state.json` from the latest known
`Pulse body state to tape` Git commit so `latest.md` immediately shows the last
body pulse. The seed state is not tracked or mirrored.

### Bridge Systemd Outbound Allowlist

Added `body/bridge/systemd/` to the narrow outbound sync allowlist in
`bridge_sync_outbound.py`.

This lets bridge-facing service and timer file updates publish through the
normal bridge outbound path, alongside scripts, instructions, docs, state
summary, and outbox messages. The allowlist still does not include whole
`body/`, runtime state JSON, locks, logs, or local inbox/processed queues.

Runtime and mirrored copies of `bridge_sync_outbound.py` were kept identical.

### Body Pulse To Tape

Added a scheduled body pulse publisher for the public bridge summary.

Runtime files:

```text
bridge/scripts/body_pulse_to_tape.py
bridge/systemd/noema-body-pulse.service
bridge/systemd/noema-body-pulse.timer
```

The service refreshes `body/bridge/state_summary/latest.md`, verifies there are
no unrelated dirty repo paths, stages exactly that one file, commits with
`Pulse body state to tape`, and pushes to `origin/main`. It uses the existing
bridge cycle lock so it does not run concurrently with a normal bridge cycle.

The timer schedule is six times daily in `Europe/Prague`:

```text
00:00, 04:00, 08:00, 12:00, 16:00, 20:00
```

Safety boundaries:

- raw `state/body_health.json` remains local and is not pushed;
- runtime logs, locks, outbox queues, and unrelated dirty paths are not staged;
- heartbeat, watchdog, Codex autoreply, and bridge cycle cadence are unchanged.

### Body Health In Latest Summary

Changed the public bridge summary to use local
`/home/fiste/Noema/state/body_health.json` as an input only.

`latest.md` now includes a short `Body Health` section with the last health
snapshot timestamp, CPU temperature, load average, RAM/swap/root disk usage, and
selected timer states. The full `body_health.json` remains local runtime state
and is not mirrored to the repository.

Removed the `Bridge Log Tail` section from `latest.md`, so summary generation no
longer reads and filters `bridge/logs/bridge.log` on every bridge cycle.

The `--log-lines` option remains accepted as a compatibility no-op.

### Body Health Runtime Monitor

Added a separate local body health monitor instead of expanding
`core/watchdog/state_watchdog.py`.

Runtime files:

```text
core/body_health/body_health.py
core/body_health/systemd/noema-body-health.service
core/body_health/systemd/noema-body-health.timer
state/body_health.json
```

The monitor writes an atomic JSON snapshot every 10 minutes with hostname,
uptime, load average, memory, swap, root disk usage, CPU temperature when
available, and a safe allowlist of Noema/bridge/Codex systemd unit states.

Installed and enabled:

```text
noema-body-health.service
noema-body-health.timer
```

Safety boundaries:

- no changes to heartbeat or body watchdog behavior;
- no changes to bridge cycle, bridge watchdog, or Codex autoreply timers;
- no publication into `latest.md` in this first phase;
- writes are limited to `/home/fiste/Noema/state/body_health.json`.

Verified by `py_compile`, dry-run JSON, real snapshot write, `systemd-analyze
verify`, manual service start, and timer enable/start. The first timer-triggered
snapshot updated `generated_at` and captured 10 allowlisted unit states.

### Codex Autoreply End-To-End Read Test

Verified the automatic Codex inbox to main outbox path after enabling read-only
local file inspection.

Observed flow:

```text
codex/processed/2026-06/2026-06-13T165822Z_codex-request-codex-request-20260613-check-agents-md-autoreply-003.md
bridge/outbox/published/2026-06/2026-06-13T165831Z_codex-autoreply-codex-request-20260613-165822-codex-request-20260613-check-agents-md-autoreply-0.md
body/bridge/outbox/messages/2026-06-13T165831Z_codex-autoreply-codex-request-20260613-165822-codex-request-20260613-check-agents-md-autoreply-0.md
```

The request asked Codex to read
`/home/fiste/Noema/symnozein/body/docs/AGENTS.md` and summarize it. The
automatic response confirmed the file exists, identified its purpose as a short
agent orientation document, listed the mirror/runtime/Codex queue boundaries and
bridge safety anchors, and judged it suitable as a concise agent entry sheet.

This confirmed:

- bridge agent delivered the `codex_request` into the local Codex inbox;
- `codex-autoreply.timer` ran the worker automatically;
- `codex exec` used read-only local inspection successfully;
- the wrapper wrote one `codex_response` into runtime outbox;
- the source request was archived into `codex/processed/YYYY-MM/`;
- outbound sync published the response to the GH main outbox tape.

### Codex Autoreply Read-Only Inspection

Relaxed the autoreply Codex prompt so automatic replies can inspect local files
read-only under `/home/fiste/Noema` when that is necessary to answer a request.

The worker still forbids edits, commits, pushes, deletes, installs, service
restarts, and runtime state changes. The systemd service remains unchanged:
`codex exec` still runs with `approval_policy="never"` and `--sandbox
read-only`, while the Python wrapper remains the only component that writes the
final response into `bridge/outbox/messages/` and archives the source request.

### Codex Autoreply Timer Preparation

Prepared optional systemd automation for the Codex autoreply worker:

```text
bridge/systemd/codex-autoreply.service
bridge/systemd/codex-autoreply.timer
```

The service is a oneshot wrapper around:

```text
/usr/bin/python3 /home/fiste/Noema/bridge/scripts/codex_autoreply_worker.py --run-codex --quiet-empty --json
```

The timer cadence is 60 seconds. The unit files are mirrored under:

```text
body/bridge/systemd/
```

Safety choices:

- empty Codex inbox returns `idle` with exit code 0 via `--quiet-empty`;
- `--allow-needs-human` is not enabled in the service, so risky requests remain
  pending for manual review;
- writable paths are limited to Codex inbox/processed, bridge outbox/messages,
  bridge state, and Codex CLI state under `/home/fiste/.codex`;
- no service was installed or enabled in this step.

Verified by `py_compile`, `codex_autoreply_worker.py --run-codex --quiet-empty
--json` on an empty inbox, `systemd-analyze verify`, and runtime/mirror file
comparison.

### Codex Autoreply Worker Stub Phase

Added a narrow local worker:

```text
bridge/scripts/codex_autoreply_worker.py
```

The worker is the first safe step toward processing a filled Codex inbox without
requiring an interactive Codex session. It processes exactly one request per run
from:

```text
/home/fiste/Noema/codex/inbox/
```

First phase behavior:

- dry-run by default;
- `--write-stub` writes one `codex_response` Markdown file to
  `bridge/outbox/messages/`;
- `--run-codex` calls `codex exec` in read-only, non-interactive mode and writes
  the final Codex answer to `bridge/outbox/messages/`;
- archives the source request to `/home/fiste/Noema/codex/processed/YYYY-MM/`
  only after the outbox write succeeds;
- records runtime-local state in `bridge/state/codex_autoreply_state.json`;
- does not commit, push, restart services, or process multiple requests in one
  run.

Safety boundary for model execution:

- `codex exec` runs with `--sandbox read-only` and `approval_policy="never"`;
- the prompt explicitly forbids file edits, commands, commits, pushes, deletes,
  installs, service restarts, and runtime state changes;
- requests classified as `needs_human` require explicit `--allow-needs-human`;
- if Codex execution fails, times out, produces no output, or produces an
  oversized response, the source request remains in the inbox and no archive is
  written.

This keeps automatic Codex response wiring auditable while avoiding a new broad
agent or hidden runtime autonomy.

### Bridge Documentation And Systemd Mirror Cleanup

Updated the bridge mirror and documentation after the body docs cleanup.

Mirrored all current bridge systemd units under:

```text
body/bridge/systemd/
```

Current mirrored units:

- `bridge-cycle.service`
- `bridge-cycle.timer`
- `bridge-watchdog.service`
- `bridge-watchdog.timer`

Also moved root/body legacy orientation files into `body/docs/` and
`body/docs/legacy/`, then removed the obsolete `body/shared/` tree from the
repository by explicit human/Codex commits rather than automatic bridge
deletion.

Outbound sync was tightened so it checks for disallowed worktree changes before
staging allowed paths, preventing half-staged states when a manual move includes
a delete outside the outbound whitelist. It also now pushes existing local
commits that are already ahead of `origin/main` even when the only new staged
runtime change is `state_summary/latest.md`.

Verified by:

- `systemd-analyze verify` for all bridge systemd unit files
- runtime and mirror `bridge/systemd/` tree comparison
- `py_compile` for updated outbound sync
- bridge cycle returning to `status: ok`
- `body/shared` absent from both `HEAD` and `origin/main`

### Bridge Watchdog Systemd Activation

Installed and enabled the bridge watchdog systemd units:

```text
bridge-watchdog.service
bridge-watchdog.timer
```

First phase runs the watchdog as a 60 second oneshot observer:

```text
/usr/bin/python3 /home/fiste/Noema/bridge/scripts/bridge_watchdog.py --no-outbox --json
```

The service write scope is intentionally narrow:

- `bridge/state/`
- `bridge/incidents/`

`bridge/outbox/messages/` is not writable in this phase because `--no-outbox`
is active and incident publication is intentionally disabled for the first
runtime deployment.

Activation sequence:

- installed units into `/etc/systemd/system/`
- ran `systemctl daemon-reload`
- manually started `bridge-watchdog.service`
- verified clean oneshot exit
- enabled and started `bridge-watchdog.timer`
- verified one automatic timer run

Observed result:

- timer active with 60 second cadence
- service exits with `status=0/SUCCESS`
- `bridge_watchdog_state.json` recorded `last_incident_count=0`
- no new local incident was created
- bridge latest summary continued updating and showed no bridge error

### Outbound Rebase With Local-Only Inbox Deletions

Fixed outbound sync after GitHub-side inbox cleanup. When remote inbox files are
deleted, inbound sync mirrors those deletions locally under:

```text
body/bridge/inbox/messages/
```

Those paths are local-only for outbound publish, but they still made the working
tree dirty and blocked safe pre-push rebase.

`bridge_sync_outbound.py` now includes `LOCAL_ONLY_REPO_PATHS` in the temporary
pre-rebase stash. This lets rebase proceed while preserving the rule that
inbound mirror changes are not pushed as outbound changes.

Verified by:

- temp git reproduction of local delete + remote delete
- `py_compile`
- real outbound sync from `behind 14`
- follow-up outbound sync without rebase failure

Published as:

```text
1de76e3 Sync RPi bridge outbound state
```

### Bridge Watchdog V1

Added a local bridge watchdog observer:

```text
bridge/scripts/bridge_watchdog.py
```

It checks the bridge as a cycle path, not body liveness:

```text
bridge-cycle.timer -> bridge_cycle.py -> inbound sync -> agent -> summary -> outbound sync
```

The watchdog reads local bridge state:

- `bridge/state/bridge_cycle_state.json`
- `bridge/state/bridge_cycle.lock.json`
- `bridge/state/cycle_error_state.json`
- a safe `systemctl show` subset when available

Primary incident records are local JSON files under:

```text
bridge/incidents/YYYY-MM/
```

`bridge/outbox/messages/` is only a best-effort publish attempt for later
GitHub delivery. If outbox write fails, the local JSON incident remains the
source of truth.

V1 is observation-only. It does not restart services, delete locks, reclaim
locks, change heartbeat/watchdog body behavior, change timers, or perform git
housekeeping.

Manual real runtime test returned `incident_count=0`. Isolated tests covered
healthy cycle, cycle missing, summary stale, stuck running, stale lock, stalled
step, active cycle error, deduplication, and outbox write failure.

A false `bridge_service_failed` incident caused by sandboxed `systemctl`
unavailability was removed; unavailable `systemctl` is now recorded as a safe
snapshot field, not as an incident.

Published across:

```text
b53ae61 Sync RPi bridge outbound state
568e568 Sync RPi bridge outbound state
ae64254 Sync RPi bridge outbound state
```

### Runtime Inbox Lifecycle

Introduced a runtime-only live inbox for bridge work:

```text
/home/fiste/Noema/bridge/inbox/messages/
```

The GitHub inbox remains the audit input tape:

```text
body/bridge/inbox/messages/
```

Inbound sync now hydrates the runtime inbox copy-only from the GH mirror. It
skips messages already recorded in `bridge/state/processed_messages.json` with
terminal bridge-agent statuses: `ok`, `ignored`, `pending_codex`, or `error`.
`pending` is not terminal and can be retried after a crash.

The bridge agent now reads runtime inbox messages and archives processed files
locally under:

```text
/home/fiste/Noema/bridge/inbox/processed/YYYY-MM/
```

Invalid runtime inbox messages are error-reported, recorded by sha256, and
archived with an `invalid-` filename prefix so the live inbox does not stay
dirty. The processed archive is runtime-local and is not mirrored or pushed.

Real e2e test:

- input: `body/bridge/inbox/messages/2026-06-08T194555Z_runtime-inbox-e2e-codex-request.md`
- local Codex request: `codex/inbox/2026-06-08T194906Z_codex-request-runtime-inbox-e2e-20260608T194555Z.md`
- archived runtime input: `bridge/inbox/processed/2026-06/2026-06-08T194555Z_runtime-inbox-e2e-codex-request.md`
- second inbound sync rehydrated `0` files.

Published across:

```text
54b1cfc Sync RPi bridge outbound state
0b16638 Sync RPi bridge outbound state
```

### PC-Codex Postman Quick Rule

Added a short quick-reference version of the PC-Codex postman rules.

Changed:

- `body/bridge/instructions/pc_codex_postman_quick.md`

Behavior:

- summarizes the one-file inbox delivery rule, clean checkout checks, allowed
  envelope fixes, narrow commit scope, reporting requirements, and stop
  conditions;
- no runtime bridge behavior was changed.

### Block Bridge Script Bytecode Publishing

Removed an accidentally tracked Python bytecode cache file from the bridge
script mirror and hardened outbound publishing against future bytecode cache
publication.

Changed:

- `bridge/scripts/.gitignore`
- `body/bridge/scripts/.gitignore`
- `bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/scripts/__pycache__/bridge_sync_outbound.cpython-311.pyc`

Behavior now:

- `body/bridge/scripts/__pycache__/` and `*.pyc`/`*.pyo`/`*.pyd` files are
  ignored in the bridge script mirror;
- outbound staging rejects script cache paths unless the change is deleting an
  already tracked cache file;
- the existing tracked `bridge_sync_outbound.cpython-311.pyc` is removed from
  the repository;
- runtime bridge behavior is unchanged.

### PC-Codex Postman Instructions

Added a repository instruction document for the PC-Codex postman role.

Changed:

- `body/bridge/instructions/pc_codex_postman.md`
- `bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/scripts/bridge_sync_outbound.py`

Behavior:

- documents PC-Codex as a narrow GitHub tape postman for delivering exactly one
  requested Codex inbox message;
- records allowed scope, forbidden paths/actions, filename rules, delivery
  procedure, `created_at` rules, stop conditions, push rejection handling, and
  response template;
- outbound sync now allows the documentation-only
  `body/bridge/instructions/` path so instruction files can be published by the
  bridge audit flow;
- no heartbeat/watchdog behavior, bridge lock logic, timer cadence,
  inbox/outbox processing, or Git housekeeping was changed.

### Bridge Logging Cleanup Final State

Closed the bridge logging cleanup pass after removing duplicate publication,
restoring local-only rotation, reducing duplicate runtime log writes, and
filtering the public summary tail.

Current behavior:

- raw `/home/fiste/Noema/bridge/logs/bridge.log` remains local-only;
- standalone `body/bridge/logs/bridge_tail.log` is no longer created,
  published, or tracked;
- `body/bridge/logs/` is absent from the repository checkout because Git does
  not track empty directories;
- bridge agent stdout is no longer re-logged by `bridge_cycle.py`;
- runtime `bridge.log` rotates locally after `8000` lines and retains `3000`
  active lines;
- rotation archives stay local under
  `/home/fiste/Noema/bridge/logs/archive/YYYY-MM/`;
- public `body/bridge/state_summary/latest.md` keeps a filtered `Bridge Log
  Tail` with a default maximum of `60` lines;
- the summary writer reads the runtime log tail backwards in small byte chunks,
  avoiding full-file log reads during normal summary generation.

Observed after rollout:

- `latest.md` was reduced to a small public summary, about 86-95 lines during
  normal operation;
- runtime `bridge.log` continued as the full diagnostic log and was about
  3.4k-3.6k active lines after rotation;
- the only recurring dirty file after cycles is the expected generated
  `body/bridge/state_summary/latest.md`;
- no heartbeat/watchdog, bridge lock semantics, timer cadence, inbox/outbox
  processing, task allowlist, or Git housekeeping behavior was intentionally
  changed.

### Filtered Public Bridge Log Tail

Reduced the public log tail in `body/bridge/state_summary/latest.md` without
changing the local runtime log.

Changed:

- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

Behavior now:

- default public `Bridge Log Tail` is `60` filtered lines instead of `120` raw
  lines;
- the summary writer reads the runtime log tail backwards in small byte chunks
  instead of loading the whole file;
- filtering scans only a bounded tail window before selecting public lines;
- routine no-op noise such as already-processed messages, normal fetch output,
  no-op outbound summaries, and repeated root/path lines is omitted from the
  public tail;
- WARN/ERROR lines, cycle step boundaries, bridge cycle completion, runtime log
  rotation notices, body state observations, task lines, replies, and concise
  count lines remain visible;
- local `/home/fiste/Noema/bridge/logs/bridge.log` is unchanged and remains the
  full runtime diagnostic log.

Verified:

- runtime and mirrored `write_bridge_summary.py` copies match;
- Python syntax compilation passes for both copies;
- local summary generation writes `latest.md` with a filtered bridge log tail.

### Runtime-Only Bridge Log Rotation

Moved bridge runtime log rotation back into the bridge runtime cycle, separate
from outbound publishing.

Changed:

- `bridge/scripts/bridge_cycle.py`
- `body/bridge/scripts/bridge_cycle.py`

Behavior now:

- `bridge_cycle.py` checks `/home/fiste/Noema/bridge/logs/bridge.log` before
  writing the first line of a new cycle;
- if the log has more than `8000` lines, older lines are archived under
  `/home/fiste/Noema/bridge/logs/archive/YYYY-MM/`;
- the newest `3000` lines are retained in the active runtime log;
- the rotation archive remains local and is not mirrored to `symnozein`;
- outbound sync remains responsible only for publishing allowed repository
  outputs, not for runtime log maintenance.

Verified:

- runtime and mirrored `bridge_cycle.py` copies match;
- Python syntax compilation passes for both copies;
- rotation is scoped to `/home/fiste/Noema/bridge/logs/bridge.log` under the
  bridge runtime root.

### Stop Re-Logging Bridge Agent Stdout

Reduced duplication in `/home/fiste/Noema/bridge/logs/bridge.log` by stopping
`bridge_cycle.py` from writing the bridge agent's stdout back into the same
runtime log.

Changed:

- `bridge/scripts/bridge_cycle.py`
- `body/bridge/scripts/bridge_cycle.py`

Behavior now:

- `run_step(...)` accepts `log_stdout`, defaulting to `True` for existing child
  steps;
- the `bridge agent` step calls `run_step(..., log_stdout=False)`;
- `bridge_agent_v2.py` still writes its own lines directly to `bridge.log`;
- bridge agent stderr remains captured and logged by the cycle wrapper;
- inbound sync, summary writer, and outbound sync stdout logging remain
  unchanged.

Verified:

- runtime and mirrored `bridge_cycle.py` copies match;
- Python syntax compilation passes for both copies;
- no heartbeat/watchdog, bridge lock, timer cadence, inbox/outbox processing,
  outbound sync, or Git housekeeping behavior was changed.

### Stop Publishing Bridge Tail Log

Removed the standalone repository mirror of the runtime bridge log tail because
`body/bridge/state_summary/latest.md` already carries the public bridge log
tail needed for orientation.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/logs/bridge_tail.log`

Behavior now:

- outbound sync no longer creates or updates
  `body/bridge/logs/bridge_tail.log`;
- the now-empty mirror directory `body/bridge/logs/` was removed from the
  checkout; Git does not track empty directories;
- runtime `/home/fiste/Noema/bridge/logs/bridge.log` remains local and is not
  mirrored or rotated by outbound sync;
- public bridge log tail remains available through
  `body/bridge/state_summary/latest.md`, generated by
  `write_bridge_summary.py`;
- normal outbound staging no longer treats `bridge_tail.log` as an allowed
  published path;
- `bridge_tail.log` is kept only in a deprecated removal list so its tracked
  deletion can be staged and committed once, without allowing future published
  updates.

Verified:

- runtime and mirrored `bridge_sync_outbound.py` copies match;
- Python syntax compilation passes for the touched outbound sync script;
- outbound dry-run does not recreate `body/bridge/logs/bridge_tail.log`;
- `body/bridge/logs/` is absent from the repository checkout after the tracked
  log tail file was removed;
- runtime `bridge/logs/bridge.log` remains present.

### Bridge Cycle Lock Diagnostics

Improved bridge cycle lock visibility so a blocked or overlapping cycle leaves
actionable diagnostics instead of only reporting that a lock exists.

Changed:

- `bridge/scripts/bridge_cycle_lock.py`
- `body/bridge/scripts/bridge_cycle_lock.py`
- `bridge/scripts/bridge_cycle.py`
- `body/bridge/scripts/bridge_cycle.py`

Behavior now:

- cycle locks include `status`, `current_step`, `last_progress_at`, `owner`,
  and `host`;
- active-lock errors report whether the recorded PID is alive, lock age,
  current step, progress age, expiry, owner, and host;
- `bridge_cycle.py` updates lock progress before each major step:
  inbound sync, bridge agent, bridge summary, and outbound sync;
- released locks preserve the diagnostic fields and mark
  `current_step=released`;
- lock files remain runtime-local under `/home/fiste/Noema/bridge/state/`.

Verified:

- runtime and mirrored bridge script copies match, except for ignored local
  `__pycache__` files;
- the latest script mirror committed the cycle lock and cycle updates;
- post-check dirty state only showed expected generated outputs:
  `body/bridge/logs/bridge_tail.log` and
  `body/bridge/state_summary/latest.md`.

### Runtime Heartbeat Watchdog Tolerance

Adjusted the local runtime heartbeat/watchdog behavior after two same-day
false `heartbeat_timeout` flips were traced to heartbeat age crossing the old
30 second threshold by only a fraction of a second.

Changed runtime files:

- `core/hb/heartbeat.py`
- `core/watchdog/state_watchdog.py`

Changed mirrored bridge summary script:

- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

Behavior now:

- heartbeat timeout threshold is `45` seconds;
- watchdog requires `2` consecutive heartbeat timeout checks before setting
  `awake=false` / `status=heartbeat_timeout`;
- heartbeat writes `heartbeat_count`, `heartbeat_last_gap_seconds`, and
  `heartbeat_max_gap_seconds` into `/home/fiste/Noema/state/body_state.json`;
- watchdog writes `watchdog_last_hb_age_seconds`,
  `watchdog_max_hb_age_seconds`, `heartbeat_timeout_count`, and
  `heartbeat_timeout_required_count` into the same runtime state;
- public bridge summary renders the new heartbeat/watchdog metrics.

Deployment notes:

- `noema-heartbeat.service` was restarted to load the heartbeat changes;
- `noema-watchdog.service` was restarted to load the 45 second threshold and
  two-check hysteresis;
- two `missing_services: noema-heartbeat.service` state events were produced
  during the maintenance window while heartbeat was intentionally stopped.

Verified:

- both services are active after restart;
- `body_state.json` shows `watchdog_max_hb_age_seconds: 45`,
  `heartbeat_timeout_required_count: 2`, and `heartbeat_timeout_count: 0`;
- the public summary shows heartbeat count, heartbeat gap metrics, watchdog
  heartbeat age, timeout threshold, and hysteresis count;
- synthetic hysteresis check confirms the first >45s miss keeps
  `awake=true`, the second consecutive miss sets `heartbeat_timeout`, and a
  fresh heartbeat resets the count.

Mirror boundary:

- runtime `core/` files are not mirrored to `symnozein` yet;
- current mirror scope remains bridge-owned files only, mainly
  `body/bridge/scripts`, `body/bridge/state_summary`, `body/bridge/logs`, and
  bridge outbox files;
- no `core/` paths are tracked in the `symnozein` mirror.

### Exact Inbound Mirror And Codex Path Visibility

Tightened the bridge inbox mirror rule so the Raspberry Pi checkout mirrors the
GitHub inbox, while the Raspberry Pi never publishes inbox changes back to
GitHub.

Changed:

- `bridge/scripts/bridge_sync_inbound.py`
- `body/bridge/scripts/bridge_sync_inbound.py`
- `bridge/scripts/bridge_agent_v2.py`
- `body/bridge/scripts/bridge_agent_v2.py`
- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

Behavior now:

- `body/bridge/inbox/messages` is treated as an exact local worktree mirror of
  `FETCH_HEAD`;
- inbound sync restores files from `FETCH_HEAD` and removes stale local files
  under `body/bridge/inbox/messages`;
- stale inbound pruning is local-only and does not stage, commit, or push inbox
  paths;
- outbound sync still excludes inbox paths from `ALLOWED_REPO_PATHS`, so the
  Raspberry Pi reads the GitHub inbox but does not write it back;
- bridge agent logs observed file counts and latest file names for
  `body/bridge/inbox/messages/codex` and `body/bridge/outbox/codex`;
- public summary reports codex inbox/outbox file counts, not just `*.md`
  counts, because historical codex inbox files include extensionless files.

Verified:

- inbound dry-run against current `origin/main` reports no inbound changes;
- local `body/bridge/inbox/messages` and `FETCH_HEAD` both contain 16 files,
  with no local-only or remote-only paths;
- local `body/bridge/outbox/codex` and `FETCH_HEAD` both contain 12 files,
  with no local-only or remote-only paths;
- a timer cycle completed successfully after the change;
- post-cycle status only showed expected runtime outputs:
  `body/bridge/logs/bridge_tail.log` and
  `body/bridge/state_summary/latest.md`;
- no `bridge_cycle.py`, systemd unit/timer, allowlist, runtime task execution,
  or Codex reader automation changes were made.

### Codex Inbox Reader Manual Writer Stub

Added an optional manual `--write-stub` mode to the standalone Codex inbox
reader.

Changed:

- `bridge/scripts/codex_inbox_reader.py`
- `body/bridge/scripts/codex_inbox_reader.py`
- `bridge/scripts/tasks/TASK_REQUESTS.md`
- `body/bridge/scripts/tasks/TASK_REQUESTS.md`

Behavior:

- default mode remains dry-run with no file writes, no state updates, no
  commits, and no pushes;
- `--write-stub` reads `body/bridge/inbox/messages/codex/*.md` with the same
  validation and classification as dry-run;
- runtime-local state is stored at
  `/home/fiste/Noema/bridge/state/codex_reader_state.json`;
- processed messages are keyed by `message_id` plus `sha256(content)`;
- repeated runs of the same message/hash do not duplicate a response;
- the same `message_id` with a different hash is recorded as `conflict`;
- safe classified requests create a stub `codex_response` with
  `status: stub_written` under `body/bridge/outbox/codex/`;
- risky or unknown requests create a stub response with
  `status: needs_human`;
- generated response paths are constrained to `body/bridge/outbox/codex/`.

Verified:

- syntax compiles with `PYTHONDONTWRITEBYTECODE=1`;
- `/tmp` dry-run fixture has no side effects and creates no state/outbox files;
- `/tmp` writer-stub fixture creates one safe stub response;
- repeated writer-stub run does not duplicate the response;
- same message id with changed content hash records a conflict;
- risky request produces `needs_human`;
- state is written under the runtime root, not under the repo tree;
- no `bridge_cycle.py`, systemd unit/timer, allowlist, outbound sync rules,
  runtime task processing, or automatic reader startup changes were made.

### Heartbeat Log Start Metrics In Public Summary

Extended the public bridge summary with heartbeat start-log metrics derived
from `core/hb/logs/heartbeat.log`.

Changed:

- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

New fields:

- `Heartbeat log starts count`
- `Heartbeat log latest start`
- `Heartbeat log max start gap seconds`

Verified:

- summary writer syntax compiles with `PYTHONDONTWRITEBYTECODE=1`;
- local summary generation renders the new fields;
- no heartbeat service restart, `bridge_cycle.py`, systemd, allowlist, task
  processing, outbound sync, or Codex reader automation changes were made.

### Heartbeat Uptime In Public Summary

Added heartbeat uptime visibility to the public bridge summary without changing
the heartbeat service, watchdog service, bridge cycle, systemd units, allowlist,
task processing, or outbound sync rules.

Changed:

- `bridge/scripts/write_bridge_summary.py`
- `body/bridge/scripts/write_bridge_summary.py`

Behavior:

- `latest.md` now includes heartbeat service start, heartbeat uptime seconds,
  restart count, uptime source, and last heartbeat gap seconds;
- the summary writer first tries systemd service metadata for
  `noema-heartbeat.service`;
- when systemd metadata is unavailable, it falls back to the last
  `heartbeat started` line in `core/hb/logs/heartbeat.log`;
- max heartbeat gap since start is explicitly marked unavailable without
  heartbeat state history.

Verified:

- Codex dry-run reader classified the request as `design_review` and reported
  all side effects as false;
- `write_bridge_summary.py` renders the new fields locally;
- no heartbeat service restart was needed;
- no `bridge_cycle.py`, systemd unit/timer, allowlist, runtime task processing,
  Codex reader automation, outbound sync rules, existing inbox/outbox messages,
  or audit files were changed.

### Codex Inbox Reader Dry-Run

Prepared the first safe standalone dry-run step for a future Codex inbox
reader.

Changed:

- `bridge/scripts/codex_inbox_reader.py`
- `body/bridge/scripts/codex_inbox_reader.py`
- `bridge/scripts/tasks/TASK_REQUESTS.md`
- `body/bridge/scripts/tasks/TASK_REQUESTS.md`

Behavior:

- scans only `body/bridge/inbox/messages/codex/*.md`;
- ignores hidden files, symlinks, non-files, and files outside the allowed
  inbox directory;
- rejects files larger than 64 KiB;
- parses YAML frontmatter and extracts `id`, `type`, `sender`, `target`, and
  `created_at`;
- computes `sha256(content)`;
- classifies requests as `design_review`, `documentation_review`,
  `status_summary`, `safety_review`, `needs_human`, or `invalid`;
- prints what it would do and writes nothing.

State specification:

- future runtime-local state path:
  `/home/fiste/Noema/bridge/state/codex_reader_state.json`;
- dry-run mode does not create or update that file.

Verified:

- real inbox dry-run succeeds and reports side effects as false for file writes,
  outbox writes, commits, and pushes;
- `/tmp` fixture confirms a design request becomes `design_review`, a risky
  request becomes `needs_human`, and a file without frontmatter becomes
  `invalid`;
- no `bridge_cycle.py`, systemd unit/timer, allowlist, runtime task processing,
  outbound sync rules, existing inbox/outbox messages, or audit files were
  changed.

### Git Housekeeping Cleanup After Rebase Fix

Cleared the Git maintenance warnings that were still appearing in every bridge
cycle after the safe rebase fix.

Operational steps:

- stopped `bridge-cycle.timer` before maintenance;
- inspected all `bridge-outbound-pre-rebase` stashes and verified they contained
  only derived bridge outputs:
  `body/bridge/logs/bridge_tail.log` and
  `body/bridge/state_summary/latest.md`;
- cleared those stale bridge rebase stashes;
- removed only Git housekeeping files:
  `symnozein/.git/gc.log` and
  `symnozein/.git/objects/pack/tmp_pack_*`;
- ran `git prune`;
- ran `git gc --prune=now`;
- restarted `bridge-cycle.timer`.

Verified:

- `git fsck --connectivity-only --no-progress` exits cleanly with no output;
- `git count-objects -vH` reports `garbage: 0`, `size-garbage: 0 bytes`,
  `packs: 1`, and only a small loose object count after subsequent cycles;
- `symnozein/.git/gc.log` no longer exists;
- `git stash list` is empty;
- post-cleanup bridge cycles finish with `status: ok` and no GC/prune warning
  in the journal;
- no audit outbox files, inbox files, bridge runtime state, allowlist, systemd
  config, or bridge runtime logic were changed.

### Safe Pre-Push Rebase Inbox Handling

Fixed an outbound sync failure where pre-push rebase stashed an
inbound-restored inbox file as untracked, then failed on `stash pop` after the
same file arrived from `FETCH_HEAD` as tracked.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`
- `body/bridge/scripts/bridge_sync_outbound.py`

Behavior now:

- worktree status uses `--untracked-files=all` so inbox file paths are checked
  precisely;
- before rebase, only local-only untracked inbox files that exactly match
  `FETCH_HEAD` are removed, allowing rebase to restore them as tracked files;
- pre-rebase stash is limited to existing `ALLOWED_REPO_PATHS`;
- `LOCAL_ONLY_REPO_PATHS` / inbox files are not stashed;
- `git stash push --include-untracked` is no longer used.

Verified with a local `/tmp` reproduction: remote added an inbox file, the same
file existed locally as untracked, an allowed outbound file was dirty, rebase
completed, the inbox file became tracked from remote HEAD, the outbound change
remained, and no test stash was left behind.

Cleanup: removed an accidentally mirrored Python bytecode file from
`body/bridge/scripts/__pycache__/` after syntax verification generated it.

### Git Maintenance Review And Local GC

Reviewed the repeated Git maintenance warning from `.git/gc.log` and the
transient outbound sync error. The repository had many unreachable loose
objects, while tracked state was clean except expected bridge-owned runtime
outputs.

Checked:

- `git status -sb`
- `.git/gc.log`
- `git count-objects -vH`
- `git fsck --connectivity-only --no-progress`
- `bridge-cycle.service` and `bridge-cycle.timer` status

Maintenance performed:

- temporarily stopped `bridge-cycle.timer` to avoid colliding with outbound
  sync;
- ran `git gc --prune=now` in `symnozein`;
- restarted `bridge-cycle.timer`.

Verified:

- loose object count went from `21201` / `84.34 MiB` to `0`;
- pack count went from `33` to `1`;
- `.git/gc.log` no longer exists;
- `git fsck --connectivity-only --no-progress` exits cleanly with no output;
- no audit outbox files, runtime state files, allowlist, systemd config, or
  bridge runtime logic were changed;
- remaining worktree changes are only expected bridge-owned outputs:
  `body/bridge/logs/bridge_tail.log` and
  `body/bridge/state_summary/latest.md`.

### Known Bridge Limits Anchor

Added an operational anchor for known bridge limits:

```text
body/bridge/docs/known_limits.md
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

### Body State Atomic Writes And Bridge Cycle Recovery

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

### Passive Codex Request Queue

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

### One-Time Cycle Error Reporting

Fixed repeated cycle error spam. The cycle now fingerprints the active error
and writes only one outbox error for the same failure. Repeats update local
state instead of creating a new error file every 30 seconds.

Changed:

- `bridge/scripts/bridge_cycle.py`

### Safe Inbound Handling For Existing Inbox Files

Adjusted inbound sync so an identical local inbox file and remote inbox file are
accepted as the same message. A real content conflict still stops the cycle.

Changed:

- `bridge/scripts/bridge_sync_inbound.py`

### Outbound Rebase Tolerance For Local Inbox

Allowed local inbox files to exist during outbound rebase checks without being
treated as forbidden outbound changes. Inbox is still not staged or pushed by
outbound sync.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

Published with the first successful task result as:

```text
9b4df4c Sync RPi bridge outbound state
```

### Task Request Guide

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

### Runtime Log Tail And Rotation

Stopped publishing the full bridge log to GitHub. Outbound sync now publishes:

```text
symnozein/body/bridge/logs/bridge_tail.log
```

Runtime `bridge/logs/bridge.log` rotates after 8000 lines, retaining 3000 lines.
Archives are stored under:

```text
bridge/logs/archive/YYYY-MM/
```

Published across:

```text
72740cc Sync RPi bridge outbound state
aade471 Sync RPi bridge outbound state
```

### Safe Pre-Push Rebase

Outbound sync now fetches and safely rebases before commit/push when local
changes are limited to bridge-owned paths. It uses no force push and refuses
disallowed worktree changes.

Changed:

- `bridge/scripts/bridge_sync_outbound.py`

### Systemd Bridge Cycle

Installed and validated a one-shot bridge cycle controlled by a systemd timer.
The service runs the sequence:

1. inbound sync
2. `bridge_agent_v2.py`
3. `write_bridge_summary.py`
4. outbound sync

The timer fires every 30 seconds. There is no daemon loop inside the bridge
scripts.

### Allowlisted Task Runner

Added `task_request` support to the bridge agent. Tasks run only from:

```text
/home/fiste/Noema/bridge/scripts/tasks/
```

Execution is controlled by `allowlist.json`, uses `shell=False`, enforces string
arguments, timeout, non-root execution, stdout/stderr capture, and task run
state in local `task_runs.json`.

### Bridge Cycle Stale Lock Handling

Investigated repeated `rpi5_cycle-error-unknown` outbox spam. Root cause was a
systemd `TimeoutStartSec=25` kill during `inbound sync`, leaving an active
15-minute lock with a dead PID. Subsequent 30-second timer runs treated the lock
as active until expiry and published one error file per tick.

Narrow fix applied:

- `bridge_cycle_lock.py` reclaims only local bridge-cycle locks with
  `status=active`, matching owner/host, and `pid_alive is False`.
- Live PIDs are never overwritten.
- `bridge_cycle.py` infers `step` from `current_step=...` in lock errors when
  `last_step` is not set yet.
- Lock-error dedup fingerprints ignore volatile age/progress values, so repeated
  stale-lock reports do not create a new outbox file every timer tick.

Runtime behavior intentionally unchanged outside lock/error reporting: no
heartbeat/watchdog, timer cadence, `TimeoutStartSec`, inbox/outbox processing,
logging cleanup, or git housekeeping changes.

Published by bridge cycle as:

```text
ee4db0b Sync RPi bridge outbound state
e882369 Sync RPi bridge outbound state
```
