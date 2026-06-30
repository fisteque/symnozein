# Bridge State Summary

- Generated at: `2026-06-30T03:52:06.579313Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T03:52:01.678739+00:00`
- Heartbeat count: `225955`
- Heartbeat last gap seconds: `10.004368`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2264403`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `3.873761`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T03:52:05.552518+00:00`

## Body Health

- Health generated at: `2026-06-30T03:42:24.725735Z`
- CPU temperature C: `52.35`
- Load average 1m / 5m / 15m: `0.02 / 0.08 / 0.08`
- RAM used percent: `16.24`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T03:52:06.419171Z`
- Last outbound sync: `2026-06-30T03:51:06.949106Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-30T02:00:08.454523Z`
- Last pulse commit: `f04f44a3`
- Next scheduled pulse: `Tue 2026-06-30 08:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T03:52:05.552518Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T03:42:24.725735Z`; age seconds: `581`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `634036`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T03:52:06.419171Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T02:00:08.454523Z`; age seconds: `6718`
