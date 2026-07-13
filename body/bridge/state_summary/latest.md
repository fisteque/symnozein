# Bridge State Summary

- Generated at: `2026-07-13T22:00:08.330512Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-13T22:00:00.627888+00:00`
- Heartbeat count: `344559`
- Heartbeat last gap seconds: `10.004265`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3452885`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `7.068176`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-13T22:00:07.696080+00:00`

## Body Health

- Health generated at: `2026-07-13T21:51:37.114484Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.04 / 0.01 / 0.0`
- RAM used percent: `18.6`
- Swap used percent: `0.0`
- Root disk used percent: `8.25`

## Bridge Sync

- Last inbound sync: `2026-07-13T21:59:58.364087Z`
- Last outbound sync: `2026-07-13T21:59:59.135334Z`
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
- Current pulse started: `2026-07-13T22:00:07.792624Z`
- Last body pulse: `2026-07-13T18:00:10.162234Z`
- Last pulse commit: `724c2589`
- Next scheduled pulse: `2026-07-14T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-13T22:00:07.696080Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-13T21:51:37.114484Z`; age seconds: `511`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1129258`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-13T21:59:59.135334Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-13T22:00:08.275408Z`; age seconds: `0`
