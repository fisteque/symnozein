# Bridge State Summary

- Generated at: `2026-06-18T02:00:04.475354Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-18T02:00:01.181460+00:00`
- Heartbeat count: `121825`
- Heartbeat last gap seconds: `10.007535`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1220881`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.635305`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-18T02:00:03.816783+00:00`

## Body Health

- Health generated at: `2026-06-18T01:56:43.603987Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.04 / 0.05 / 0.01`
- RAM used percent: `14.1`
- Swap used percent: `0.0`
- Root disk used percent: `7.84`

## Bridge Sync

- Last inbound sync: `2026-06-18T01:59:54.473746Z`
- Last outbound sync: `2026-06-18T01:59:55.172601Z`
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
- Current pulse started: `2026-06-18T02:00:03.936343Z`
- Last body pulse: `2026-06-17T22:00:05.602753Z`
- Last pulse commit: `a3d73f00`
- Next scheduled pulse: `2026-06-18T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-18T02:00:03.816783Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-18T01:56:43.603987Z`; age seconds: `200`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T17:17:39.057579Z`; age seconds: `31345`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-18T01:59:55.172601Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-18T02:00:04.418726Z`; age seconds: `0`
