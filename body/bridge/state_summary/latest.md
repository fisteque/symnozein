# Bridge State Summary

- Generated at: `2026-06-19T02:00:04.644569Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-19T02:00:00.557777+00:00`
- Heartbeat count: `130448`
- Heartbeat last gap seconds: `10.007568`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1307281`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `6.291653`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-19T01:59:56.841877+00:00`

## Body Health

- Health generated at: `2026-06-19T01:58:46.815947Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.37`
- Swap used percent: `0.0`
- Root disk used percent: `7.86`

## Bridge Sync

- Last inbound sync: `2026-06-19T01:59:37.368231Z`
- Last outbound sync: `2026-06-19T01:59:38.133309Z`
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
- Current pulse started: `2026-06-19T02:00:04.125318Z`
- Last body pulse: `2026-06-18T22:00:09.507426Z`
- Last pulse commit: `3a94d51e`
- Next scheduled pulse: `2026-06-19T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-19T02:00:00.557777Z`; age seconds: `4`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-19T01:58:46.815947Z`; age seconds: `77`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `64879`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-19T01:59:38.133309Z`; age seconds: `26`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-19T02:00:04.591797Z`; age seconds: `0`
