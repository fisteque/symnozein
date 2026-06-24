# Bridge State Summary

- Generated at: `2026-06-24T14:00:02.457247Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-24T13:59:59.563671+00:00`
- Heartbeat count: `177860`
- Heartbeat last gap seconds: `10.007693`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1782479`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `6.213107`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-24T13:59:55.769100+00:00`

## Body Health

- Health generated at: `2026-06-24T13:50:14.940858Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.06`
- RAM used percent: `15.28`
- Swap used percent: `0.0`
- Root disk used percent: `7.97`

## Bridge Sync

- Last inbound sync: `2026-06-24T14:00:00.705131Z`
- Last outbound sync: `2026-06-24T14:00:01.546192Z`
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
- Current pulse started: `2026-06-24T14:00:01.655826Z`
- Last body pulse: `2026-06-24T10:00:08.982057Z`
- Last pulse commit: `5e432ebf`
- Next scheduled pulse: `2026-06-24T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-24T13:59:59.563671Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-24T13:50:14.940858Z`; age seconds: `587`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:44:50.013988Z`; age seconds: `152112`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-24T14:00:01.546192Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-24T14:00:02.402260Z`; age seconds: `0`
