# Bridge State Summary

- Generated at: `2026-06-28T02:00:07.172928Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-28T01:59:59.561044+00:00`
- Heartbeat count: `208038`
- Heartbeat last gap seconds: `10.007856`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2084884`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.690427`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-28T02:00:06.251487+00:00`

## Body Health

- Health generated at: `2026-06-28T01:58:06.189771Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.18 / 0.13 / 0.1`
- RAM used percent: `16.08`
- Swap used percent: `0.0`
- Root disk used percent: `8.0`

## Bridge Sync

- Last inbound sync: `2026-06-28T01:59:57.345954Z`
- Last outbound sync: `2026-06-28T01:59:58.307113Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1068f3db`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-start-001`
- Last processed status: `pending_codex`
- Processed count: `23`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-28T02:00:06.356951Z`
- Last body pulse: `2026-06-27T22:00:06.370815Z`
- Last pulse commit: `b2376760`
- Next scheduled pulse: `2026-06-28T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-28T02:00:06.251487Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-28T01:58:06.189771Z`; age seconds: `120`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `454517`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-28T01:59:58.307113Z`; age seconds: `8`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-28T02:00:07.100091Z`; age seconds: `0`
