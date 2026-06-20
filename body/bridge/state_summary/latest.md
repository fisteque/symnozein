# Bridge State Summary

- Generated at: `2026-06-20T14:00:04.639951Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-20T13:59:57.235147+00:00`
- Heartbeat count: `143378`
- Heartbeat last gap seconds: `10.00826`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1436881`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `8.000939`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-20T13:59:55.227842+00:00`

## Body Health

- Health generated at: `2026-06-20T13:51:54.124135Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.73`
- Swap used percent: `0.0`
- Root disk used percent: `7.9`

## Bridge Sync

- Last inbound sync: `2026-06-20T13:59:55.905522Z`
- Last outbound sync: `2026-06-20T13:59:56.614821Z`
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
- Current pulse started: `2026-06-20T14:00:04.130257Z`
- Last body pulse: `2026-06-20T10:00:05.915578Z`
- Last pulse commit: `4d2f236e`
- Next scheduled pulse: `2026-06-20T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-20T13:59:57.235147Z`; age seconds: `7`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-20T13:51:54.124135Z`; age seconds: `490`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `194479`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-20T13:59:56.614821Z`; age seconds: `8`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-20T14:00:04.571295Z`; age seconds: `0`
