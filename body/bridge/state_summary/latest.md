# Bridge State Summary

- Generated at: `2026-07-26T18:16:14.899802Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T18:16:14.627582+00:00`
- Heartbeat count: `455282`
- Heartbeat last gap seconds: `10.004097`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4562651`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `9.402294`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T18:16:14.025793+00:00`

## Body Health

- Health generated at: `2026-07-26T18:09:03.380737Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.08 / 0.05 / 0.01`
- RAM used percent: `11.87`
- Swap used percent: `0.0`
- Root disk used percent: `8.87`

## Bridge Sync

- Last inbound sync: `2026-07-26T18:16:14.728486Z`
- Last outbound sync: `2026-07-26T18:15:45.590303Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `7a763fd5`
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

- Current pulse status: `idle`
- Last body pulse: `2026-07-26T18:00:04.718542Z`
- Last pulse commit: `4566eb83`
- Next scheduled pulse: `Mon 2026-07-27 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T18:16:14.627582Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T18:09:03.380737Z`; age seconds: `431`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `3875`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T18:16:14.728486Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T18:00:04.718542Z`; age seconds: `970`
