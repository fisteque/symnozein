# Bridge State Summary

- Generated at: `2026-06-29T06:00:08.365611Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-29T06:00:00.214364+00:00`
- Heartbeat count: `218096`
- Heartbeat last gap seconds: `10.004161`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2185685`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `6.071375`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-29T06:00:06.285755+00:00`

## Body Health

- Health generated at: `2026-06-29T05:50:35.639214Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.09 / 0.08 / 0.03`
- RAM used percent: `16.37`
- Swap used percent: `0.0`
- Root disk used percent: `8.01`

## Bridge Sync

- Last inbound sync: `2026-06-29T06:00:06.940910Z`
- Last outbound sync: `2026-06-29T06:00:07.727877Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-29T06:00:07.848819Z`
- Last body pulse: `2026-06-29T02:00:08.841923Z`
- Last pulse commit: `2c249c4b`
- Next scheduled pulse: `2026-06-29T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-29T06:00:06.285755Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-29T05:50:35.639214Z`; age seconds: `572`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `555318`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-29T06:00:07.727877Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-29T06:00:08.308761Z`; age seconds: `0`
