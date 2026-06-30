# Bridge State Summary

- Generated at: `2026-06-30T19:12:43.908497Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T19:12:34.819184+00:00`
- Heartbeat count: `231468`
- Heartbeat last gap seconds: `10.004405`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2319640`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `8.278661`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T19:12:43.097861+00:00`

## Body Health

- Health generated at: `2026-06-30T19:03:41.992644Z`
- CPU temperature C: `51.25`
- Load average 1m / 5m / 15m: `0.1 / 0.06 / 0.01`
- RAM used percent: `16.2`
- Swap used percent: `0.0`
- Root disk used percent: `8.02`

## Bridge Sync

- Last inbound sync: `2026-06-30T19:12:43.747430Z`
- Last outbound sync: `2026-06-30T19:12:14.512448Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `79fb17a5`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260630-codex-diagnose-inbound-sync-exit2-001`
- Last processed status: `pending_codex`
- Processed count: `24`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-30T18:00:10.248076Z`
- Last pulse commit: `8eb03a4a`
- Next scheduled pulse: `Wed 2026-07-01 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T19:12:43.097861Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T19:03:41.992644Z`; age seconds: `541`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T19:10:43.379713Z`; age seconds: `120`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T19:12:43.747430Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T18:00:10.248076Z`; age seconds: `4353`
