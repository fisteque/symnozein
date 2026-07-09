# Bridge State Summary

- Generated at: `2026-07-09T22:00:08.109156Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-09T22:00:05.973761+00:00`
- Heartbeat count: `310066`
- Heartbeat last gap seconds: `10.004244`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3107285`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.483884`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-09T22:00:07.457662+00:00`

## Body Health

- Health generated at: `2026-07-09T21:52:56.779040Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.21 / 0.12 / 0.04`
- RAM used percent: `17.86`
- Swap used percent: `0.0`
- Root disk used percent: `8.21`

## Bridge Sync

- Last inbound sync: `2026-07-09T21:59:48.357512Z`
- Last outbound sync: `2026-07-09T21:59:49.157300Z`
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
- Current pulse started: `2026-07-09T22:00:07.558139Z`
- Last body pulse: `2026-07-09T18:00:07.971905Z`
- Last pulse commit: `aec2cdec`
- Next scheduled pulse: `2026-07-10T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-09T22:00:07.457662Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-09T21:52:56.779040Z`; age seconds: `431`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `783658`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-09T21:59:49.157300Z`; age seconds: `18`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-09T22:00:08.058199Z`; age seconds: `0`
