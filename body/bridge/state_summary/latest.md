# Bridge State Summary

- Generated at: `2026-07-03T10:00:08.874499Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-03T10:00:02.111575+00:00`
- Heartbeat count: `254027`
- Heartbeat last gap seconds: `10.00761`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2545685`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `6.178831`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-03T10:00:08.290422+00:00`

## Body Health

- Health generated at: `2026-07-03T09:59:08.308733Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.22 / 0.13 / 0.04`
- RAM used percent: `16.8`
- Swap used percent: `0.0`
- Root disk used percent: `8.12`

## Bridge Sync

- Last inbound sync: `2026-07-03T09:59:58.930384Z`
- Last outbound sync: `2026-07-03T09:59:59.740999Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

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
- Current pulse started: `2026-07-03T10:00:08.387382Z`
- Last body pulse: `2026-07-03T06:00:09.769141Z`
- Last pulse commit: `8cb2cb41`
- Next scheduled pulse: `2026-07-03T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-03T10:00:08.290422Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-03T09:59:08.308733Z`; age seconds: `60`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `222059`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-03T09:59:59.740999Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-03T10:00:08.821794Z`; age seconds: `0`
