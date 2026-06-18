# Bridge State Summary

- Generated at: `2026-06-18T14:00:06.549535Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T13:59:56.581647+00:00`
- Heartbeat count: `126138`
- Heartbeat last gap seconds: `10.006454`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1264083`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `9.328172`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T14:00:05.909834+00:00`

## Body Health

- Health generated at: `2026-06-18T13:57:45.825022Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.01`
- RAM used percent: `14.36`
- Swap used percent: `0.0`
- Root disk used percent: `7.85`

## Bridge Sync

- Last inbound sync: `2026-06-18T13:59:46.528123Z`
- Last outbound sync: `2026-06-18T13:59:47.266103Z`
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
- Current pulse started: `2026-06-18T14:00:06.003624Z`
- Last body pulse: `2026-06-18T10:00:08.507995Z`
- Last pulse commit: `1ab68475`
- Next scheduled pulse: `2026-06-18T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T14:00:05.909834Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T13:57:45.825022Z`; age seconds: `140`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `21681`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T13:59:47.266103Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T14:00:06.494825Z`; age seconds: `0`
