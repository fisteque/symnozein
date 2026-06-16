# Bridge State Summary

- Generated at: `2026-06-16T14:00:03.187651Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-16T13:59:55.120834+00:00`
- Heartbeat count: `108890`
- Heartbeat last gap seconds: `10.004134`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1091280`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.216169`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-16T14:00:02.337481+00:00`

## Body Health

- Health generated at: `2026-06-16T13:53:31.892509Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.04 / 0.16 / 0.12`
- RAM used percent: `13.76`
- Swap used percent: `0.0`
- Root disk used percent: `7.78`

## Bridge Sync

- Last inbound sync: `2026-06-16T13:59:52.967668Z`
- Last outbound sync: `2026-06-16T13:59:53.692305Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-16T14:00:02.452388Z`
- Last body pulse: `2026-06-16T10:00:04.318482Z`
- Last pulse commit: `30d4f9a1`
- Next scheduled pulse: `2026-06-16T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-16T14:00:02.337481Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-16T13:53:31.892509Z`; age seconds: `391`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `152798`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-16T13:59:53.692305Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-16T14:00:03.133860Z`; age seconds: `0`
