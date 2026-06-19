# Bridge State Summary

- Generated at: `2026-06-19T14:00:08.617801Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-19T14:00:04.586468+00:00`
- Heartbeat count: `134760`
- Heartbeat last gap seconds: `10.00777`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1350485`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `3.376279`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-19T14:00:07.962764+00:00`

## Body Health

- Health generated at: `2026-06-19T13:59:48.033416Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.0 / 0.07 / 0.04`
- RAM used percent: `14.62`
- Swap used percent: `0.0`
- Root disk used percent: `7.87`

## Bridge Sync

- Last inbound sync: `2026-06-19T13:59:58.655392Z`
- Last outbound sync: `2026-06-19T13:59:59.427357Z`
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
- Current pulse started: `2026-06-19T14:00:08.064486Z`
- Last body pulse: `2026-06-19T10:00:09.703325Z`
- Last pulse commit: `759b5ab6`
- Next scheduled pulse: `2026-06-19T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-19T14:00:07.962764Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-19T13:59:48.033416Z`; age seconds: `20`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `108083`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-19T13:59:59.427357Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-19T14:00:08.559328Z`; age seconds: `0`
