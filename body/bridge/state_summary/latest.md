# Bridge State Summary

- Generated at: `2026-07-13T18:00:08.429277Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-13T17:59:59.672060+00:00`
- Heartbeat count: `343121`
- Heartbeat last gap seconds: `10.007241`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3438485`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `8.103819`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-13T18:00:07.775895+00:00`

## Body Health

- Health generated at: `2026-07-13T17:51:17.115878Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.2 / 0.14 / 0.05`
- RAM used percent: `18.3`
- Swap used percent: `0.0`
- Root disk used percent: `8.24`

## Bridge Sync

- Last inbound sync: `2026-07-13T17:59:48.460860Z`
- Last outbound sync: `2026-07-13T17:59:49.244902Z`
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
- Current pulse started: `2026-07-13T18:00:07.870020Z`
- Last body pulse: `2026-07-13T14:00:10.842912Z`
- Last pulse commit: `f05400eb`
- Next scheduled pulse: `2026-07-14T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-13T18:00:07.775895Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-13T17:51:17.115878Z`; age seconds: `531`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1114858`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-13T17:59:49.244902Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-13T18:00:08.373585Z`; age seconds: `0`
