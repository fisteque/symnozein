# Bridge State Summary

- Generated at: `2026-07-09T18:00:06.392019Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-09T18:00:01.477950+00:00`
- Heartbeat count: `308629`
- Heartbeat last gap seconds: `10.00829`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3092883`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `4.251362`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-09T18:00:05.729327+00:00`

## Body Health

- Health generated at: `2026-07-09T17:52:34.131167Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `17.6`
- Swap used percent: `0.0`
- Root disk used percent: `8.21`

## Bridge Sync

- Last inbound sync: `2026-07-09T17:59:46.382526Z`
- Last outbound sync: `2026-07-09T17:59:47.214593Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-07-09T18:00:05.824107Z`
- Last body pulse: `2026-07-09T14:00:07.405078Z`
- Last pulse commit: `59a58f00`
- Next scheduled pulse: `2026-07-10T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-09T18:00:05.729327Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-09T17:52:34.131167Z`; age seconds: `452`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `769256`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-09T17:59:47.214593Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-09T18:00:06.337575Z`; age seconds: `0`
