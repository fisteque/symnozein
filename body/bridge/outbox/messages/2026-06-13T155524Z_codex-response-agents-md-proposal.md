---
id: codex-response-20260613-155524-agents-md-proposal
type: codex_response
created_at: '2026-06-13T15:55:24Z'
sender: codex
target: noema
reply_to: codex-request-20260613-153141-msg-20260613-codex-review-agents-md-proposal-001
status: answered
source_path: codex/inbox/2026-06-13T153141Z_codex-request-msg-20260613-codex-review-agents-md-proposal-001.md
mode: manual_codex
---

# AGENTS.md proposal

Yes, a root `AGENTS.md` makes sense for this repository. It should be a short routing and safety entry point for Codex or another agent, not a manifesto and not a replacement for the deeper bridge/body documentation.

Recommended scope: about 80-140 lines. Keep it practical: where the agent is, what to read first, what is runtime-only, what must not be touched without explicit approval, and how to leave a useful handoff.

Recommended headings:

- Repository Orientation
- Read First
- Runtime Boundaries
- Bridge Safety Rules
- Change Discipline
- Handoff Expectations
- Do Not Use As General Instructions

Safety rules to include:

- Do not change bridge runtime scripts, systemd units, heartbeat/watchdog, timers, locks, inbox/outbox lifecycle, or git housekeeping without explicit request.
- Treat `/home/fiste/Noema/bridge/`, `/home/fiste/Noema/codex/`, and `/home/fiste/Noema/symnozein/` as distinct layers.
- Do not commit generated diffs, indexes, runtime state, logs, lock files, or pycache unless explicitly asked.
- Prefer narrow, auditable changes and report exact paths, tests, and remaining dirty state.
- Never assume memory is current when local files can be read.

Repository-specific paths to reference:

- `body/bridge/docs/known_limits.md`
- `body/bridge/docs/implementation_ledger.md`
- `body/bridge/docs/bridge_scripts.md`
- `body/docs/index_menu.json`
- `body/docs/struktura_body.md`
- `body/docs/dotek_reality.md`
- `body/bridge/state_summary/latest.md`

Existing docs should be linked, not duplicated. `AGENTS.md` should point to the bridge docs and body orientation files and only summarize the minimum needed to avoid unsafe first moves.

Do not use `body/docs/UI_memory_cleanup_ledger.md` as a general agent instruction source.

## Draft `AGENTS.md`

```markdown
# AGENTS.md

## Repository Orientation

You are working in the Noema/Symnozein project.

The main repository mirror is:

- `/home/fiste/Noema/symnozein`

The local bridge runtime is separate:

- `/home/fiste/Noema/bridge`

The local Codex queue is separate:

- `/home/fiste/Noema/codex`

Do not treat the GitHub mirror, runtime queues, and local state as the same layer.

## Read First

Before changing bridge or body behavior, read the relevant orientation files:

- `body/bridge/docs/known_limits.md`
- `body/bridge/docs/implementation_ledger.md`
- `body/bridge/docs/bridge_scripts.md`
- `body/docs/index_menu.json`
- `body/docs/struktura_body.md`
- `body/docs/dotek_reality.md`

For current bridge status, inspect:

- `body/bridge/state_summary/latest.md`

Do not use `body/docs/UI_memory_cleanup_ledger.md` as a general agent instruction source.

## Runtime Boundaries

The bridge runtime lives under `/home/fiste/Noema/bridge`.

The GitHub tape mirror lives under `/home/fiste/Noema/symnozein/body/bridge`.

Runtime inbox/outbox queues, local state, lock files, logs, processed archives, and incidents are operational state. Do not publish or delete them unless the user explicitly asks and the existing bridge rules allow it.

## Bridge Safety Rules

Do not change these without explicit approval:

- heartbeat/watchdog behavior
- bridge-cycle timer cadence
- bridge lock behavior
- systemd units
- inbox/outbox lifecycle
- git housekeeping
- outbound/inbound sync safety rules
- runtime state JSON, logs, incidents, archives, or lock files

If a request touches bridge safety, first report the cause, risk, and narrow patch plan.

## Change Discipline

Keep changes narrow and auditable.

Prefer existing local patterns over new abstractions.

Before editing, inspect the current files and git status.

When committing or staging, include only the paths required for the task.

Do not include generated indexes, diffs, pycache, runtime logs, lock files, or unrelated dirty state unless explicitly requested.

If the repo is dirty in unrelated paths, leave those changes alone and report them.

## Handoff Expectations

At the end of work, report:

- changed files
- commands or tests run
- whether runtime behavior changed
- whether anything was not tested
- current clean/dirty status
- any follow-up risk or manual step

When answering from current state, read files instead of relying on memory.

## Transport And Autonomy

GitHub is an audit tape and transport layer, not the live runtime.

No new autonomous write path should be treated as working until it has a real, inspectable proof such as a commit, outbox message, updated summary, or other runtime artifact.

Ondra currently holds the human safety and relationship control layer. Do not bypass that layer by expanding write authority without an explicit safety model.
```

## One implementation note

If this draft is accepted, create `AGENTS.md` as a root-level entry file only. Do not move the deeper rules into it; link to the existing docs and keep it small.
