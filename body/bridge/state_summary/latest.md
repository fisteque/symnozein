# Bridge State Summary

- Generated at: `2026-07-20T14:00:07.636773Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-20T13:59:59.179860+00:00`
- Heartbeat count: `402016`
- Heartbeat last gap seconds: `10.00866`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4028884`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `5.916654`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-20T14:00:05.096531+00:00`

## Body Health

- Health generated at: `2026-07-20T13:55:44.126109Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.02 / 0.05 / 0.06`
- RAM used percent: `19.51`
- Swap used percent: `0.0`
- Root disk used percent: `8.48`

## Bridge Sync

- Last inbound sync: `2026-07-20T14:00:05.834902Z`
- Last outbound sync: `2026-07-20T14:00:06.888251Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `f1c00bdd`

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
- Current pulse started: `2026-07-20T14:00:06.997614Z`
- Last body pulse: `2026-07-20T10:00:07.009634Z`
- Last pulse commit: `d748c9c2`
- Next scheduled pulse: `2026-07-20T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-20T14:00:05.096531Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-20T13:55:44.126109Z`; age seconds: `263`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1705257`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-20T14:00:06.888251Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-20T14:00:07.582737Z`; age seconds: `0`
