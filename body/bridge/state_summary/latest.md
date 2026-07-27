# Bridge State Summary

- Generated at: `2026-07-27T02:00:07.288818Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-27T01:59:58.479790+00:00`
- Heartbeat count: `458059`
- Heartbeat last gap seconds: `10.008748`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4590484`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `6.489544`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-27T02:00:04.969350+00:00`

## Body Health

- Health generated at: `2026-07-27T01:59:45.044690Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `12.04`
- Swap used percent: `0.0`
- Root disk used percent: `8.87`

## Bridge Sync

- Last inbound sync: `2026-07-27T02:00:05.696593Z`
- Last outbound sync: `2026-07-27T02:00:06.590107Z`
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
- Current pulse started: `2026-07-27T02:00:06.701233Z`
- Last body pulse: `2026-07-26T22:00:08.538901Z`
- Last pulse commit: `9b945982`
- Next scheduled pulse: `2026-07-27T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-27T02:00:04.969350Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-27T01:59:45.044690Z`; age seconds: `22`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `31708`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-27T02:00:06.590107Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-27T02:00:07.233912Z`; age seconds: `0`
