# Bridge State Summary

- Generated at: `2026-06-26T02:00:09.636741Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-26T01:59:59.705809+00:00`
- Heartbeat count: `190793`
- Heartbeat last gap seconds: `10.006441`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1912086`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `7.656969`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-26T02:00:07.362793+00:00`

## Body Health

- Health generated at: `2026-06-26T01:53:36.714475Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.01 / 0.03 / 0.0`
- RAM used percent: `15.72`
- Swap used percent: `0.0`
- Root disk used percent: `7.99`

## Bridge Sync

- Last inbound sync: `2026-06-26T02:00:08.042887Z`
- Last outbound sync: `2026-06-26T02:00:09.008436Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

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
- Current pulse started: `2026-06-26T02:00:09.118375Z`
- Last body pulse: `2026-06-25T22:00:08.543301Z`
- Last pulse commit: `5ff996c6`
- Next scheduled pulse: `2026-06-26T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-26T02:00:07.362793Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-26T01:53:36.714475Z`; age seconds: `392`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `281719`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-26T02:00:09.008436Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-26T02:00:09.582703Z`; age seconds: `0`
