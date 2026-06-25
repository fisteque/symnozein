# Bridge State Summary

- Generated at: `2026-06-25T06:00:03.969759Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-25T06:00:00.607138+00:00`
- Heartbeat count: `183606`
- Heartbeat last gap seconds: `10.005035`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1840081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.624047`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-25T06:00:03.231257+00:00`

## Body Health

- Health generated at: `2026-06-25T05:51:42.634673Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.05 / 0.04 / 0.01`
- RAM used percent: `15.68`
- Swap used percent: `0.0`
- Root disk used percent: `7.98`

## Bridge Sync

- Last inbound sync: `2026-06-25T05:59:43.846517Z`
- Last outbound sync: `2026-06-25T05:59:44.606339Z`
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
- Current pulse started: `2026-06-25T06:00:03.323470Z`
- Last body pulse: `2026-06-25T02:00:05.328931Z`
- Last pulse commit: `f2cfe4c1`
- Next scheduled pulse: `2026-06-25T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-25T06:00:03.231257Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-25T05:51:42.634673Z`; age seconds: `501`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `209713`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-25T05:59:44.606339Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-25T06:00:03.917744Z`; age seconds: `0`
