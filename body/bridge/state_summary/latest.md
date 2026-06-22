# Bridge State Summary

- Generated at: `2026-06-22T15:16:55.819586Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T15:16:47.200434+00:00`
- Heartbeat count: `161079`
- Heartbeat last gap seconds: `10.005417`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1614292`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.637957`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T15:16:54.838406+00:00`

## Body Health

- Health generated at: `2026-06-22T15:16:04.168569Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.0 / 0.08 / 0.07`
- RAM used percent: `15.34`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-22T15:16:55.499335Z`
- Last outbound sync: `2026-06-22T15:16:26.126075Z`
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

- Current pulse status: `idle`
- Last body pulse: `2026-06-22T14:00:11.863987Z`
- Last pulse commit: `9c300d2a`
- Next scheduled pulse: `Mon 2026-06-22 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T15:16:54.838406Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T15:16:04.168569Z`; age seconds: `51`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `113118`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T15:16:55.499335Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T14:00:11.863987Z`; age seconds: `4603`
