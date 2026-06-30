# Bridge State Summary

- Generated at: `2026-06-30T10:00:04.690923Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T09:59:59.191569+00:00`
- Heartbeat count: `228159`
- Heartbeat last gap seconds: `10.007858`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2286481`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `7.043093`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T09:59:56.226821+00:00`

## Body Health

- Health generated at: `2026-06-30T09:52:55.676983Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.02 / 0.02 / 0.0`
- RAM used percent: `16.29`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T09:59:56.948447Z`
- Last outbound sync: `2026-06-30T09:59:57.683603Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `79fb17a5`

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
- Current pulse started: `2026-06-30T10:00:04.134169Z`
- Last body pulse: `2026-06-30T06:00:05.935327Z`
- Last pulse commit: `fd41422d`
- Next scheduled pulse: `2026-06-30T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T09:59:59.191569Z`; age seconds: `5`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T09:52:55.676983Z`; age seconds: `429`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `656114`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T09:59:57.683603Z`; age seconds: `7`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T10:00:04.615981Z`; age seconds: `0`
