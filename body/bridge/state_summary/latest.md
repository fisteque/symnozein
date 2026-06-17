# Bridge State Summary

- Generated at: `2026-06-17T11:12:42.207581Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T11:12:37.107803+00:00`
- Heartbeat count: `116512`
- Heartbeat last gap seconds: `10.00752`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1167639`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.343559`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T11:12:41.451379+00:00`

## Body Health

- Health generated at: `2026-06-17T11:05:20.635726Z`
- CPU temperature C: `43.0`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.03`
- Swap used percent: `0.0`
- Root disk used percent: `7.8`

## Bridge Sync

- Last inbound sync: `2026-06-17T11:12:42.039377Z`
- Last outbound sync: `2026-06-17T11:12:12.687451Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `9af98d12`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-autoreply-path-test-001`
- Last processed status: `pending_codex`
- Processed count: `16`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-17T10:00:08.535178Z`
- Last pulse commit: `f7940c5c`
- Next scheduled pulse: `Wed 2026-06-17 16:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T11:12:41.451379Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T11:05:20.635726Z`; age seconds: `441`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T11:11:11.917967Z`; age seconds: `90`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T11:12:42.039377Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T10:00:08.535178Z`; age seconds: `4353`
