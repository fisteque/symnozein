# Bridge State Summary

- Generated at: `2026-06-26T22:00:09.877855Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-26T22:00:06.075011+00:00`
- Heartbeat count: `197979`
- Heartbeat last gap seconds: `10.005432`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1984086`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `3.176297`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-26T22:00:09.251324+00:00`

## Body Health

- Health generated at: `2026-06-26T21:55:28.856796Z`
- CPU temperature C: `51.25`
- Load average 1m / 5m / 15m: `0.08 / 0.03 / 0.0`
- RAM used percent: `16.04`
- Swap used percent: `0.0`
- Root disk used percent: `7.99`

## Bridge Sync

- Last inbound sync: `2026-06-26T21:59:49.848378Z`
- Last outbound sync: `2026-06-26T21:59:50.608738Z`
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
- Current pulse started: `2026-06-26T22:00:09.352875Z`
- Last body pulse: `2026-06-26T18:00:08.737321Z`
- Last pulse commit: `4af680e1`
- Next scheduled pulse: `2026-06-27T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-26T22:00:09.251324Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-26T21:55:28.856796Z`; age seconds: `281`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `353719`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-26T21:59:50.608738Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-26T22:00:09.823035Z`; age seconds: `0`
