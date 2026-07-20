# Bridge State Summary

- Generated at: `2026-07-20T22:00:06.483144Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-20T22:00:02.728867+00:00`
- Heartbeat count: `404890`
- Heartbeat last gap seconds: `10.004478`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4057683`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.98326`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-20T22:00:05.712143+00:00`

## Body Health

- Health generated at: `2026-07-20T21:56:25.498739Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `19.47`
- Swap used percent: `0.0`
- Root disk used percent: `8.48`

## Bridge Sync

- Last inbound sync: `2026-07-20T21:59:56.416144Z`
- Last outbound sync: `2026-07-20T21:59:57.289113Z`
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
- Current pulse started: `2026-07-20T22:00:05.847404Z`
- Last body pulse: `2026-07-20T18:00:08.022895Z`
- Last pulse commit: `8e5d6f48`
- Next scheduled pulse: `2026-07-21T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-20T22:00:05.712143Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-20T21:56:25.498739Z`; age seconds: `220`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1734056`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-20T21:59:57.289113Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-20T22:00:06.377390Z`; age seconds: `0`
