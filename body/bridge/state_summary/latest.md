# Bridge State Summary

- Generated at: `2026-06-17T14:00:04.764191Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T13:59:55.905473+00:00`
- Heartbeat count: `117514`
- Heartbeat last gap seconds: `10.007856`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1177681`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `0.487568`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T13:59:56.393057+00:00`

## Body Health

- Health generated at: `2026-06-17T13:55:36.075554Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.25 / 0.31 / 0.18`
- RAM used percent: `14.12`
- Swap used percent: `0.0`
- Root disk used percent: `7.8`

## Bridge Sync

- Last inbound sync: `2026-06-17T13:59:47.007138Z`
- Last outbound sync: `2026-06-17T13:59:47.722857Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `c982736f`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-autoreply-agents-root-test-001`
- Last processed status: `pending_codex`
- Processed count: `17`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-17T14:00:04.135187Z`
- Last body pulse: `2026-06-17T10:00:08.535178Z`
- Last pulse commit: `f7940c5c`
- Next scheduled pulse: `2026-06-17T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T13:59:56.393057Z`; age seconds: `8`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T13:55:36.075554Z`; age seconds: `268`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T11:55:46.761261Z`; age seconds: `7458`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T13:59:47.722857Z`; age seconds: `17`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T14:00:04.693941Z`; age seconds: `0`
