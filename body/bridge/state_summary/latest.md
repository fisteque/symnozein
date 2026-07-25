# Bridge State Summary

- Generated at: `2026-07-25T10:00:10.558317Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-25T10:00:05.236815+00:00`
- Heartbeat count: `443690`
- Heartbeat last gap seconds: `10.008613`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4446487`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.625305`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-25T10:00:09.862137+00:00`

## Body Health

- Health generated at: `2026-07-25T09:55:59.622797Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.01`
- RAM used percent: `20.69`
- Swap used percent: `0.0`
- Root disk used percent: `8.55`

## Bridge Sync

- Last inbound sync: `2026-07-25T09:59:50.595177Z`
- Last outbound sync: `2026-07-25T09:59:51.474846Z`
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
- Current pulse started: `2026-07-25T10:00:09.955208Z`
- Last body pulse: `2026-07-25T06:00:12.564410Z`
- Last pulse commit: `7134e973`
- Next scheduled pulse: `2026-07-25T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-25T10:00:09.862137Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-25T09:55:59.622797Z`; age seconds: `250`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2122860`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-25T09:59:51.474846Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-25T10:00:10.486335Z`; age seconds: `0`
