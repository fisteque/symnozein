# Bridge State Summary

- Generated at: `2026-06-14T08:29:06.698831Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T08:28:59.159285+00:00`
- Heartbeat count: `89661`
- Heartbeat last gap seconds: `10.007348`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `898623`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.254587`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T08:29:05.413887+00:00`

## Body Health

- Health generated at: `2026-06-14T08:28:55.478188Z`
- CPU temperature C: `47.95`
- Load average 1m / 5m / 15m: `0.12 / 0.04 / 0.01`
- RAM used percent: `14.86`
- Swap used percent: `0.0`
- Root disk used percent: `7.74`

## Bridge Sync

- Last inbound sync: `2026-06-14T08:29:06.039776Z`
- Last outbound sync: `2026-06-14T08:28:36.565364Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `4934b4e4`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
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

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T08:29:05.413887Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T08:28:55.478188Z`; age seconds: `11`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-13T19:01:34.718722Z`; age seconds: `48451`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T08:29:06.039776Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T06:00:06.237944Z`; age seconds: `8940`
