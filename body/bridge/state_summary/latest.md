# Bridge State Summary

- Generated at: `2026-06-18T08:00:45.504325Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T08:00:38.802484+00:00`
- Heartbeat count: `123986`
- Heartbeat last gap seconds: `10.006806`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1242522`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.91738`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T08:00:44.719881+00:00`

## Body Health

- Health generated at: `2026-06-18T07:57:14.131770Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.29`
- Swap used percent: `0.0`
- Root disk used percent: `7.84`

## Bridge Sync

- Last inbound sync: `2026-06-18T08:00:45.344467Z`
- Last outbound sync: `2026-06-18T08:00:16.038452Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `067af326`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260618-codex-diagnose-missing-sender-frontmatter-001`
- Last processed status: `pending_codex`
- Processed count: `20`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-18T06:00:06.418172Z`
- Last pulse commit: `1aa8d8b9`
- Next scheduled pulse: `Thu 2026-06-18 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T08:00:44.719881Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T07:57:14.131770Z`; age seconds: `211`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `120`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T08:00:45.344467Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T06:00:06.418172Z`; age seconds: `7239`
