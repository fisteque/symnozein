# Bridge State Summary

- Generated at: `2026-07-07T06:00:00.642154Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-07T05:59:50.869806+00:00`
- Heartbeat count: `287076`
- Heartbeat last gap seconds: `10.006514`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2876877`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `7.675165`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-07T05:59:58.544986+00:00`

## Body Health

- Health generated at: `2026-07-07T05:57:18.381365Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.17 / 0.11 / 0.04`
- RAM used percent: `17.34`
- Swap used percent: `0.0`
- Root disk used percent: `8.14`

## Bridge Sync

- Last inbound sync: `2026-07-07T05:59:59.233713Z`
- Last outbound sync: `2026-07-07T06:00:00.010965Z`
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
- Current pulse started: `2026-07-07T06:00:00.120909Z`
- Last body pulse: `2026-07-07T02:00:11.350242Z`
- Last pulse commit: `9d295091`
- Next scheduled pulse: `2026-07-07T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-07T05:59:58.544986Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-07T05:57:18.381365Z`; age seconds: `162`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `553250`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-07T06:00:00.010965Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-07T06:00:00.585345Z`; age seconds: `0`
