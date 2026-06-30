# Bridge State Summary

- Generated at: `2026-06-30T18:00:08.655759Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T18:00:00.766285+00:00`
- Heartbeat count: `231033`
- Heartbeat last gap seconds: `10.009146`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2315285`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `5.80056`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T18:00:06.566861+00:00`

## Body Health

- Health generated at: `2026-06-30T17:53:36.073541Z`
- CPU temperature C: `51.8`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.02`
- RAM used percent: `16.15`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T18:00:07.259307Z`
- Last outbound sync: `2026-06-30T18:00:08.059027Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `79fb17a5`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-30T18:00:08.164067Z`
- Last body pulse: `2026-06-30T14:00:10.096443Z`
- Last pulse commit: `db5f03d9`
- Next scheduled pulse: `2026-07-01T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T18:00:06.566861Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T17:53:36.073541Z`; age seconds: `392`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `684918`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T18:00:08.059027Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T18:00:08.601085Z`; age seconds: `0`
