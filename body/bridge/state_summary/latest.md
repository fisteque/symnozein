# Bridge State Summary

- Generated at: `2026-08-21T19:04:44.412813Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-08-21T19:04:36.979571+00:00`
- Heartbeat count: `656391`
- Heartbeat last gap seconds: `10.007853`
- Heartbeat max gap seconds: `234084.609605`
- Heartbeat service started at: `Tue 2026-08-11 23:39:31 CEST`
- Heartbeat uptime seconds: `620638`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `19`
- Heartbeat log latest start: `2026-08-11T21:39:32.221012Z`
- Heartbeat log max start gap seconds: `4969432`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `3.399044`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-08-21T19:04:40.378631+00:00`

## Body Health

- Health generated at: `2026-08-21T18:55:09.765480Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `8.05`
- Swap used percent: `0.0`
- Root disk used percent: `9.59`

## Bridge Sync

- Last inbound sync: `2026-08-21T19:04:44.168561Z`
- Last outbound sync: `2026-07-31T11:15:22.124557Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `992a0618`
- Summary snapshot phase: `pre-outbound`

## Queues

- Bridge inbox pending: `0`
- Bridge runtime outbox awaiting publish/archive: `11`
- Oldest runtime outbox age seconds: `1842500`

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

- Current pulse status: `error`
- Current pulse started: `(unknown)`
- Last body pulse: `2026-07-31T10:00:06.789382Z`
- Last pulse commit: `5906bcf7`
- Next scheduled pulse: `2026-08-22T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-08-21T19:04:40.378631Z`; age seconds: `4`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-08-21T18:55:09.765480Z`; age seconds: `574`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `2253185`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-08-21T19:04:44.168561Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-08-18T22:00:00.202973Z`; age seconds: `248684`
