# Bridge State Summary

- Generated at: `2026-06-27T14:00:11.455965Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-27T14:00:10.846221+00:00`
- Heartbeat count: `203727`
- Heartbeat last gap seconds: `10.007717`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2041688`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `8.517336`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-27T14:00:09.355856+00:00`

## Body Health

- Health generated at: `2026-06-27T13:56:59.180796Z`
- CPU temperature C: `51.8`
- Load average 1m / 5m / 15m: `0.03 / 0.01 / 0.0`
- RAM used percent: `15.94`
- Swap used percent: `0.0`
- Root disk used percent: `7.99`

## Bridge Sync

- Last inbound sync: `2026-06-27T14:00:10.010939Z`
- Last outbound sync: `2026-06-27T14:00:10.814671Z`
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
- Current pulse started: `2026-06-27T14:00:10.931706Z`
- Last body pulse: `2026-06-27T10:00:06.016164Z`
- Last pulse commit: `20fb96e5`
- Next scheduled pulse: `2026-06-27T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-27T14:00:10.846221Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-27T13:56:59.180796Z`; age seconds: `192`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `411321`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-27T14:00:10.814671Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-27T14:00:11.400579Z`; age seconds: `0`
