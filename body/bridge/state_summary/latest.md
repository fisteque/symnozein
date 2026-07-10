# Bridge State Summary

- Generated at: `2026-07-10T18:00:01.091940Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-10T17:59:54.513832+00:00`
- Heartbeat count: `317250`
- Heartbeat last gap seconds: `10.007606`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3179278`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.945881`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-10T18:00:00.459728+00:00`

## Body Health

- Health generated at: `2026-07-10T17:54:50.181205Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.13 / 0.11 / 0.04`
- RAM used percent: `17.85`
- Swap used percent: `0.0`
- Root disk used percent: `8.22`

## Bridge Sync

- Last inbound sync: `2026-07-10T17:59:39.734119Z`
- Last outbound sync: `2026-07-10T17:59:40.515332Z`
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
- Current pulse started: `2026-07-10T18:00:00.548731Z`
- Last body pulse: `2026-07-10T14:00:11.383013Z`
- Last pulse commit: `1c163c43`
- Next scheduled pulse: `2026-07-11T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-10T18:00:00.459728Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-10T17:54:50.181205Z`; age seconds: `310`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `855651`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-10T17:59:40.515332Z`; age seconds: `20`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-10T18:00:01.038238Z`; age seconds: `0`
