# Bridge State Summary

- Generated at: `2026-07-01T10:00:04.772836Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-01T09:59:55.626758+00:00`
- Heartbeat count: `236780`
- Heartbeat last gap seconds: `10.007578`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2372881`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `1.117583`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-01T09:59:56.744356+00:00`

## Body Health

- Health generated at: `2026-07-01T09:54:56.303317Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.54 / 0.25 / 0.13`
- RAM used percent: `16.53`
- Swap used percent: `0.0`
- Root disk used percent: `8.03`

## Bridge Sync

- Last inbound sync: `2026-07-01T09:59:47.379749Z`
- Last outbound sync: `2026-07-01T09:59:48.182230Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `666a6c6f`

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
- Current pulse started: `2026-07-01T10:00:04.122619Z`
- Last body pulse: `2026-07-01T06:00:08.988419Z`
- Last pulse commit: `00a5e294`
- Next scheduled pulse: `2026-07-01T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-01T09:59:56.744356Z`; age seconds: `8`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-01T09:54:56.303317Z`; age seconds: `308`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `49255`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-01T09:59:48.182230Z`; age seconds: `16`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-01T10:00:04.715949Z`; age seconds: `0`
