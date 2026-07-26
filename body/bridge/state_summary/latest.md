# Bridge State Summary

- Generated at: `2026-07-26T02:00:06.625097Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T02:00:03.020801+00:00`
- Heartbeat count: `449437`
- Heartbeat last gap seconds: `10.010753`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4504083`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.838128`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T02:00:05.858946+00:00`

## Body Health

- Health generated at: `2026-07-26T01:57:25.731964Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.05`
- RAM used percent: `21.21`
- Swap used percent: `0.0`
- Root disk used percent: `8.58`

## Bridge Sync

- Last inbound sync: `2026-07-26T01:59:46.529803Z`
- Last outbound sync: `2026-07-26T01:59:47.400826Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `f1c00bdd`

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
- Current pulse started: `2026-07-26T02:00:05.941298Z`
- Last body pulse: `2026-07-25T22:00:03.159231Z`
- Last pulse commit: `6668c15b`
- Next scheduled pulse: `2026-07-26T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T02:00:05.858946Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T01:57:25.731964Z`; age seconds: `160`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2180456`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T01:59:47.400826Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T02:00:06.552257Z`; age seconds: `0`
