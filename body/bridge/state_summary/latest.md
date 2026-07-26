# Bridge State Summary

- Generated at: `2026-07-26T10:00:02.297194Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T09:59:57.751139+00:00`
- Heartbeat count: `452310`
- Heartbeat last gap seconds: `10.007213`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4532879`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `1.966075`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T09:59:59.717231+00:00`

## Body Health

- Health generated at: `2026-07-26T09:58:19.554241Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.05 / 0.25 / 0.24`
- RAM used percent: `29.08`
- Swap used percent: `0.0`
- Root disk used percent: `9.12`

## Bridge Sync

- Last inbound sync: `2026-07-26T10:00:00.449567Z`
- Last outbound sync: `2026-07-26T10:00:01.368006Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `a69f23e8`

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

- Current pulse status: `running`
- Current pulse started: `2026-07-26T10:00:01.478147Z`
- Last body pulse: `2026-07-26T06:00:11.947548Z`
- Last pulse commit: `af00fdf6`
- Next scheduled pulse: `2026-07-26T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T09:59:59.717231Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T09:58:19.554241Z`; age seconds: `102`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2209252`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T10:00:01.368006Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T10:00:02.237752Z`; age seconds: `0`
