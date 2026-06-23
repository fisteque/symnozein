# Bridge State Summary

- Generated at: `2026-06-23T14:00:06.316633Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-23T13:59:56.480222+00:00`
- Heartbeat count: `169238`
- Heartbeat last gap seconds: `10.005189`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1696083`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `9.20619`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-23T14:00:05.686426+00:00`

## Body Health

- Health generated at: `2026-06-23T13:58:05.641821Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.05 / 0.15 / 0.12`
- RAM used percent: `15.42`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-23T13:59:40.684944Z`
- Last outbound sync: `2026-06-23T13:59:41.448198Z`
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
- Current pulse started: `2026-06-23T14:00:05.783421Z`
- Last body pulse: `2026-06-23T10:00:08.091825Z`
- Last pulse commit: `2fbeec1a`
- Next scheduled pulse: `2026-06-23T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-23T14:00:05.686426Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-23T13:58:05.641821Z`; age seconds: `120`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `65716`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-23T13:59:41.448198Z`; age seconds: `24`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-23T14:00:06.264155Z`; age seconds: `0`
