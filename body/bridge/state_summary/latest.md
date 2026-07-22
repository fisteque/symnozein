# Bridge State Summary

- Generated at: `2026-07-22T10:00:07.929108Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-22T10:00:06.269868+00:00`
- Heartbeat count: `417822`
- Heartbeat last gap seconds: `10.004195`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4187285`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `0.961533`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-22T10:00:07.231417+00:00`

## Body Health

- Health generated at: `2026-07-22T09:59:27.278574Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.0 / 0.05 / 0.08`
- RAM used percent: `19.87`
- Swap used percent: `0.0`
- Root disk used percent: `8.51`

## Bridge Sync

- Last inbound sync: `2026-07-22T09:59:58.035298Z`
- Last outbound sync: `2026-07-22T09:59:58.871337Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `f1c00bdd`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-07-22T10:00:07.346446Z`
- Last body pulse: `2026-07-22T06:00:10.294571Z`
- Last pulse commit: `304d2cb5`
- Next scheduled pulse: `2026-07-22T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-22T10:00:07.231417Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-22T09:59:27.278574Z`; age seconds: `40`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1863658`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-22T09:59:58.871337Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-22T10:00:07.871620Z`; age seconds: `0`
