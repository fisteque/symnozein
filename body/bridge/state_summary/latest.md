# Bridge State Summary

- Generated at: `2026-07-20T10:00:05.437505Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-20T09:59:58.332593+00:00`
- Heartbeat count: `400579`
- Heartbeat last gap seconds: `10.004315`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4014482`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.401697`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-20T10:00:04.734307+00:00`

## Body Health

- Health generated at: `2026-07-20T09:55:24.118425Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `19.65`
- Swap used percent: `0.0`
- Root disk used percent: `8.48`

## Bridge Sync

- Last inbound sync: `2026-07-20T09:59:55.441287Z`
- Last outbound sync: `2026-07-20T09:59:56.305142Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `f1c00bdd`

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
- Current pulse started: `2026-07-20T10:00:04.831274Z`
- Last body pulse: `2026-07-20T06:00:06.291945Z`
- Last pulse commit: `84207c9c`
- Next scheduled pulse: `2026-07-20T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-20T10:00:04.734307Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-20T09:55:24.118425Z`; age seconds: `281`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1690855`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-20T09:59:56.305142Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-20T10:00:05.381703Z`; age seconds: `0`
