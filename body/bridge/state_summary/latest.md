# Bridge State Summary

- Generated at: `2026-07-06T22:00:08.981535Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-06T22:00:08.554962+00:00`
- Heartbeat count: `284203`
- Heartbeat last gap seconds: `10.009556`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2848086`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `9.766489`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-06T22:00:08.311915+00:00`

## Body Health

- Health generated at: `2026-07-06T21:56:38.136577Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `17.28`
- Swap used percent: `0.0`
- Root disk used percent: `8.14`

## Bridge Sync

- Last inbound sync: `2026-07-06T21:59:58.982957Z`
- Last outbound sync: `2026-07-06T21:59:59.739679Z`
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
- Current pulse started: `2026-07-06T22:00:08.416738Z`
- Last body pulse: `2026-07-06T18:00:10.406146Z`
- Last pulse commit: `41339035`
- Next scheduled pulse: `2026-07-07T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-06T22:00:08.554962Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-06T21:56:38.136577Z`; age seconds: `210`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `524459`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-06T21:59:59.739679Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-06T22:00:08.929625Z`; age seconds: `0`
