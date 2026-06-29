# Bridge State Summary

- Generated at: `2026-06-29T18:00:06.688002Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-29T18:00:03.388545+00:00`
- Heartbeat count: `222408`
- Heartbeat last gap seconds: `10.00771`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2228883`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.648246`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-29T18:00:06.036806+00:00`

## Body Health

- Health generated at: `2026-06-29T17:51:35.433000Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.18 / 0.15 / 0.07`
- RAM used percent: `16.34`
- Swap used percent: `0.0`
- Root disk used percent: `8.01`

## Bridge Sync

- Last inbound sync: `2026-06-29T17:59:56.651133Z`
- Last outbound sync: `2026-06-29T17:59:57.405077Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-29T18:00:06.159297Z`
- Last body pulse: `2026-06-29T14:00:09.919594Z`
- Last pulse commit: `26a24e9f`
- Next scheduled pulse: `2026-06-30T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-29T18:00:06.036806Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-29T17:51:35.433000Z`; age seconds: `511`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `598516`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-29T17:59:57.405077Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-29T18:00:06.633965Z`; age seconds: `0`
