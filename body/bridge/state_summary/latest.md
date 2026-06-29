# Bridge State Summary

- Generated at: `2026-06-29T02:00:07.340057Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-29T01:59:59.079579+00:00`
- Heartbeat count: `216659`
- Heartbeat last gap seconds: `10.007234`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2171284`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.633602`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-29T02:00:06.713198+00:00`

## Body Health

- Health generated at: `2026-06-29T01:50:16.072678Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.25`
- Swap used percent: `0.0`
- Root disk used percent: `8.01`

## Bridge Sync

- Last inbound sync: `2026-06-29T01:59:47.413054Z`
- Last outbound sync: `2026-06-29T01:59:48.148523Z`
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
- Current pulse started: `2026-06-29T02:00:06.813781Z`
- Last body pulse: `2026-06-28T22:00:06.004403Z`
- Last pulse commit: `8d95bf8d`
- Next scheduled pulse: `2026-06-29T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-29T02:00:06.713198Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-29T01:50:16.072678Z`; age seconds: `591`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `540917`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-29T01:59:48.148523Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-29T02:00:07.287833Z`; age seconds: `0`
