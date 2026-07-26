# Bridge State Summary

- Generated at: `2026-07-26T14:00:02.060038Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T14:00:00.717050+00:00`
- Heartbeat count: `453746`
- Heartbeat last gap seconds: `10.00783`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4547279`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `0.582631`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T14:00:01.299697+00:00`

## Body Health

- Health generated at: `2026-07-26T13:58:41.307580Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.02 / 0.01 / 0.0`
- RAM used percent: `11.65`
- Swap used percent: `0.0`
- Root disk used percent: `8.86`

## Bridge Sync

- Last inbound sync: `2026-07-26T13:59:42.041210Z`
- Last outbound sync: `2026-07-26T13:59:42.877051Z`
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
- Current pulse started: `2026-07-26T14:00:01.398847Z`
- Last body pulse: `2026-07-26T10:00:04.068739Z`
- Last pulse commit: `f82045cf`
- Next scheduled pulse: `2026-07-26T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T14:00:01.299697Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T13:58:41.307580Z`; age seconds: `80`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2223652`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T13:59:42.877051Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T14:00:02.004931Z`; age seconds: `0`
