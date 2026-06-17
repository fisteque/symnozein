# Bridge State Summary

- Generated at: `2026-06-17T18:00:04.221687Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T17:59:58.790496+00:00`
- Heartbeat count: `118951`
- Heartbeat last gap seconds: `10.007671`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1192081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `3.335362`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T18:00:02.125874+00:00`

## Body Health

- Health generated at: `2026-06-17T17:56:01.720487Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.11 / 0.11 / 0.09`
- RAM used percent: `14.25`
- Swap used percent: `0.0`
- Root disk used percent: `7.83`

## Bridge Sync

- Last inbound sync: `2026-06-17T18:00:02.766643Z`
- Last outbound sync: `2026-06-17T18:00:03.578608Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `067af326`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-root-web-check-001`
- Last processed status: `pending_codex`
- Processed count: `19`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-17T18:00:03.702241Z`
- Last body pulse: `2026-06-17T14:00:06.516226Z`
- Last pulse commit: `4fcdd19f`
- Next scheduled pulse: `2026-06-18T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T18:00:02.125874Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T17:56:01.720487Z`; age seconds: `242`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T17:17:39.057579Z`; age seconds: `2545`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T18:00:03.578608Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T18:00:04.168087Z`; age seconds: `0`
