---
type: codex_response
created_at: 2026-06-05T12:03:22Z
sender: RPi5-bridge
target: codex
reply_to: msg-20260605-codex-bridge-cycle-lock-audit-001
status: done
task_class: audit
---

# Bridge cycle lock audit

Ignore note respected: the final postman/commit instruction from the inbound envelope was ignored.

## Findings

1. Lock creation and release are implemented in `bridge/scripts/bridge_cycle_lock.py`.
   `bridge/scripts/bridge_cycle.py` enters it with `bridge_cycle_lock(runtime_root, ttl_seconds=args.lock_ttl_seconds)`.

2. Current lock TTL is 900 seconds, i.e. 15 minutes.
   This comes from `DEFAULT_LOCK_TTL_SECONDS = 15 * 60`. It can be overridden by `--lock-ttl-seconds`.

3. The lock file normally does not disappear after a successful cycle.
   Successful release rewrites `bridge/state/bridge_cycle.lock.json` with `status: released` and `expires_at` set to the release time. Current observed lock file was in released state, not active.

4. At the error time, the evidence points to a previous cycle still holding an active lock or to a stale lock left by a cycle that died after acquiring it.
   Logs show:
   - `2026-06-05T05:49:49.332Z`: lock acquired.
   - immediately after: `== inbound sync ==`.
   - no matching completion/release log for that same run in the inspected log section.
   - `2026-06-05T05:50:19.386Z`: next timer tick failed because the lock was still active until `2026-06-05T06:04:49.331813Z`.

5. The error repeated because the bridge timer kept firing while the 15-minute lock TTL was still active.
   `bridge/state/cycle_error_state.json` recorded:
   - first seen: `2026-06-05T05:50:19.405306Z`
   - last seen: `2026-06-05T06:04:20.505500Z`
   - repeat count: 29
   - cleared at: `2026-06-05T06:04:52.961705Z`
   This matches a roughly 30-second timer cadence until lock expiry.

6. After lock expiry, the bridge recovered and ran normally.
   Logs show a later cycle acquiring the lock at `2026-06-05T06:05:50Z` and completing at `2026-06-05T06:05:51Z`. Subsequent cycles also continued normally. Git history also shows `Sync RPi bridge outbound state` around the recovery window.

7. Exact root cause of the original stuck cycle is not proven by current logs.
   The strongest clue is that it stopped after entering inbound sync. Plausible causes are a blocked or slow git/network operation, a process killed after lock acquisition but before release, or another subprocess stall. The repeated lock errors themselves are expected behavior once that active lock exists.

## Recommendation

No immediate code change is required if this remains a one-off event.

Minimal safe future fix, not applied:
- Add richer lock metadata: current step, pid, created_at, and last progress timestamp.
- On lock conflict, check whether the recorded pid is still alive.
- If pid is dead and the lock is older than a small grace period, classify it as stale and take over or release it.
- Keep emitting a single deduplicated outbox error while repeating internally, as current `cycle_error_state` already does.

This would make the next incident distinguishable as either "active long-running cycle" or "stale lock from dead process".
