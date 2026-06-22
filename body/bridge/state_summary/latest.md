# Bridge State Summary

- Generated at: `2026-06-22T16:29:21.675491Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T16:29:21.359902+00:00`
- Heartbeat count: `161514`
- Heartbeat last gap seconds: `10.00417`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1618638`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `9.343426`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T16:29:20.699173+00:00`

## Body Health

- Health generated at: `2026-06-22T16:26:10.528750Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.02 / 0.01 / 0.0`
- RAM used percent: `15.09`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-22T16:29:21.509339Z`
- Last outbound sync: `2026-06-22T16:28:51.604517Z`
- Last outbound sync status: `error`
- Last outbound commit: `47c27cfe`

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
- Last body pulse: `2026-06-22T14:00:11.863987Z`
- Last pulse commit: `9c300d2a`
- Next scheduled pulse: `Mon 2026-06-22 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T16:29:21.359902Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T16:26:10.528750Z`; age seconds: `191`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `117464`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T16:29:21.509339Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T14:00:11.863987Z`; age seconds: `8949`
