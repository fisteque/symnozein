# Bridge State Summary

- Generated at: `2026-07-22T18:00:10.031558Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-22T18:00:01.192437+00:00`
- Heartbeat count: `420696`
- Heartbeat last gap seconds: `10.008249`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4216087`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `8.08564`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-22T18:00:09.278093+00:00`

## Body Health

- Health generated at: `2026-07-22T18:00:09.370074Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.1 / 0.15 / 0.09`
- RAM used percent: `19.93`
- Swap used percent: `0.0`
- Root disk used percent: `8.51`

## Bridge Sync

- Last inbound sync: `2026-07-22T17:59:49.983477Z`
- Last outbound sync: `2026-07-22T17:59:50.880140Z`
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
- Current pulse started: `2026-07-22T18:00:09.376441Z`
- Last body pulse: `2026-07-22T14:00:12.870904Z`
- Last pulse commit: `38d77703`
- Next scheduled pulse: `2026-07-23T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-22T18:00:09.278093Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-22T18:00:09.370074Z`; age seconds: `0`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1892460`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-22T17:59:50.880140Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-22T18:00:09.920365Z`; age seconds: `0`
