# Bridge State Summary

- Generated at: `2026-06-16T22:00:05.026569Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-16T21:59:57.355431+00:00`
- Heartbeat count: `111764`
- Heartbeat last gap seconds: `10.004428`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1120082`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `5.276629`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-16T22:00:02.632077+00:00`

## Body Health

- Health generated at: `2026-06-16T21:54:12.161262Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.23 / 0.05 / 0.02`
- RAM used percent: `14.02`
- Swap used percent: `0.0`
- Root disk used percent: `7.79`

## Bridge Sync

- Last inbound sync: `2026-06-16T22:00:03.313804Z`
- Last outbound sync: `2026-06-16T22:00:04.472155Z`
- Last outbound sync status: `error`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-16T22:00:04.591846Z`
- Last body pulse: `2026-06-16T10:00:04.318482Z`
- Last pulse commit: `30d4f9a1`
- Next scheduled pulse: `2026-06-17T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-16T22:00:02.632077Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-16T21:54:12.161262Z`; age seconds: `352`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `181600`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-16T22:00:04.472155Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-16T22:00:04.970525Z`; age seconds: `0`
