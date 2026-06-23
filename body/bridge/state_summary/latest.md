# Bridge State Summary

- Generated at: `2026-06-23T02:00:02.513035Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-23T02:00:00.607624+00:00`
- Heartbeat count: `164926`
- Heartbeat last gap seconds: `10.006431`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1652879`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `0.884872`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-23T02:00:01.492513+00:00`

## Body Health

- Health generated at: `2026-06-23T01:57:01.281837Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.0 / 0.02 / 0.06`
- RAM used percent: `15.39`
- Swap used percent: `0.0`
- Root disk used percent: `7.93`

## Bridge Sync

- Last inbound sync: `2026-06-23T01:59:42.418620Z`
- Last outbound sync: `2026-06-23T01:59:43.149182Z`
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
- Current pulse started: `2026-06-23T02:00:01.585459Z`
- Last body pulse: `2026-06-22T22:00:03.387615Z`
- Last pulse commit: `9ee979f3`
- Next scheduled pulse: `2026-06-23T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-23T02:00:01.492513Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-23T01:57:01.281837Z`; age seconds: `181`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `22512`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-23T01:59:43.149182Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-23T02:00:02.439492Z`; age seconds: `0`
