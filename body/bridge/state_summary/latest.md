# Bridge State Summary

- Generated at: `2026-07-05T22:00:00.928338Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-05T22:00:00.800017+00:00`
- Heartbeat count: `275582`
- Heartbeat last gap seconds: `10.005111`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2761678`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `7.837554`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-05T21:59:58.632477+00:00`

## Body Health

- Health generated at: `2026-07-05T21:54:38.209155Z`
- CPU temperature C: `47.95`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.82`
- Swap used percent: `0.0`
- Root disk used percent: `8.13`

## Bridge Sync

- Last inbound sync: `2026-07-05T21:59:59.304822Z`
- Last outbound sync: `2026-07-05T22:00:00.052135Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-07-05T22:00:00.186162Z`
- Last body pulse: `2026-07-05T18:00:08.551452Z`
- Last pulse commit: `fde11bac`
- Next scheduled pulse: `2026-07-06T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-05T22:00:00.800017Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-05T21:54:38.209155Z`; age seconds: `322`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `438051`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-05T22:00:00.052135Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-05T22:00:00.874683Z`; age seconds: `0`
