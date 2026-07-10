# Bridge State Summary

- Generated at: `2026-07-10T02:00:01.106890Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-10T01:59:40.162920+00:00`
- Heartbeat count: `311502`
- Heartbeat last gap seconds: `10.005294`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3121678`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `20`
- Watchdog last heartbeat age seconds: `20.029201`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-10T02:00:00.192137+00:00`

## Body Health

- Health generated at: `2026-07-10T01:53:19.664420Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.41 / 0.17 / 0.09`
- RAM used percent: `17.72`
- Swap used percent: `0.0`
- Root disk used percent: `8.22`

## Bridge Sync

- Last inbound sync: `2026-07-10T01:59:50.875199Z`
- Last outbound sync: `2026-07-10T01:59:51.734554Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

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
- Current pulse started: `2026-07-10T02:00:00.300361Z`
- Last body pulse: `2026-07-09T22:00:09.830891Z`
- Last pulse commit: `e6b8cf82`
- Next scheduled pulse: `2026-07-10T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-10T02:00:00.192137Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-10T01:53:19.664420Z`; age seconds: `401`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `798051`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-10T01:59:51.734554Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-10T02:00:01.052799Z`; age seconds: `0`
