# Bridge State Summary

- Generated at: `2026-06-15T22:00:10.940169Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-15T22:00:08.942624+00:00`
- Heartbeat count: `103142`
- Heartbeat last gap seconds: `10.019105`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1033688`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `0.054359`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-15T22:00:08.997001+00:00`

## Body Health

- Health generated at: `2026-06-15T21:52:08.355557Z`
- CPU temperature C: `43.0`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `13.73`
- Swap used percent: `0.0`
- Root disk used percent: `7.77`

## Bridge Sync

- Last inbound sync: `2026-06-15T22:00:09.646958Z`
- Last outbound sync: `2026-06-15T22:00:10.353362Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-15T22:00:10.458579Z`
- Last body pulse: `2026-06-15T18:00:10.841516Z`
- Last pulse commit: `4801ea43`
- Next scheduled pulse: `2026-06-16T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-15T22:00:08.997001Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-15T21:52:08.355557Z`; age seconds: `482`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `95206`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-15T22:00:10.353362Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-15T22:00:10.884319Z`; age seconds: `0`
