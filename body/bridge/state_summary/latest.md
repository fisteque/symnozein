# Bridge State Summary

- Generated at: `2026-07-29T02:00:03.164896Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-29T02:00:02.935023+00:00`
- Heartbeat count: `475296`
- Heartbeat last gap seconds: `10.007761`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4763280`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `7.709475`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-29T02:00:00.636752+00:00`

## Body Health

- Health generated at: `2026-07-29T01:54:00.219870Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.1 / 0.03 / 0.01`
- RAM used percent: `12.39`
- Swap used percent: `0.0`
- Root disk used percent: `8.9`

## Bridge Sync

- Last inbound sync: `2026-07-29T02:00:01.601198Z`
- Last outbound sync: `2026-07-29T02:00:02.485615Z`
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
- Current pulse started: `2026-07-29T02:00:02.597124Z`
- Last body pulse: `2026-07-28T22:00:12.223546Z`
- Last pulse commit: `ae9e70de`
- Next scheduled pulse: `2026-07-29T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-29T02:00:02.935023Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-29T01:54:00.219870Z`; age seconds: `362`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `204504`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-29T02:00:02.485615Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-29T02:00:03.107812Z`; age seconds: `0`
