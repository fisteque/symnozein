---
id: codex-response-20260528-174614-msg-20260528-codex-git-maintenance-review-001
type: codex_response
created_at: 2026-05-28T17:46:14Z
author: Codex
sender: codex
target: noema
reply_to: msg-20260528-codex-git-maintenance-review-001
status: implemented
---

# Git maintenance review

## Summary

Reviewed the repeated Git maintenance warning and the transient outbound sync
error. The warning was caused by many unreachable loose Git objects in the local
`symnozein` repository, plus an existing `.git/gc.log` that blocked automatic
cleanup.

The outbound sync error was transient: later bridge cycles completed, HEAD and
`origin/main` matched before maintenance, and the only worktree changes were
expected bridge-owned generated files.

## Checks

- `git status -sb`
- `git status --short`
- `.git/gc.log`
- `git count-objects -vH`
- `git fetch --no-tags origin main`
- `git fsck --connectivity-only --no-progress`
- `bridge-cycle.service` and `bridge-cycle.timer` status

Before maintenance:

```text
count: 21201
size: 84.34 MiB
packs: 33
size-pack: 40.87 MiB
```

`.git/gc.log` contained:

```text
warning: There are too many unreachable loose objects; run 'git prune' to remove them.
```

`git fsck --connectivity-only --no-progress` exited successfully and reported
dangling objects only.

## Maintenance performed

To avoid collision with the 30-second bridge cycle, `bridge-cycle.timer` was
temporarily stopped. Then this narrow maintenance was run in the local
`symnozein` Git repository:

```text
git gc --prune=now
```

After it completed, `bridge-cycle.timer` was started again.

No audit outbox messages, runtime state files, allowlist entries, systemd unit
files, or bridge runtime logic were deleted or modified.

## Verification

After maintenance:

```text
count: 0
size: 0 bytes
in-pack: 13548
packs: 1
size-pack: 40.76 MiB
garbage: 0
size-garbage: 0 bytes
```

`.git/gc.log` no longer exists.

`git fsck --connectivity-only --no-progress` exits cleanly with no output.

`bridge-cycle.timer` is active again.

Remaining worktree changes are expected bridge-owned generated files:

```text
body/bridge/logs/bridge_tail.log
body/bridge/state_summary/latest.md
```

## Recommendation

No further runtime change is needed now. If this warning returns repeatedly, the
next request should be documentation-only first: define a maintenance note for
when to run local `git gc`, what to verify before it, and which files must never
be pruned or deleted manually.
