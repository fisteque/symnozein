# Bridge State Summary

- Generated at: `2026-06-17T14:31:49.980033Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T14:31:47.744990+00:00`
- Heartbeat count: `117705`
- Heartbeat last gap seconds: `10.34697`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1179587`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.350109`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T14:31:49.095116+00:00`

## Body Health

- Health generated at: `2026-06-17T14:25:38.559342Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.18`
- Swap used percent: `0.0`
- Root disk used percent: `7.8`

## Bridge Sync

- Last inbound sync: `2026-06-17T14:31:49.727588Z`
- Last outbound sync: `2026-06-17T14:31:20.612358Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `c982736f`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `1`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-pulse-state-check-001`
- Last processed status: `pending_codex`
- Processed count: `18`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-17T14:00:06.516226Z`
- Last pulse commit: `4fcdd19f`
- Next scheduled pulse: `Wed 2026-06-17 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T14:31:49.095116Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T14:25:38.559342Z`; age seconds: `371`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T14:24:19.305608Z`; age seconds: `450`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T14:31:49.727588Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T14:00:06.516226Z`; age seconds: `1903`
