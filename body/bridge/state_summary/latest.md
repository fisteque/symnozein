# Bridge State Summary

- Generated at: `2026-07-24T14:00:01.737109Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-24T13:59:59.776693+00:00`
- Heartbeat count: `436503`
- Heartbeat last gap seconds: `10.007335`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4374478`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `1.280956`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-24T14:00:01.057676+00:00`

## Body Health

- Health generated at: `2026-07-24T13:54:10.575768Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.19 / 0.18 / 0.1`
- RAM used percent: `20.29`
- Swap used percent: `0.0`
- Root disk used percent: `8.55`

## Bridge Sync

- Last inbound sync: `2026-07-24T13:59:41.742688Z`
- Last outbound sync: `2026-07-24T13:59:42.629381Z`
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
- Current pulse started: `2026-07-24T14:00:01.143800Z`
- Last body pulse: `2026-07-24T10:00:12.770429Z`
- Last pulse commit: `45a9f5c0`
- Next scheduled pulse: `2026-07-24T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-24T14:00:01.057676Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-24T13:54:10.575768Z`; age seconds: `351`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2050851`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-24T13:59:42.629381Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-24T14:00:01.679778Z`; age seconds: `0`
