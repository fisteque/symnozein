# Bridge State Summary

- Generated at: `2026-06-29T22:00:07.274109Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-29T22:00:05.178995+00:00`
- Heartbeat count: `223846`
- Heartbeat last gap seconds: `10.007589`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2243284`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.474832`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-29T22:00:06.653844+00:00`

## Body Health

- Health generated at: `2026-06-29T21:51:55.959661Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.1 / 0.05 / 0.01`
- RAM used percent: `16.17`
- Swap used percent: `0.0`
- Root disk used percent: `8.01`

## Bridge Sync

- Last inbound sync: `2026-06-29T21:59:57.295433Z`
- Last outbound sync: `2026-06-29T21:59:58.045381Z`
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
- Current pulse started: `2026-06-29T22:00:06.768350Z`
- Last body pulse: `2026-06-29T18:00:08.088045Z`
- Last pulse commit: `56540ad2`
- Next scheduled pulse: `2026-06-30T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-29T22:00:06.653844Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-29T21:51:55.959661Z`; age seconds: `491`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `612917`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-29T21:59:58.045381Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-29T22:00:07.219858Z`; age seconds: `0`
