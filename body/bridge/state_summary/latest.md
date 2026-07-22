# Bridge State Summary

- Generated at: `2026-07-22T22:00:01.657124Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-22T21:59:53.929587+00:00`
- Heartbeat count: `422132`
- Heartbeat last gap seconds: `10.005514`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4230478`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.744425`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-22T22:00:00.674026+00:00`

## Body Health

- Health generated at: `2026-07-22T21:50:30.035190Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.2 / 0.1 / 0.03`
- RAM used percent: `20.35`
- Swap used percent: `0.0`
- Root disk used percent: `8.52`

## Bridge Sync

- Last inbound sync: `2026-07-22T21:59:51.432690Z`
- Last outbound sync: `2026-07-22T21:59:52.247671Z`
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
- Current pulse started: `2026-07-22T22:00:00.785462Z`
- Last body pulse: `2026-07-22T18:00:14.244064Z`
- Last pulse commit: `bc2bfc72`
- Next scheduled pulse: `2026-07-23T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-22T22:00:00.674026Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-22T21:50:30.035190Z`; age seconds: `571`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1906851`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-22T21:59:52.247671Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-22T22:00:01.602386Z`; age seconds: `0`
