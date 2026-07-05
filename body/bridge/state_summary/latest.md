# Bridge State Summary

- Generated at: `2026-07-05T18:00:07.147373Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-05T17:59:57.854904+00:00`
- Heartbeat count: `274145`
- Heartbeat last gap seconds: `10.006729`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2747284`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `8.672769`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-05T18:00:06.527688+00:00`

## Body Health

- Health generated at: `2026-07-05T17:54:15.998457Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.0 / 0.03 / 0.05`
- RAM used percent: `17.22`
- Swap used percent: `0.0`
- Root disk used percent: `8.13`

## Bridge Sync

- Last inbound sync: `2026-07-05T17:59:47.217083Z`
- Last outbound sync: `2026-07-05T17:59:48.032060Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

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
- Current pulse started: `2026-07-05T18:00:06.613682Z`
- Last body pulse: `2026-07-05T14:00:07.287048Z`
- Last pulse commit: `9eb2734c`
- Next scheduled pulse: `2026-07-06T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-05T18:00:06.527688Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-05T17:54:15.998457Z`; age seconds: `351`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `423657`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-05T17:59:48.032060Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-05T18:00:07.073016Z`; age seconds: `0`
