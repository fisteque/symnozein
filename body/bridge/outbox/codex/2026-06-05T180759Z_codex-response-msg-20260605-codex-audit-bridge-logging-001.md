---
id: codex-response-msg-20260605-codex-audit-bridge-logging-001
type: codex_response
created_at: 2026-06-05T18:07:59Z
author: Codex
target: noema
reply_to: msg-20260605-codex-audit-bridge-logging-001
status: audit_complete
---

# Codex Response

Audit only. No runtime code, service, timer, heartbeat, watchdog, inbox/outbox
processing, or Git housekeeping behavior was changed.

## Relevant Files And Functions

- `bridge/scripts/bridge_cycle.py`
  - `cycle_log(...)`: appends cycle lines to
    `/home/fiste/Noema/bridge/logs/bridge.log` and prints the same line to
    stdout.
  - `run_step(...)`: captures each child step's stdout/stderr, then writes the
    captured text back into `bridge.log` through `cycle_log(...)`.
- `bridge/scripts/bridge_agent_v2.py`
  - `LOG_FILE = BRIDGE_ROOT / "logs" / "bridge.log"`.
  - `log(...)`: appends agent lines to `bridge.log` and prints the same line to
    stdout.
  - `process_inbox(...)`: logs routine start/end, body state observation,
    inbox counts, already-processed messages, pending counts, replies, and
    errors.
  - `run_allowlisted_task(...)`: logs task start/end and truncated task
    stdout/stderr.
- `bridge/scripts/write_bridge_summary.py`
  - `tail_lines(...)`: reads a file and returns the last N lines.
  - `render_summary(...)`: reads
    `/home/fiste/Noema/bridge/logs/bridge.log` through
    `tail_lines(..., log_lines)`.
  - default `--log-lines` is `120`.
  - appends the result under `## Bridge Log Tail` in
    `body/bridge/state_summary/latest.md`.
- `bridge/scripts/bridge_sync_outbound.py`
  - no longer creates or publishes `body/bridge/logs/bridge_tail.log`.
  - allowed outbound paths are now outbox, Codex outbox, state summary, and
    scripts.
  - `body/bridge/logs/bridge_tail.log` remains only in a deprecated removal
    list for its already-committed deletion path.
- `core/hb/heartbeat.py`
  - writes only to `core/hb/logs/heartbeat.log`, not to bridge runtime log.
- `core/watchdog/state_watchdog.py`
  - writes only to `core/watchdog/logs/watchdog.log`, not to bridge runtime
    log.
- `bridge/scripts/legacy/bridge_agent.py`
  - historical script that also targeted `bridge/logs/bridge.log`, but it is
    not the current cycle path.

## Current Log Flow

1. `bridge_cycle.py` starts a timer cycle and writes cycle boundary/progress
   lines directly into `bridge/logs/bridge.log`.
2. It runs child steps with captured stdout/stderr:
   inbound sync, bridge agent, summary writer, outbound sync.
3. `bridge_agent_v2.py` writes its own structured text lines directly into the
   same `bridge.log`.
4. The agent also prints those same lines to stdout.
5. `bridge_cycle.py` captures that stdout and writes it back into `bridge.log`
   again as one cycle log message.
6. `write_bridge_summary.py` reads the last 120 lines of `bridge.log` and
   embeds them into `body/bridge/state_summary/latest.md`.
7. Outbound sync publishes `latest.md`; standalone `bridge_tail.log` is no
   longer created or tracked.

## Redundant Or Risky Parts

- The main duplication is agent logging:
  `bridge_agent_v2.log(...)` writes to `bridge.log`, then prints to stdout,
  then `bridge_cycle.run_step(...)` captures that stdout and writes the same
  content back into `bridge.log` with a `[cycle]` prefix.
- The same pattern can affect other child steps that print multi-line status:
  inbound sync, summary writer, outbound sync. They do not write directly to
  `bridge.log`, so for them capture is useful; for the agent it duplicates.
- `bridge.log` still grows quickly. Current observed size was about 6,988
  lines / 543,839 bytes, with many local archives under
  `bridge/logs/archive/2026-06/`.
- Rotation currently no longer lives in outbound sync after the
  `bridge_tail.log` cleanup. If no other active rotation path exists, runtime
  `bridge.log` can keep growing until a future cleanup task handles it.
- `latest.md` exposes raw tail lines. That is useful for audit/debug, but it
  also includes repetitive routine noise such as already-processed messages,
  normal fetch output, and repeated no-op outbound summaries.

## Suggested Cleaner Logging Architecture

Separate three surfaces:

1. Local runtime debug log
   - Path: `/home/fiste/Noema/bridge/logs/bridge.log`.
   - Local only, never mirrored directly.
   - Contains full cycle and child process diagnostics.
   - Has explicit local rotation owned by a small runtime logging helper or
     by `bridge_cycle.py`, not by outbound publishing.

2. Public summary tail
   - Path: `body/bridge/state_summary/latest.md`.
   - Small, filtered, and intentionally public.
   - Should show recent WARN/ERROR lines, last cycle status, last step, lock
     progress, and maybe the latest few INFO lines.
   - Should not publish a raw 120-line dump forever unless debugging requires
     it.

3. Structured state/event records
   - Runtime-local JSON: `bridge/state/bridge_cycle_state.json`,
     `processed_messages.json`, `event_state.json`, `task_runs.json`.
   - Public event messages: outbox `state_event`, `error`, `task_result`,
     `codex_response`.
   - These should remain the durable audit layer for significant facts, while
     logs stay diagnostic.

## Minimal Safe Implementation Plan

For a later implementation task:

1. Stop duplicate agent log capture.
   - Add an option in `bridge_cycle.run_step(...)`, e.g.
     `log_stdout=True`.
   - Call the bridge agent step with `log_stdout=False` or a mode that logs
     only child stderr/nonzero output.
   - Keep stdout capture for inbound sync, summary writer, and outbound sync.

2. Add local runtime log rotation outside outbound sync.
   - Put a narrow helper in `bridge_cycle.py` or a dedicated local function.
   - Rotate only `/home/fiste/Noema/bridge/logs/bridge.log`.
   - Keep archives local under `bridge/logs/archive/`.
   - Do not mirror archives to `symnozein`.

3. Filter public summary tail.
   - Keep `latest.md` as the public operational summary.
   - Prefer a smaller section such as:
     - last cycle status,
     - last cycle error if present,
     - recent WARN/ERROR lines,
     - last 20 routine INFO lines at most.
   - Make `--log-lines` lower by default only after verifying the summary
     remains useful.

4. Preserve current audit messages.
   - Do not replace `state_event`, `error`, `task_result`, or Codex outbox
     responses with logs.
   - Logs should support investigation; they should not be the source of truth.

## What I Would Not Change

- Do not mirror raw `bridge.log` or archived bridge logs into the repository.
- Do not reintroduce `body/bridge/logs/bridge_tail.log`.
- Do not change heartbeat/watchdog logging in this task; their logs are
  separate local subsystem logs.
- Do not change timer cadence, bridge lock semantics, inbox/outbox processing,
  task allowlist behavior, or Git housekeeping.
- Do not remove `Bridge Log Tail` from `latest.md` abruptly; reduce or filter
  it in a separate reviewed change.

## Bottom Line

The post-cleanup outbound path is cleaner: `bridge_tail.log` is gone and the
only public log view is `latest.md`. The remaining architectural issue is that
`bridge.log` is both a direct agent log and a cycle-captured child stdout log,
which causes duplication and fast growth. The next safest improvement is to
stop re-logging agent stdout in `bridge_cycle.py`, then move local rotation into
a dedicated runtime-only path.
