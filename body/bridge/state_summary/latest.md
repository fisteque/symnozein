# Bridge State Summary

- Generated at: `2026-06-21T08:07:19.048489Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-21T08:07:09.510839+00:00`
- Heartbeat count: `149890`
- Heartbeat last gap seconds: `10.004508`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1502116`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `8.702343`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-21T08:07:18.213198+00:00`

## Body Health

- Health generated at: `2026-06-21T08:03:27.329002Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.01 / 0.0 / 0.0`
- RAM used percent: `14.72`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-21T08:07:18.887144Z`
- Last outbound sync: `2026-06-21T08:06:49.575657Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `0ee533b3`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260620-codex-inspect-task-github-write-test-001`
- Last processed status: `ignored`
- Processed count: `21`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-21T06:00:09.927882Z`
- Last pulse commit: `292ec757`
- Next scheduled pulse: `Sun 2026-06-21 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-21T08:07:18.213198Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-21T08:03:27.329002Z`; age seconds: `231`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `941`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-21T08:07:18.887144Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-21T06:00:09.927882Z`; age seconds: `7629`
