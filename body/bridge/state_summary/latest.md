# Bridge State Summary

- Generated at: `2026-07-05T06:00:03.608173Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-05T05:59:58.146672+00:00`
- Heartbeat count: `269834`
- Heartbeat last gap seconds: `10.004302`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2704080`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `3.025312`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-05T06:00:01.172001+00:00`

## Body Health

- Health generated at: `2026-07-05T05:53:10.720171Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.07 / 0.04 / 0.04`
- RAM used percent: `17.16`
- Swap used percent: `0.0`
- Root disk used percent: `8.13`

## Bridge Sync

- Last inbound sync: `2026-07-05T06:00:01.870872Z`
- Last outbound sync: `2026-07-05T06:00:02.897507Z`
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
- Current pulse started: `2026-07-05T06:00:03.033607Z`
- Last body pulse: `2026-07-05T02:00:06.006314Z`
- Last pulse commit: `134b5634`
- Next scheduled pulse: `2026-07-05T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-05T06:00:01.172001Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-05T05:53:10.720171Z`; age seconds: `412`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `380453`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-05T06:00:02.897507Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-05T06:00:03.555247Z`; age seconds: `0`
