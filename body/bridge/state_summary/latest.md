# Bridge State Summary

- Generated at: `2026-06-30T22:00:07.940409Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-30T22:00:02.095166+00:00`
- Heartbeat count: `232470`
- Heartbeat last gap seconds: `10.005185`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2329685`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `5.209108`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-30T22:00:07.304290+00:00`

## Body Health

- Health generated at: `2026-06-30T21:53:56.848880Z`
- CPU temperature C: `50.7`
- Load average 1m / 5m / 15m: `0.06 / 0.2 / 0.12`
- RAM used percent: `16.45`
- Swap used percent: `0.0`
- Root disk used percent: `8.03`

## Bridge Sync

- Last inbound sync: `2026-06-30T21:59:57.977432Z`
- Last outbound sync: `2026-06-30T21:59:58.752041Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `666a6c6f`

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
- Current pulse started: `2026-06-30T22:00:07.418282Z`
- Last body pulse: `2026-06-30T18:00:10.248076Z`
- Last pulse commit: `8eb03a4a`
- Next scheduled pulse: `2026-07-01T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-30T22:00:07.304290Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-30T21:53:56.848880Z`; age seconds: `371`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `6058`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-30T21:59:58.752041Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-30T22:00:07.884708Z`; age seconds: `0`
