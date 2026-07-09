# Bridge State Summary

- Generated at: `2026-07-09T14:00:05.846770Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-09T13:59:57.533000+00:00`
- Heartbeat count: `307192`
- Heartbeat last gap seconds: `10.004238`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3078482`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `6.077145`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-09T14:00:03.610161+00:00`

## Body Health

- Health generated at: `2026-07-09T13:52:13.090899Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.01 / 0.01 / 0.0`
- RAM used percent: `17.77`
- Swap used percent: `0.0`
- Root disk used percent: `8.21`

## Bridge Sync

- Last inbound sync: `2026-07-09T14:00:04.317191Z`
- Last outbound sync: `2026-07-09T14:00:05.128809Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

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
- Current pulse started: `2026-07-09T14:00:05.288497Z`
- Last body pulse: `2026-07-09T10:00:06.064644Z`
- Last pulse commit: `163473cd`
- Next scheduled pulse: `2026-07-09T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-09T14:00:03.610161Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-09T13:52:13.090899Z`; age seconds: `472`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `754856`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-09T14:00:05.128809Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-09T14:00:05.793918Z`; age seconds: `0`
