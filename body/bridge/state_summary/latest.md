# Bridge State Summary

- Generated at: `2026-07-03T14:00:01.682253Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-03T13:59:54.053470+00:00`
- Heartbeat count: `255462`
- Heartbeat last gap seconds: `10.00779`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2560078`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.962627`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-03T14:00:01.016111+00:00`

## Body Health

- Health generated at: `2026-07-03T13:59:31.074432Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.47 / 0.19 / 0.11`
- RAM used percent: `16.66`
- Swap used percent: `0.0`
- Root disk used percent: `8.11`

## Bridge Sync

- Last inbound sync: `2026-07-03T13:59:51.679451Z`
- Last outbound sync: `2026-07-03T13:59:52.445304Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

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
- Current pulse started: `2026-07-03T14:00:01.103519Z`
- Last body pulse: `2026-07-03T10:00:10.138923Z`
- Last pulse commit: `5734ddff`
- Next scheduled pulse: `2026-07-03T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-03T14:00:01.016111Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-03T13:59:31.074432Z`; age seconds: `30`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `236451`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-03T13:59:52.445304Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-03T14:00:01.628949Z`; age seconds: `0`
