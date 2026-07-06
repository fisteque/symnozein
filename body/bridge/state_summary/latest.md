# Bridge State Summary

- Generated at: `2026-07-06T06:00:09.494281Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-06T06:00:04.054574+00:00`
- Heartbeat count: `278451`
- Heartbeat last gap seconds: `10.006997`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2790486`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.794336`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-06T06:00:08.848926+00:00`

## Body Health

- Health generated at: `2026-07-06T05:55:18.523326Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.95`
- Swap used percent: `0.0`
- Root disk used percent: `8.14`

## Bridge Sync

- Last inbound sync: `2026-07-06T05:59:49.480081Z`
- Last outbound sync: `2026-07-06T05:59:50.234453Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

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
- Current pulse started: `2026-07-06T06:00:08.941393Z`
- Last body pulse: `2026-07-06T02:00:02.771097Z`
- Last pulse commit: `b32116d6`
- Next scheduled pulse: `2026-07-06T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-06T06:00:08.848926Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-06T05:55:18.523326Z`; age seconds: `290`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `466859`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-06T05:59:50.234453Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-06T06:00:09.422228Z`; age seconds: `0`
