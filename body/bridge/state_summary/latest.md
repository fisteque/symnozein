# Bridge State Summary

- Generated at: `2026-06-27T02:00:04.020915Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-27T01:59:59.752606+00:00`
- Heartbeat count: `199415`
- Heartbeat last gap seconds: `10.004295`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1998481`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `1.846982`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-27T02:00:01.599604+00:00`

## Body Health

- Health generated at: `2026-06-27T01:55:51.252594Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.09 / 0.1 / 0.03`
- RAM used percent: `15.82`
- Swap used percent: `0.0`
- Root disk used percent: `8.0`

## Bridge Sync

- Last inbound sync: `2026-06-27T02:00:02.494255Z`
- Last outbound sync: `2026-06-27T02:00:03.405672Z`
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
- Current pulse started: `2026-06-27T02:00:03.514172Z`
- Last body pulse: `2026-06-26T22:00:11.572716Z`
- Last pulse commit: `72b438c1`
- Next scheduled pulse: `2026-06-27T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-27T02:00:01.599604Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-27T01:55:51.252594Z`; age seconds: `252`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `368114`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-27T02:00:03.405672Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-27T02:00:03.966973Z`; age seconds: `0`
