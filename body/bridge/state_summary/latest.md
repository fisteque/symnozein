# Bridge State Summary

- Generated at: `2026-07-05T02:00:04.678834Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-05T02:00:04.116460+00:00`
- Heartbeat count: `268397`
- Heartbeat last gap seconds: `10.007091`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2689681`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `5.702278`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-05T01:59:59.811662+00:00`

## Body Health

- Health generated at: `2026-07-05T01:52:49.236063Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.1 / 0.09 / 0.07`
- RAM used percent: `16.86`
- Swap used percent: `0.0`
- Root disk used percent: `8.12`

## Bridge Sync

- Last inbound sync: `2026-07-05T01:59:40.456505Z`
- Last outbound sync: `2026-07-05T01:59:41.199968Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

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
- Current pulse started: `2026-07-05T02:00:04.135066Z`
- Last body pulse: `2026-07-04T22:00:06.054840Z`
- Last pulse commit: `c376922e`
- Next scheduled pulse: `2026-07-05T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-05T02:00:04.116460Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-05T01:52:49.236063Z`; age seconds: `435`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `366054`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-05T01:59:41.199968Z`; age seconds: `23`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-05T02:00:04.624575Z`; age seconds: `0`
