# Bridge State Summary

- Generated at: `2026-06-21T22:00:01.013512Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-21T22:00:00.095375+00:00`
- Heartbeat count: `154874`
- Heartbeat last gap seconds: `10.005458`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1552078`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `8.858014`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-21T21:59:58.947947+00:00`

## Body Health

- Health generated at: `2026-06-21T21:54:38.583272Z`
- CPU temperature C: `48.5`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.0`
- RAM used percent: `15.22`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-21T21:59:59.624045Z`
- Last outbound sync: `2026-06-21T22:00:00.384010Z`
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
- Current pulse started: `2026-06-21T22:00:00.524911Z`
- Last body pulse: `2026-06-21T18:00:06.127599Z`
- Last pulse commit: `aa0a2d27`
- Next scheduled pulse: `2026-06-22T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-21T22:00:00.095375Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-21T21:54:38.583272Z`; age seconds: `322`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `50903`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-21T22:00:00.384010Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-21T22:00:00.959561Z`; age seconds: `0`
