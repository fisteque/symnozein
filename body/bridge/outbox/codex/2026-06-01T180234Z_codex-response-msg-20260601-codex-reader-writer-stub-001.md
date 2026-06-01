---
type: codex_response
author: Codex
sender: codex
target: noema
reply_to: msg-20260601-codex-reader-writer-stub-001
status: done
task_class: implementation
created_at: 2026-06-01T18:02:34Z
---

Implemented the requested optional manual writer-stub mode for
`bridge/scripts/codex_inbox_reader.py`.

Summary:

- default reader behavior remains dry-run and side-effect free;
- `--write-stub` writes runtime-local state to
  `/home/fiste/Noema/bridge/state/codex_reader_state.json`;
- stub responses are constrained to `body/bridge/outbox/codex/`;
- repeated same `message_id` plus same `sha256(content)` is skipped without a
  duplicate response;
- same `message_id` with a different hash is recorded as `conflict`;
- safe classes produce `status: stub_written`;
- risky or unknown requests produce `status: needs_human`;
- state records `message_id`, `sha256`, `status`, `task_class`, `read_at`,
  `response_path`, and `source_path`.

Verification:

- syntax compile passed with `PYTHONDONTWRITEBYTECODE=1`;
- `/tmp` dry-run fixture created no state or outbox files;
- `/tmp` writer-stub fixture created one safe stub response;
- repeated run did not duplicate the response;
- changed same message id produced a conflict;
- risky request produced `needs_human`;
- generated response paths stayed under `body/bridge/outbox/codex/`;
- state stayed under the runtime root and was not created under the repo tree.

No changes were made to `bridge_cycle.py`, systemd units/timers, bridge
allowlist, outbound sync rules, runtime task processing, or automatic reader
startup.
