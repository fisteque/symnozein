# Bridge State Summary

- Generated at: `2026-07-28T18:00:11.292069Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-28T18:00:06.039278+00:00`
- Heartbeat count: `472423`
- Heartbeat last gap seconds: `10.007713`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4734488`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `2.866654`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-28T18:00:08.905948+00:00`

## Body Health

- Health generated at: `2026-07-28T17:53:18.444679Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.07 / 0.14 / 0.09`
- RAM used percent: `12.39`
- Swap used percent: `0.0`
- Root disk used percent: `8.9`

## Bridge Sync

- Last inbound sync: `2026-07-28T18:00:09.742277Z`
- Last outbound sync: `2026-07-28T18:00:10.555028Z`
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
- Current pulse started: `2026-07-28T18:00:10.668417Z`
- Last body pulse: `2026-07-28T14:00:10.445770Z`
- Last pulse commit: `c6285528`
- Next scheduled pulse: `2026-07-29T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-28T18:00:08.905948Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-28T17:53:18.444679Z`; age seconds: `412`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `175712`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-28T18:00:10.555028Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-28T18:00:11.237268Z`; age seconds: `0`
