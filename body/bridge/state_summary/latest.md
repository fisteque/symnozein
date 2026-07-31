# Bridge State Summary

- Generated at: `2026-07-31T06:00:04.226605Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-31T05:59:56.207124+00:00`
- Heartbeat count: `493973`
- Heartbeat last gap seconds: `10.006895`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4950481`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `5.391411`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-31T06:00:01.598549+00:00`

## Body Health

- Health generated at: `2026-07-31T05:58:41.566216Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.04 / 0.08 / 0.08`
- RAM used percent: `13.11`
- Swap used percent: `0.0`
- Root disk used percent: `9.47`

## Bridge Sync

- Last inbound sync: `2026-07-31T06:00:02.657393Z`
- Last outbound sync: `2026-07-31T06:00:03.502920Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `992a0618`
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
- Current pulse started: `2026-07-31T06:00:03.664843Z`
- Last body pulse: `2026-07-31T02:00:05.093214Z`
- Last pulse commit: `e9cf1d4d`
- Next scheduled pulse: `2026-07-31T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-31T06:00:01.598549Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-31T05:58:41.566216Z`; age seconds: `82`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `391705`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-31T06:00:03.502920Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-31T06:00:04.171954Z`; age seconds: `0`
