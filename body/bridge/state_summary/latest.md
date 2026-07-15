# Bridge State Summary

- Generated at: `2026-07-15T14:00:09.802565Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-15T14:00:05.804597+00:00`
- Heartbeat count: `358926`
- Heartbeat last gap seconds: `10.004272`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3596886`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `3.347066`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-15T14:00:09.151681+00:00`

## Body Health

- Health generated at: `2026-07-15T13:54:58.753325Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.09 / 0.06 / 0.01`
- RAM used percent: `18.71`
- Swap used percent: `0.0`
- Root disk used percent: `8.34`

## Bridge Sync

- Last inbound sync: `2026-07-15T13:59:49.810530Z`
- Last outbound sync: `2026-07-15T13:59:50.568997Z`
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
- Current pulse started: `2026-07-15T14:00:09.254020Z`
- Last body pulse: `2026-07-15T10:00:11.589869Z`
- Last pulse commit: `e0fb0f9f`
- Next scheduled pulse: `2026-07-15T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-15T14:00:09.151681Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-15T13:54:58.753325Z`; age seconds: `311`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1273260`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-15T13:59:50.568997Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-15T14:00:09.752231Z`; age seconds: `0`
