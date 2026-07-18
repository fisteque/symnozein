# Bridge State Summary

- Generated at: `2026-07-18T14:00:04.646148Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-18T13:59:56.327020+00:00`
- Heartbeat count: `384777`
- Heartbeat last gap seconds: `10.007781`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3856081`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `1.05282`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-18T13:59:57.379856+00:00`

## Body Health

- Health generated at: `2026-07-18T13:51:26.649607Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.17 / 0.13 / 0.09`
- RAM used percent: `19.34`
- Swap used percent: `0.0`
- Root disk used percent: `8.46`

## Bridge Sync

- Last inbound sync: `2026-07-18T13:59:38.042940Z`
- Last outbound sync: `2026-07-18T13:59:38.882668Z`
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
- Current pulse started: `2026-07-18T14:00:04.127611Z`
- Last body pulse: `2026-07-18T10:00:08.849619Z`
- Last pulse commit: `a3c52fb7`
- Next scheduled pulse: `2026-07-18T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-18T13:59:57.379856Z`; age seconds: `7`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-18T13:51:26.649607Z`; age seconds: `517`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1532454`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-18T13:59:38.882668Z`; age seconds: `25`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-18T14:00:04.592788Z`; age seconds: `0`
