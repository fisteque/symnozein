# Bridge State Summary

- Generated at: `2026-06-21T02:00:07.854740Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-21T02:00:01.002739+00:00`
- Heartbeat count: `147691`
- Heartbeat last gap seconds: `10.003979`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1480084`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `4.872566`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-21T02:00:05.875322+00:00`

## Body Health

- Health generated at: `2026-06-21T01:52:55.401607Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.05 / 0.02 / 0.0`
- RAM used percent: `14.95`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-21T02:00:06.532134Z`
- Last outbound sync: `2026-06-21T02:00:07.273766Z`
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
- Current pulse started: `2026-06-21T02:00:07.380315Z`
- Last body pulse: `2026-06-20T22:00:07.800689Z`
- Last pulse commit: `01541f00`
- Next scheduled pulse: `2026-06-21T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-21T02:00:05.875322Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-21T01:52:55.401607Z`; age seconds: `432`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `237682`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-21T02:00:07.273766Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-21T02:00:07.799003Z`; age seconds: `0`
