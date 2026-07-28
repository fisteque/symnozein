# Bridge State Summary

- Generated at: `2026-07-28T14:00:08.700847Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-28T14:00:03.980019+00:00`
- Heartbeat count: `470986`
- Heartbeat last gap seconds: `10.004931`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4720085`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `3.958652`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-28T14:00:07.938688+00:00`

## Body Health

- Health generated at: `2026-07-28T13:52:57.370087Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.06 / 0.08 / 0.04`
- RAM used percent: `12.33`
- Swap used percent: `0.0`
- Root disk used percent: `8.9`

## Bridge Sync

- Last inbound sync: `2026-07-28T13:59:58.684056Z`
- Last outbound sync: `2026-07-28T13:59:59.564562Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1e23c9b6`
- Summary snapshot phase: `pre-outbound`

## Queues

- Bridge inbox pending: `0`
- Bridge runtime outbox awaiting publish/archive: `0`
- Oldest runtime outbox age seconds: `(none)`

- Codex runtime inbox files: `0`
- Active Codex pending: `0`
- Needs human count: `0`

- Last processed message: `msg-20260726-codex-read-runtime-bridge-state-001`
- Last bridge-agent status: `pending_codex (terminal handoff to Codex layer)`

- Last Codex worker request: `codex-request-20260726-171139-msg-20260726-codex-read-runtime-bridge-state-001`
- Last Codex worker status: `answered`

- Processed count: `28`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-07-28T14:00:08.049302Z`
- Last body pulse: `2026-07-28T10:00:10.136510Z`
- Last pulse commit: `4f1e24ed`
- Next scheduled pulse: `2026-07-28T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-28T14:00:07.938688Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-28T13:52:57.370087Z`; age seconds: `431`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `161309`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-28T13:59:59.564562Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-28T14:00:08.641872Z`; age seconds: `0`
