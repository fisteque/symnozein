# Bridge State Summary

- Generated at: `2026-07-01T02:00:07.701425Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-01T02:00:03.493570+00:00`
- Heartbeat count: `233906`
- Heartbeat last gap seconds: `10.011173`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2344084`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `3.57584`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-01T02:00:07.069426+00:00`

## Body Health

- Health generated at: `2026-07-01T01:54:16.518713Z`
- CPU temperature C: `48.5`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.25`
- Swap used percent: `0.0`
- Root disk used percent: `8.03`

## Bridge Sync

- Last inbound sync: `2026-07-01T01:59:47.729074Z`
- Last outbound sync: `2026-07-01T01:59:48.461827Z`
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
- Current pulse started: `2026-07-01T02:00:07.155600Z`
- Last body pulse: `2026-06-30T22:00:09.278213Z`
- Last pulse commit: `b5ff3d46`
- Next scheduled pulse: `2026-07-01T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-01T02:00:07.069426Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-01T01:54:16.518713Z`; age seconds: `351`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `20457`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-01T01:59:48.461827Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-01T02:00:07.647819Z`; age seconds: `0`
