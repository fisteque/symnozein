# Bridge State Summary

- Generated at: `2026-07-20T06:00:35.648873Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-20T06:00:26.638421+00:00`
- Heartbeat count: `399145`
- Heartbeat last gap seconds: `10.007846`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4000112`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `7.932169`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-20T06:00:34.570606+00:00`

## Body Health

- Health generated at: `2026-07-20T05:55:04.145369Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.07 / 0.02 / 0.0`
- RAM used percent: `19.39`
- Swap used percent: `0.0`
- Root disk used percent: `8.47`

## Bridge Sync

- Last inbound sync: `2026-07-20T06:00:35.479689Z`
- Last outbound sync: `2026-07-20T05:59:36.009714Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

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
- Last body pulse: `2026-07-20T06:00:06.291945Z`
- Last pulse commit: `84207c9c`
- Next scheduled pulse: `Mon 2026-07-20 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-20T06:00:34.570606Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-20T05:55:04.145369Z`; age seconds: `331`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1676485`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-20T06:00:35.479689Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-20T06:00:06.291945Z`; age seconds: `29`
