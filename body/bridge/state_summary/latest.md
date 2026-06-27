# Bridge State Summary

- Generated at: `2026-06-27T18:00:04.262633Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-27T18:00:03.887471+00:00`
- Heartbeat count: `205164`
- Heartbeat last gap seconds: `10.006955`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2056081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `8.031116`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-27T18:00:01.911648+00:00`

## Body Health

- Health generated at: `2026-06-27T17:57:21.785130Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.21 / 0.11 / 0.04`
- RAM used percent: `16.03`
- Swap used percent: `0.0`
- Root disk used percent: `8.0`

## Bridge Sync

- Last inbound sync: `2026-06-27T18:00:02.704010Z`
- Last outbound sync: `2026-06-27T18:00:03.553629Z`
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
- Current pulse started: `2026-06-27T18:00:03.661754Z`
- Last body pulse: `2026-06-27T14:00:12.738328Z`
- Last pulse commit: `e205480b`
- Next scheduled pulse: `2026-06-28T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-27T18:00:03.887471Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-27T17:57:21.785130Z`; age seconds: `162`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `425714`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-27T18:00:03.553629Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-27T18:00:04.209494Z`; age seconds: `0`
