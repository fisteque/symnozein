# Bridge State Summary

- Generated at: `2026-06-17T09:55:31.984975Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T09:55:23.208164+00:00`
- Heartbeat count: `116049`
- Heartbeat last gap seconds: `10.008955`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1163009`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `1.126952`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T09:55:24.335128+00:00`

## Body Health

- Health generated at: `2026-06-17T09:55:14.090569Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.52 / 0.25 / 0.12`
- RAM used percent: `14.17`
- Swap used percent: `0.0`
- Root disk used percent: `7.8`

## Bridge Sync

- Last inbound sync: `2026-06-17T09:55:30.485562Z`
- Last outbound sync: `2026-06-17T09:55:31.363579Z`
- Last outbound sync status: `latest_only_skipped`
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
- Current pulse started: `2026-06-17T09:55:31.523483Z`
- Last body pulse: `2026-06-17T09:54:43.541186Z`
- Last pulse commit: `0076f658`
- Next scheduled pulse: `2026-06-17T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T09:55:24.335128Z`; age seconds: `7`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T09:55:14.090569Z`; age seconds: `17`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `224527`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T09:55:31.363579Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T09:55:31.923652Z`; age seconds: `0`
