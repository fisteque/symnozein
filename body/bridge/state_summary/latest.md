# Bridge State Summary

- Generated at: `2026-07-24T10:00:11.208704Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-24T10:00:05.911793+00:00`
- Heartbeat count: `435069`
- Heartbeat last gap seconds: `10.004223`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4360088`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `2.99413`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-24T10:00:08.905939+00:00`

## Body Health

- Health generated at: `2026-07-24T09:53:48.474605Z`
- CPU temperature C: `41.9`
- Load average 1m / 5m / 15m: `0.0 / 0.05 / 0.04`
- RAM used percent: `20.69`
- Swap used percent: `0.0`
- Root disk used percent: `8.54`

## Bridge Sync

- Last inbound sync: `2026-07-24T10:00:09.668531Z`
- Last outbound sync: `2026-07-24T10:00:10.476063Z`
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
- Current pulse started: `2026-07-24T10:00:10.609528Z`
- Last body pulse: `2026-07-24T06:00:09.329475Z`
- Last pulse commit: `16ac1ca8`
- Next scheduled pulse: `2026-07-24T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-24T10:00:08.905939Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-24T09:53:48.474605Z`; age seconds: `382`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2036461`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-24T10:00:10.476063Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-24T10:00:11.153536Z`; age seconds: `0`
