# Bridge State Summary

- Generated at: `2026-06-18T22:00:08.178600Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T21:59:59.109086+00:00`
- Heartbeat count: `129012`
- Heartbeat last gap seconds: `10.004912`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1292885`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `7.122459`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T22:00:06.231561+00:00`

## Body Health

- Health generated at: `2026-06-18T21:58:26.172594Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.04 / 0.01 / 0.0`
- RAM used percent: `14.37`
- Swap used percent: `0.0`
- Root disk used percent: `7.86`

## Bridge Sync

- Last inbound sync: `2026-06-18T22:00:06.867876Z`
- Last outbound sync: `2026-06-18T22:00:07.587213Z`
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
- Current pulse started: `2026-06-18T22:00:07.703906Z`
- Last body pulse: `2026-06-18T18:00:08.168326Z`
- Last pulse commit: `7b6c0ceb`
- Next scheduled pulse: `2026-06-19T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T22:00:06.231561Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T21:58:26.172594Z`; age seconds: `102`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `50482`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T22:00:07.587213Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T22:00:08.123977Z`; age seconds: `0`
