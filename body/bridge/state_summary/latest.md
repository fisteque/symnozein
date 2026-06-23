# Bridge State Summary

- Generated at: `2026-06-23T06:00:05.598048Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-23T06:00:02.648947+00:00`
- Heartbeat count: `166363`
- Heartbeat last gap seconds: `10.052184`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1667282`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `0.725806`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-23T06:00:03.374771+00:00`

## Body Health

- Health generated at: `2026-06-23T05:57:23.220550Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.03`
- RAM used percent: `15.41`
- Swap used percent: `0.0`
- Root disk used percent: `7.93`

## Bridge Sync

- Last inbound sync: `2026-06-23T06:00:04.197838Z`
- Last outbound sync: `2026-06-23T06:00:04.953561Z`
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
- Current pulse started: `2026-06-23T06:00:05.060242Z`
- Last body pulse: `2026-06-23T02:00:04.217810Z`
- Last pulse commit: `70d92ceb`
- Next scheduled pulse: `2026-06-23T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-23T06:00:03.374771Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-23T05:57:23.220550Z`; age seconds: `162`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `36915`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-23T06:00:04.953561Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-23T06:00:05.543466Z`; age seconds: `0`
