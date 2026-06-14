# Bridge State Summary

- Generated at: `2026-06-14T14:52:19.224435Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T14:52:17.686353+00:00`
- Heartbeat count: `91955`
- Heartbeat last gap seconds: `10.006699`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `921616`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `0.749163`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T14:52:18.435533+00:00`

## Body Health

- Health generated at: `2026-06-14T14:49:28.113413Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.02 / 0.01 / 0.0`
- RAM used percent: `15.03`
- Swap used percent: `0.0`
- Root disk used percent: `7.74`

## Bridge Sync

- Last inbound sync: `2026-06-14T14:52:19.058279Z`
- Last outbound sync: `2026-06-14T14:51:49.587988Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `7e848689`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260613-cli-setup-body-pulse-001`
- Last processed status: `ok`
- Processed count: `11`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Last body pulse: `2026-06-14T14:00:05.578687Z`
- Last pulse commit: `3c4c8d11`
- Next scheduled pulse: `Sun 2026-06-14 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T14:52:18.435533Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T14:49:28.113413Z`; age seconds: `171`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-13T19:01:34.718722Z`; age seconds: `71444`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T14:52:19.058279Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T14:00:05.578687Z`; age seconds: `3133`
