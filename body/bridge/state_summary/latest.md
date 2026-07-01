# Bridge State Summary

- Generated at: `2026-07-01T15:27:33.982313Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-01T15:27:25.816797+00:00`
- Heartbeat count: `238742`
- Heartbeat last gap seconds: `10.009677`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2392531`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `2.398135`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-01T15:27:28.214947+00:00`

## Body Health

- Health generated at: `2026-07-01T15:25:28.137145Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.36`
- Swap used percent: `0.0`
- Root disk used percent: `8.1`

## Bridge Sync

- Last inbound sync: `2026-07-01T15:27:33.798057Z`
- Last outbound sync: `2026-07-01T15:26:19.556242Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `666a6c6f`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-01T14:00:02.836513Z`
- Last pulse commit: `bdb981ea`
- Next scheduled pulse: `Wed 2026-07-01 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-01T15:27:28.214947Z`; age seconds: `5`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-01T15:25:28.137145Z`; age seconds: `125`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `68904`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-01T15:27:33.798057Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-01T14:00:02.836513Z`; age seconds: `5251`
