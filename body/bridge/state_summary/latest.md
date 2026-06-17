# Bridge State Summary

- Generated at: `2026-06-17T09:54:42.255832Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T09:54:33.169957+00:00`
- Heartbeat count: `116044`
- Heartbeat last gap seconds: `10.008399`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1162959`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `1.107211`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T09:54:34.277183+00:00`

## Body Health

- Health generated at: `2026-06-17T09:45:13.630064Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.08 / 0.06 / 0.05`
- RAM used percent: `14.16`
- Swap used percent: `0.0`
- Root disk used percent: `7.8`

## Bridge Sync

- Last inbound sync: `2026-06-17T09:53:33.762416Z`
- Last outbound sync: `2026-06-17T09:53:36.008254Z`
- Last outbound sync status: `pushed`
- Last outbound commit: `9af98d12`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-17T09:54:41.619426Z`
- Last body pulse: `2026-06-16T10:00:04.318482Z`
- Last pulse commit: `30d4f9a1`
- Next scheduled pulse: `2026-06-17T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T09:54:34.277183Z`; age seconds: `7`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T09:45:13.630064Z`; age seconds: `568`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `224477`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T09:53:36.008254Z`; age seconds: `66`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T09:54:42.197210Z`; age seconds: `0`
