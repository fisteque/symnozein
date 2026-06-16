# Bridge State Summary

- Generated at: `2026-06-16T02:00:04.625045Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-16T02:00:00.317244+00:00`
- Heartbeat count: `104580`
- Heartbeat last gap seconds: `10.006952`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1048081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `9.646598`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-16T01:59:59.956906+00:00`

## Body Health

- Health generated at: `2026-06-16T01:52:29.358175Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `13.78`
- Swap used percent: `0.0`
- Root disk used percent: `7.77`

## Bridge Sync

- Last inbound sync: `2026-06-16T01:59:50.523205Z`
- Last outbound sync: `2026-06-16T01:59:51.225933Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-16T02:00:04.124445Z`
- Last body pulse: `2026-06-15T22:00:12.387483Z`
- Last pulse commit: `59777636`
- Next scheduled pulse: `2026-06-16T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-16T02:00:00.317244Z`; age seconds: `4`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-16T01:52:29.358175Z`; age seconds: `455`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `109600`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-16T01:59:51.225933Z`; age seconds: `13`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-16T02:00:04.571902Z`; age seconds: `0`
