# Bridge State Summary

- Generated at: `2026-06-27T10:00:04.653871Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-27T09:59:57.119365+00:00`
- Heartbeat count: `202289`
- Heartbeat last gap seconds: `10.006547`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2027281`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `9.833516`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-27T09:59:56.946350+00:00`

## Body Health

- Health generated at: `2026-06-27T09:56:36.772403Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.02`
- Swap used percent: `0.0`
- Root disk used percent: `8.0`

## Bridge Sync

- Last inbound sync: `2026-06-27T09:59:47.573718Z`
- Last outbound sync: `2026-06-27T09:59:48.330829Z`
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
- Current pulse started: `2026-06-27T10:00:04.135048Z`
- Last body pulse: `2026-06-27T06:00:05.936082Z`
- Last pulse commit: `9940b594`
- Next scheduled pulse: `2026-06-27T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-27T09:59:57.119365Z`; age seconds: `7`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-27T09:56:36.772403Z`; age seconds: `207`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `396914`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-27T09:59:48.330829Z`; age seconds: `16`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-27T10:00:04.599072Z`; age seconds: `0`
