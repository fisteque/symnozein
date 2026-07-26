# Bridge State Summary

- Generated at: `2026-07-26T08:56:22.215709Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T08:56:15.772753+00:00`
- Heartbeat count: `451929`
- Heartbeat last gap seconds: `10.009221`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4529059`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.520361`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T08:56:21.293127+00:00`

## Body Health

- Health generated at: `2026-07-26T08:48:09.568802Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.46 / 0.39 / 0.28`
- RAM used percent: `28.87`
- Swap used percent: `0.0`
- Root disk used percent: `8.72`

## Bridge Sync

- Last inbound sync: `2026-07-26T08:56:21.993578Z`
- Last outbound sync: `2026-07-26T08:55:52.771157Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `04f20dea`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `1`
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

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T08:56:21.293127Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T08:48:09.568802Z`; age seconds: `492`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2205432`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T08:56:21.993578Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T06:00:11.947548Z`; age seconds: `10570`
