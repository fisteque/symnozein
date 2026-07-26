# Bridge State Summary

- Generated at: `2026-07-26T09:10:53.865525Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T09:10:47.270986+00:00`
- Heartbeat count: `452016`
- Heartbeat last gap seconds: `10.006842`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4529930`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.683531`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T09:10:52.954534+00:00`

## Body Health

- Health generated at: `2026-07-26T09:08:12.762552Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.0 / 0.15 / 0.26`
- RAM used percent: `29.2`
- Swap used percent: `0.0`
- Root disk used percent: `8.75`

## Bridge Sync

- Last inbound sync: `2026-07-26T09:10:53.698092Z`
- Last outbound sync: `2026-07-26T09:10:24.929584Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `10098dc1`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-26T06:00:11.947548Z`
- Last pulse commit: `af00fdf6`
- Next scheduled pulse: `Sun 2026-07-26 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T09:10:52.954534Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T09:08:12.762552Z`; age seconds: `161`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2206304`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T09:10:53.698092Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T06:00:11.947548Z`; age seconds: `11441`
