# Bridge State Summary

- Generated at: `2026-06-21T14:00:09.361381Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-21T14:00:06.675476+00:00`
- Heartbeat count: `151999`
- Heartbeat last gap seconds: `10.007266`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1523286`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `2.064777`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-21T14:00:08.740268+00:00`

## Body Health

- Health generated at: `2026-06-21T13:53:58.200066Z`
- CPU temperature C: `48.5`
- Load average 1m / 5m / 15m: `0.07 / 0.02 / 0.0`
- RAM used percent: `14.98`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-21T13:59:49.306938Z`
- Last outbound sync: `2026-06-21T13:59:50.068336Z`
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
- Current pulse started: `2026-06-21T14:00:08.848454Z`
- Last body pulse: `2026-06-21T10:00:09.721804Z`
- Last pulse commit: `866dd11f`
- Next scheduled pulse: `2026-06-21T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-21T14:00:08.740268Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-21T13:53:58.200066Z`; age seconds: `371`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-21T07:51:37.304132Z`; age seconds: `22112`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-21T13:59:50.068336Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-21T14:00:09.304730Z`; age seconds: `0`
