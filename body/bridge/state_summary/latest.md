# Bridge State Summary

- Generated at: `2026-07-01T18:00:01.100789Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-01T17:59:53.175716+00:00`
- Heartbeat count: `239656`
- Heartbeat last gap seconds: `10.007586`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2401678`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `7.76913`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-01T18:00:00.944858+00:00`

## Body Health

- Health generated at: `2026-07-01T17:55:40.728639Z`
- CPU temperature C: `49.6`
- Load average 1m / 5m / 15m: `0.04 / 0.09 / 0.04`
- RAM used percent: `16.61`
- Swap used percent: `0.0`
- Root disk used percent: `8.1`

## Bridge Sync

- Last inbound sync: `2026-07-01T17:59:59.684606Z`
- Last outbound sync: `2026-07-01T18:00:00.496016Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `6c59e9ec`

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
- Current pulse started: `2026-07-01T18:00:00.611985Z`
- Last body pulse: `2026-07-01T14:00:02.836513Z`
- Last pulse commit: `bdb981ea`
- Next scheduled pulse: `2026-07-02T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-01T18:00:00.944858Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-01T17:55:40.728639Z`; age seconds: `260`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `78051`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-01T18:00:00.496016Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-01T18:00:01.049664Z`; age seconds: `0`
