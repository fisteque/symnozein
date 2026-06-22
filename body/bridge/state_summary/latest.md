# Bridge State Summary

- Generated at: `2026-06-22T06:00:08.774761Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T06:00:01.752603+00:00`
- Heartbeat count: `157748`
- Heartbeat last gap seconds: `10.010211`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1580885`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.404047`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T06:00:08.156666+00:00`

## Body Health

- Health generated at: `2026-06-22T05:55:17.908926Z`
- CPU temperature C: `48.5`
- Load average 1m / 5m / 15m: `0.08 / 0.06 / 0.06`
- RAM used percent: `15.06`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-22T05:59:48.784818Z`
- Last outbound sync: `2026-06-22T05:59:49.525133Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `e92bf166`

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

- Current pulse status: `running`
- Current pulse started: `2026-06-22T06:00:08.256824Z`
- Last body pulse: `2026-06-22T02:00:10.481069Z`
- Last pulse commit: `a87c60ec`
- Next scheduled pulse: `2026-06-22T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T06:00:08.156666Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T05:55:17.908926Z`; age seconds: `290`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `79711`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T05:59:49.525133Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T06:00:08.715081Z`; age seconds: `0`
