# Bridge State Summary

- Generated at: `2026-06-16T18:00:05.013144Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-16T17:59:56.072095+00:00`
- Heartbeat count: `110327`
- Heartbeat last gap seconds: `10.008511`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1105682`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `6.319504`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-16T18:00:02.391615+00:00`

## Body Health

- Health generated at: `2026-06-16T17:53:51.996345Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.21 / 0.11 / 0.03`
- RAM used percent: `13.67`
- Swap used percent: `0.0`
- Root disk used percent: `7.78`

## Bridge Sync

- Last inbound sync: `2026-06-16T18:00:03.169175Z`
- Last outbound sync: `2026-06-16T18:00:04.408061Z`
- Last outbound sync status: `error`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-16T18:00:04.523648Z`
- Last body pulse: `2026-06-16T10:00:04.318482Z`
- Last pulse commit: `30d4f9a1`
- Next scheduled pulse: `2026-06-17T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-16T18:00:02.391615Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-16T17:53:51.996345Z`; age seconds: `373`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `167200`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-16T18:00:04.408061Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-16T18:00:04.956486Z`; age seconds: `0`
