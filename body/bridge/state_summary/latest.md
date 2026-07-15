# Bridge State Summary

- Generated at: `2026-07-15T06:00:04.670133Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-15T06:00:03.536955+00:00`
- Heartbeat count: `356052`
- Heartbeat last gap seconds: `10.009065`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3568081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `5.520193`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-15T05:59:59.048097+00:00`

## Body Health

- Health generated at: `2026-07-15T05:54:18.716361Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `18.81`
- Swap used percent: `0.0`
- Root disk used percent: `8.34`

## Bridge Sync

- Last inbound sync: `2026-07-15T05:59:49.706959Z`
- Last outbound sync: `2026-07-15T05:59:50.489487Z`
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
- Current pulse started: `2026-07-15T06:00:04.123469Z`
- Last body pulse: `2026-07-15T02:00:13.087988Z`
- Last pulse commit: `1f45e84c`
- Next scheduled pulse: `2026-07-15T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-15T06:00:03.536955Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-15T05:54:18.716361Z`; age seconds: `345`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1244454`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-15T05:59:50.489487Z`; age seconds: `14`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-15T06:00:04.614107Z`; age seconds: `0`
