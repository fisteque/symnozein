# Bridge State Summary

- Generated at: `2026-06-30T14:00:08.213658Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T13:59:59.858006+00:00`
- Heartbeat count: `229596`
- Heartbeat last gap seconds: `10.007527`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2300885`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `6.302078`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T14:00:06.160102+00:00`

## Body Health

- Health generated at: `2026-06-30T13:53:15.667875Z`
- CPU temperature C: `51.25`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.3`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T14:00:06.820543Z`
- Last outbound sync: `2026-06-30T14:00:07.568386Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `79fb17a5`

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
- Current pulse started: `2026-06-30T14:00:07.698670Z`
- Last body pulse: `2026-06-30T10:00:07.034464Z`
- Last pulse commit: `9db7eb98`
- Next scheduled pulse: `2026-06-30T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T14:00:06.160102Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T13:53:15.667875Z`; age seconds: `412`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `670518`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T14:00:07.568386Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T14:00:08.159493Z`; age seconds: `0`
