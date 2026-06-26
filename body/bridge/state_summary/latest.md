# Bridge State Summary

- Generated at: `2026-06-26T14:00:04.931982Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-26T13:59:59.504292+00:00`
- Heartbeat count: `195104`
- Heartbeat last gap seconds: `10.010074`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1955282`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.775157`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-26T14:00:04.279465+00:00`

## Body Health

- Health generated at: `2026-06-26T13:54:43.844846Z`
- CPU temperature C: `52.35`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `15.73`
- Swap used percent: `0.0`
- Root disk used percent: `7.99`

## Bridge Sync

- Last inbound sync: `2026-06-26T13:59:54.894570Z`
- Last outbound sync: `2026-06-26T13:59:55.673794Z`
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
- Current pulse started: `2026-06-26T14:00:04.379273Z`
- Last body pulse: `2026-06-26T10:00:05.275590Z`
- Last pulse commit: `b92915c9`
- Next scheduled pulse: `2026-06-26T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-26T14:00:04.279465Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-26T13:54:43.844846Z`; age seconds: `321`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `324914`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-26T13:59:55.673794Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-26T14:00:04.873564Z`; age seconds: `0`
