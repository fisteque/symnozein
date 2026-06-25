# Bridge State Summary

- Generated at: `2026-06-25T22:00:07.195113Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-25T22:00:06.413140+00:00`
- Heartbeat count: `189357`
- Heartbeat last gap seconds: `10.007526`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1897684`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `7.353722`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-25T22:00:03.759352+00:00`

## Body Health

- Health generated at: `2026-06-25T21:53:13.203193Z`
- CPU temperature C: `51.25`
- Load average 1m / 5m / 15m: `0.07 / 0.03 / 0.0`
- RAM used percent: `15.9`
- Swap used percent: `0.0`
- Root disk used percent: `7.99`

## Bridge Sync

- Last inbound sync: `2026-06-25T22:00:04.486241Z`
- Last outbound sync: `2026-06-25T22:00:05.524215Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-25T22:00:05.636773Z`
- Last body pulse: `2026-06-25T18:00:03.240262Z`
- Last pulse commit: `6c80a3bd`
- Next scheduled pulse: `2026-06-26T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-25T22:00:06.413140Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-25T21:53:13.203193Z`; age seconds: `413`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `267317`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-25T22:00:05.524215Z`; age seconds: `1`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-25T22:00:07.141999Z`; age seconds: `0`
