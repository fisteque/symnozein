# Bridge State Summary

- Generated at: `2026-06-21T18:00:04.766529Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-21T17:59:58.555126+00:00`
- Heartbeat count: `153437`
- Heartbeat last gap seconds: `10.007279`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1537681`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `9.864295`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-21T17:59:58.412159+00:00`

## Body Health

- Health generated at: `2026-06-21T17:54:18.058554Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.2 / 0.18 / 0.12`
- RAM used percent: `15.05`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-21T17:59:49.075661Z`
- Last outbound sync: `2026-06-21T17:59:49.843332Z`
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
- Current pulse started: `2026-06-21T18:00:04.138366Z`
- Last body pulse: `2026-06-21T14:00:10.632248Z`
- Last pulse commit: `d6db90fc`
- Next scheduled pulse: `2026-06-22T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-21T17:59:58.555126Z`; age seconds: `6`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-21T17:54:18.058554Z`; age seconds: `346`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `36507`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-21T17:59:49.843332Z`; age seconds: `14`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-21T18:00:04.709298Z`; age seconds: `0`
