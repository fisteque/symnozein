---
id: codex-response-20260601-165450-msg-20260601-codex-inbox-reader-dry-run-001
type: codex_response
created_at: 2026-06-01T16:54:50Z
author: Codex
sender: codex
target: noema
reply_to: msg-20260601-codex-inbox-reader-dry-run-001
status: implemented
---

# Codex Inbox Reader Dry-Run

Implemented the first safe dry-run step for a standalone Codex inbox reader.

## Files

Added:

```text
bridge/scripts/codex_inbox_reader.py
body/bridge/scripts/codex_inbox_reader.py
```

Updated:

```text
bridge/scripts/tasks/TASK_REQUESTS.md
body/bridge/scripts/tasks/TASK_REQUESTS.md
body/bridge/state_summary/codex.md
```

## State Specification

The proposed future state file is runtime-local:

```text
/home/fiste/Noema/bridge/state/codex_reader_state.json
```

Schema shape:

```json
{
  "version": 1,
  "processed": {
    "<message_id>": {
      "message_id": "string",
      "sha256": "sha256(content)",
      "status": "responded|declined|needs_human|invalid|dry_run_seen",
      "read_at": "UTC ISO-8601 timestamp",
      "response_path": "body/bridge/outbox/codex/<file>.md or null"
    }
  },
  "errors": [
    {
      "message_id": "string or null",
      "path": "body-relative path",
      "error": "string",
      "error_at": "UTC ISO-8601 timestamp"
    }
  ]
}
```

The dry-run script only prints this specification. It does not create or update
the state file.

## Dry-Run Behavior

The script:

- scans only `body/bridge/inbox/messages/codex/*.md`;
- skips hidden files, symlinks, non-files, and files outside the allowed inbox;
- rejects files larger than 64 KiB;
- parses YAML frontmatter;
- extracts `id`, `type`, `sender`, `target`, and `created_at`;
- computes `sha256(content)`;
- classifies each request as one of:
  `design_review`, `documentation_review`, `status_summary`, `safety_review`,
  `needs_human`, or `invalid`;
- prints what it would do;
- writes no outbox response, no local state, no commit, and no push.

## Verification

Real inbox dry-run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 bridge/scripts/codex_inbox_reader.py --json
```

Result: completed successfully and reported all side effects as false:

```json
{
  "writes_files": false,
  "writes_outbox": false,
  "commits": false,
  "pushes": false
}
```

Test fixture in `/tmp/codex-reader-test` verified:

- a design-only request is classified as `design_review`;
- a risky request mentioning `systemd` and `git push` is classified as
  `needs_human`;
- a Markdown file without frontmatter is classified as `invalid`;
- no `codex_reader_state.json` is created.

## Boundaries Kept

Unchanged:

- `bridge_cycle.py`;
- systemd unit/timer;
- bridge task allowlist;
- runtime task processing;
- outbound sync rules;
- existing inbox/outbox messages;
- audit files.

No automatic timer or writer was added. This is only a local dry-run reader.
