# Bridge State Summary

- Generated at: `2026-06-22T17:39:47.840466Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T17:39:44.561394+00:00`
- Heartbeat count: `161933`
- Heartbeat last gap seconds: `10.004543`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1622864`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.246866`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T17:39:46.808278+00:00`

## Body Health

- Health generated at: `2026-06-22T17:36:16.624401Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.0 / 0.04 / 0.01`
- RAM used percent: `15.22`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-22T17:39:47.677320Z`
- Last outbound sync: `2026-06-22T17:39:18.310196Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `a78f6a8a`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260620-codex-inspect-task-github-write-test-001`
- Last processed status: `ignored`
- Processed count: `21`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-22T14:00:11.863987Z`
- Last pulse commit: `9c300d2a`
- Next scheduled pulse: `Mon 2026-06-22 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T17:39:46.808278Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T17:36:16.624401Z`; age seconds: `211`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `121690`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T17:39:47.677320Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T14:00:11.863987Z`; age seconds: `13175`
