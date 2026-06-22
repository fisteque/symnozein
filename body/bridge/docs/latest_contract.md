# Latest Summary Contract

`body/bridge/state_summary/latest.md` is the public bridge status panel. It is
not an archive, log dump, debug trace, or complete runtime export.

## Purpose

`latest.md` should answer: what is the body and bridge status right now, and are
the main queues and pulses healthy enough to orient a reader?

It should stay short, stable, and safe to publish.

## Allowed Sections

The active summary shape is:

```text
Bridge State Summary
Body Heartbeat
Body Health
Bridge Sync
Queues
Pulse
Source Freshness
```

New sections should be added only when they are public, compact, and useful for
routine orientation.

## Do Not Include

Do not publish these through `latest.md`:

- raw runtime JSON dumps;
- bridge log tails;
- full inbox or outbox message bodies;
- locks, secrets, tokens, credentials, private IPs, or environment data;
- local incident details beyond compact public status;
- historical ledgers or diffs;
- detailed debug output that belongs in local logs.

## Where Other Information Belongs

- History and implementation rationale belong in
  `body/bridge/docs/implementation_ledger.md`.
- Operational limits belong in `body/bridge/docs/known_limits.md`.
- Script behavior belongs in `body/bridge/docs/bridge_scripts.md`.
- Runtime evidence stays in local state, logs, incidents, processed archives, or
  outbox messages.
