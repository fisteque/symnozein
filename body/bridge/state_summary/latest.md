# Bridge State Summary

- Generated at: `2026-07-14T06:00:04.689661Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-14T06:00:01.956847+00:00`
- Heartbeat count: `347433`
- Heartbeat last gap seconds: `10.00877`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3481681`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `5.587012`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-14T05:59:57.535103+00:00`

## Body Health

- Health generated at: `2026-07-14T05:52:17.011023Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.06 / 0.16 / 0.09`
- RAM used percent: `18.61`
- Swap used percent: `0.0`
- Root disk used percent: `8.25`

## Bridge Sync

- Last inbound sync: `2026-07-14T05:59:48.212588Z`
- Last outbound sync: `2026-07-14T05:59:48.982161Z`
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
- Current pulse started: `2026-07-14T06:00:04.130794Z`
- Last body pulse: `2026-07-14T02:00:06.300840Z`
- Last pulse commit: `b9154328`
- Next scheduled pulse: `2026-07-14T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-14T06:00:01.956847Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-14T05:52:17.011023Z`; age seconds: `467`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1158054`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-14T05:59:48.982161Z`; age seconds: `15`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-14T06:00:04.635250Z`; age seconds: `0`
