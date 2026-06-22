# Bridge Safety Model

This document describes the active safety model for the Noema bridge. Historical
ledger entries may describe older shapes of the system; this file describes the
current operating model.

## Roles

- Ondra is the human safety and relationship anchor.
- Noema may create intent and messages, but does not directly mutate runtime or
  GitHub state in this mode.
- PC-Codex may act only as a narrow postman when explicitly asked by Ondra.
- The Raspberry Pi bridge is an executor and audit body, not a general agent.
- Codex autoreply is a read-only answering layer for one local Codex request at
  a time.

## Layers

- GitHub mirror: `/home/fiste/Noema/symnozein`
- Bridge runtime: `/home/fiste/Noema/bridge`
- Local Codex queue: `/home/fiste/Noema/codex`

GitHub is an audit tape and transport layer. Runtime queues, state JSON, locks,
logs, incidents, and archives are operational state and stay local unless an
explicit bridge rule publishes a public summary or message.

## Write Authority

Verified write paths are intentionally narrow:

- PC-Codex postman may deliver exactly one reviewed Markdown inbox message when
  following the postman instructions.
- The bridge cycle may publish allowed outbound paths through the outbound
  allowlist.
- The body pulse may publish `body/bridge/state_summary/latest.md` only.
- Codex autoreply may write one response to `bridge/outbox/messages/` and
  archive the source Codex request after the response is written.

No other AI or chat layer should be treated as having write authority without a
separate approval, narrow scope, audit trail, and stop mechanism.

## Autoreply Boundaries

`codex_autoreply_worker.py` may call `codex exec` only in read-only,
non-interactive mode. The model answer is text; the wrapper is the only writer.

The worker must not commit, push, edit files, delete files, install packages,
restart services, change runtime state, or process more than one request per
run.

Requests classified as `needs_human` require explicit human review before any
automatic Codex execution.

## GitHub Write Limit

Direct ChatGPT or scheduled GitHub writes are not a verified path. Tests have
failed with:

```text
403 Resource not accessible by integration
```

Installing or widening a ChatGPT/GitHub App would be a new write-authority path,
not a bridge fix. It should remain closed unless Ondra explicitly approves a
narrow safety model.

## Safety Rule

Every new communication or write path is considered only a proposal until there
is an inspectable artifact: a commit, outbox message, updated summary, local
state record, or other durable proof.
