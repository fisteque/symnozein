# Bridge State Summary

- Generated at: `2026-06-20T22:00:06.444144Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-20T21:59:59.702813+00:00`
- Heartbeat count: `146254`
- Heartbeat last gap seconds: `10.005287`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1465683`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `6.137178`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-20T22:00:05.840006+00:00`

## Body Health

- Health generated at: `2026-06-20T21:52:35.315820Z`
- CPU temperature C: `47.95`
- Load average 1m / 5m / 15m: `0.32 / 0.2 / 0.07`
- RAM used percent: `14.61`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-20T21:59:44.705483Z`
- Last outbound sync: `2026-06-20T21:59:45.510190Z`
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
- Current pulse started: `2026-06-20T22:00:05.941784Z`
- Last body pulse: `2026-06-20T18:00:07.045668Z`
- Last pulse commit: `8bb1ab16`
- Next scheduled pulse: `2026-06-21T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-20T22:00:05.840006Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-20T21:52:35.315820Z`; age seconds: `451`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `223281`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-20T21:59:45.510190Z`; age seconds: `20`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-20T22:00:06.391433Z`; age seconds: `0`
