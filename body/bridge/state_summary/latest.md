# Bridge State Summary

- Generated at: `2026-07-11T02:00:06.076327Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-11T02:00:01.378947+00:00`
- Heartbeat count: `320125`
- Heartbeat last gap seconds: `10.00857`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3208083`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `4.092734`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-11T02:00:05.471696+00:00`

## Body Health

- Health generated at: `2026-07-11T01:55:35.138884Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.02 / 0.02 / 0.0`
- RAM used percent: `17.86`
- Swap used percent: `0.0`
- Root disk used percent: `8.23`

## Bridge Sync

- Last inbound sync: `2026-07-11T01:59:46.126985Z`
- Last outbound sync: `2026-07-11T01:59:46.921919Z`
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
- Current pulse started: `2026-07-11T02:00:05.563126Z`
- Last body pulse: `2026-07-10T22:00:07.095847Z`
- Last pulse commit: `741c6fc1`
- Next scheduled pulse: `2026-07-11T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-11T02:00:05.471696Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-11T01:55:35.138884Z`; age seconds: `270`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `884456`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-11T01:59:46.921919Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-11T02:00:06.023184Z`; age seconds: `0`
