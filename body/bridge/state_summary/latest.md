# Bridge State Summary

- Generated at: `2026-06-15T18:00:09.232816Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-15T18:00:07.162885+00:00`
- Heartbeat count: `101704`
- Heartbeat last gap seconds: `10.007411`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1019286`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.472468`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-15T18:00:08.635370+00:00`

## Body Health

- Health generated at: `2026-06-15T17:51:48.063424Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.09 / 0.06 / 0.0`
- RAM used percent: `13.59`
- Swap used percent: `0.0`
- Root disk used percent: `7.76`

## Bridge Sync

- Last inbound sync: `2026-06-15T17:59:59.221450Z`
- Last outbound sync: `2026-06-15T17:59:59.929396Z`
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
- Current pulse started: `2026-06-15T18:00:08.735301Z`
- Last body pulse: `2026-06-15T14:00:12.430688Z`
- Last pulse commit: `c441c020`
- Next scheduled pulse: `2026-06-16T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-15T18:00:08.635370Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-15T17:51:48.063424Z`; age seconds: `501`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `80804`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-15T17:59:59.929396Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-15T18:00:09.179149Z`; age seconds: `0`
