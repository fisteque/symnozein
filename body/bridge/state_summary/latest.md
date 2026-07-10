# Bridge State Summary

- Generated at: `2026-07-10T22:00:05.666521Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-10T21:59:58.067177+00:00`
- Heartbeat count: `318688`
- Heartbeat last gap seconds: `10.007342`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3193682`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `5.301756`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-10T22:00:03.368948+00:00`

## Body Health

- Health generated at: `2026-07-10T21:55:13.016674Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.0 / 0.04 / 0.07`
- RAM used percent: `18.1`
- Swap used percent: `0.0`
- Root disk used percent: `8.22`

## Bridge Sync

- Last inbound sync: `2026-07-10T22:00:04.118135Z`
- Last outbound sync: `2026-07-10T22:00:05.022207Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-07-10T22:00:05.153059Z`
- Last body pulse: `2026-07-10T18:00:02.768266Z`
- Last pulse commit: `f57d1130`
- Next scheduled pulse: `2026-07-11T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-10T22:00:03.368948Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-10T21:55:13.016674Z`; age seconds: `292`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `870055`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-10T22:00:05.022207Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-10T22:00:05.612806Z`; age seconds: `0`
