# Bridge State Summary

- Generated at: `2026-06-18T06:00:05.078641Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T06:00:02.961165+00:00`
- Heartbeat count: `123263`
- Heartbeat last gap seconds: `10.0044`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1235282`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.575905`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T06:00:04.537087+00:00`

## Body Health

- Health generated at: `2026-06-18T05:57:04.117180Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.23`
- Swap used percent: `0.0`
- Root disk used percent: `7.84`

## Bridge Sync

- Last inbound sync: `2026-06-18T05:59:55.158277Z`
- Last outbound sync: `2026-06-18T05:59:55.856137Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `067af326`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-root-web-check-001`
- Last processed status: `pending_codex`
- Processed count: `19`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-18T06:00:04.630771Z`
- Last body pulse: `2026-06-18T02:00:05.801135Z`
- Last pulse commit: `390b0b2d`
- Next scheduled pulse: `2026-06-18T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T06:00:04.537087Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T05:57:04.117180Z`; age seconds: `180`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T17:17:39.057579Z`; age seconds: `45746`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T05:59:55.856137Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T06:00:05.026002Z`; age seconds: `0`
