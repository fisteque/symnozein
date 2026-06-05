# PC-Codex Postman Quick Rule

Deliver exactly one new message file to:

`body/bridge/inbox/messages/codex/`

## Before

- `git fetch` / ff-only to `origin/main`.
- Verify clean checkout.
- Verify target file does not exist.

## During

- Create one `.md` only.
- Fill real UTC `created_at`.
- Fix only envelope issues: YAML, closing `---`, timestamp.
- Do not change message meaning.

## Commit

- Stage only that one new inbox file.
- No index/diff/generated files.
- No outbox/state_summary/scripts/logs/runtime changes.
- Commit and push.

## After

- Report path, `created_at`, commit hash, scope, clean/dirty status.

## Stop If

- Unclear target.
- File exists.
- Dirty checkout outside expected file.
- Conflict.
- Push/rebase unclear.
- Request asks PC-Codex to implement instead of deliver.
