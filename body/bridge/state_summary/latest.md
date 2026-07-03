# Bridge State Summary

- Generated at: `2026-07-03T09:24:15.699336Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-03T09:24:10.011129+00:00`
- Heartbeat count: `253812`
- Heartbeat last gap seconds: `10.007479`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2543532`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.838099`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-03T09:24:14.849245+00:00`

## Body Health

- Health generated at: `2026-07-03T09:19:04.437891Z`
- CPU temperature C: `47.95`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `16.76`
- Swap used percent: `0.0`
- Root disk used percent: `8.12`

## Bridge Sync

- Last inbound sync: `2026-07-03T09:24:15.537985Z`
- Last outbound sync: `2026-07-03T09:22:46.162070Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `6c59e9ec`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-03T06:00:09.769141Z`
- Last pulse commit: `8cb2cb41`
- Next scheduled pulse: `Fri 2026-07-03 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-03T09:24:14.849245Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-03T09:19:04.437891Z`; age seconds: `311`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `219905`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-03T09:24:15.537985Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-03T06:00:09.769141Z`; age seconds: `12245`
