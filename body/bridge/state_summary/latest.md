# Bridge State Summary

- Generated at: `2026-06-30T06:00:04.646024Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T05:59:57.947049+00:00`
- Heartbeat count: `226722`
- Heartbeat last gap seconds: `10.007794`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2272081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `8.286745`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T05:59:56.226016+00:00`

## Body Health

- Health generated at: `2026-06-30T05:52:35.481893Z`
- CPU temperature C: `51.25`
- Load average 1m / 5m / 15m: `0.19 / 0.1 / 0.07`
- RAM used percent: `16.11`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T05:59:56.891291Z`
- Last outbound sync: `2026-06-30T05:59:57.700198Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `79fb17a5`

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
- Current pulse started: `2026-06-30T06:00:04.118840Z`
- Last body pulse: `2026-06-30T02:00:08.454523Z`
- Last pulse commit: `f04f44a3`
- Next scheduled pulse: `2026-06-30T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T05:59:57.947049Z`; age seconds: `6`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T05:52:35.481893Z`; age seconds: `449`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `641714`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T05:59:57.700198Z`; age seconds: `6`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T06:00:04.593514Z`; age seconds: `0`
