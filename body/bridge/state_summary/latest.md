# Bridge State Summary

- Generated at: `2026-06-18T18:00:06.647933Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T17:59:57.952747+00:00`
- Heartbeat count: `127574`
- Heartbeat last gap seconds: `10.00556`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1278483`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `8.045886`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T18:00:05.998652+00:00`

## Body Health

- Health generated at: `2026-06-18T17:58:05.927459Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.14 / 0.14 / 0.05`
- RAM used percent: `14.45`
- Swap used percent: `0.0`
- Root disk used percent: `7.85`

## Bridge Sync

- Last inbound sync: `2026-06-18T17:59:56.643986Z`
- Last outbound sync: `2026-06-18T17:59:57.379338Z`
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
- Current pulse started: `2026-06-18T18:00:06.086465Z`
- Last body pulse: `2026-06-18T14:00:08.088542Z`
- Last pulse commit: `643cf456`
- Next scheduled pulse: `2026-06-19T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T18:00:05.998652Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T17:58:05.927459Z`; age seconds: `120`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `36081`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T17:59:57.379338Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T18:00:06.574265Z`; age seconds: `0`
