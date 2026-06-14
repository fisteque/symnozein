# Bridge State Summary

- Generated at: `2026-06-14T08:13:04.931949Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T08:12:58.057862+00:00`
- Heartbeat count: `89565`
- Heartbeat last gap seconds: `10.005615`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `897662`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.948973`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T08:13:04.006850+00:00`

## Body Health

- Health generated at: `2026-06-14T08:08:53.816399Z`
- CPU temperature C: `43.0`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `14.67`
- Swap used percent: `0.0`
- Root disk used percent: `7.74`

## Bridge Sync

- Last inbound sync: `2026-06-14T08:13:04.760792Z`
- Last outbound sync: `2026-06-14T08:12:35.242000Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `1ea46fe7`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260613-cli-setup-body-pulse-001`
- Last processed status: `ok`
- Processed count: `11`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Last body pulse: `2026-06-14T06:00:06.237944Z`
- Last pulse commit: `90acf6c9`
- Next scheduled pulse: `Sun 2026-06-14 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T08:13:04.006850Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T08:08:53.816399Z`; age seconds: `251`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-13T19:01:34.718722Z`; age seconds: `47490`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T08:13:04.760792Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T06:00:06.237944Z`; age seconds: `7978`
