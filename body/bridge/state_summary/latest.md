# Bridge State Summary

- Generated at: `2026-06-19T10:00:08.354833Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-19T10:00:03.034037+00:00`
- Heartbeat count: `133323`
- Heartbeat last gap seconds: `10.009694`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1336085`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.647842`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-19T10:00:07.681896+00:00`

## Body Health

- Health generated at: `2026-06-19T09:59:27.703791Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.42 / 0.27 / 0.11`
- RAM used percent: `14.63`
- Swap used percent: `0.0`
- Root disk used percent: `7.86`

## Bridge Sync

- Last inbound sync: `2026-06-19T09:59:48.312968Z`
- Last outbound sync: `2026-06-19T09:59:49.081739Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `0ee533b3`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260618-codex-diagnose-missing-sender-frontmatter-001`
- Last processed status: `pending_codex`
- Processed count: `20`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-19T10:00:07.775538Z`
- Last body pulse: `2026-06-19T06:00:09.144595Z`
- Last pulse commit: `e194e874`
- Next scheduled pulse: `2026-06-19T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-19T10:00:07.681896Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-19T09:59:27.703791Z`; age seconds: `40`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `93682`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-19T09:59:49.081739Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-19T10:00:08.300170Z`; age seconds: `0`
