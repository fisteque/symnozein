# Bridge State Summary

- Generated at: `2026-06-23T10:00:06.790272Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-23T10:00:04.928981+00:00`
- Heartbeat count: `167802`
- Heartbeat last gap seconds: `10.058568`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1681683`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `9.900067`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-23T10:00:04.770496+00:00`

## Body Health

- Health generated at: `2026-06-23T09:57:44.135474Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.05`
- RAM used percent: `15.2`
- Swap used percent: `0.0`
- Root disk used percent: `7.94`

## Bridge Sync

- Last inbound sync: `2026-06-23T10:00:05.457724Z`
- Last outbound sync: `2026-06-23T10:00:06.198535Z`
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
- Current pulse started: `2026-06-23T10:00:06.301142Z`
- Last body pulse: `2026-06-23T06:00:07.084632Z`
- Last pulse commit: `0d312386`
- Next scheduled pulse: `2026-06-23T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-23T10:00:04.928981Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-23T09:57:44.135474Z`; age seconds: `142`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `51316`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-23T10:00:06.198535Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-23T10:00:06.734978Z`; age seconds: `0`
