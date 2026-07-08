# Bridge State Summary

- Generated at: `2026-07-08T06:00:09.494693Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-08T06:00:07.700793+00:00`
- Heartbeat count: `295699`
- Heartbeat last gap seconds: `10.007603`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2963286`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `1.172112`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-08T06:00:08.872921+00:00`

## Body Health

- Health generated at: `2026-07-08T05:59:18.907700Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.16 / 0.15 / 0.13`
- RAM used percent: `17.58`
- Swap used percent: `0.0`
- Root disk used percent: `8.15`

## Bridge Sync

- Last inbound sync: `2026-07-08T05:59:49.556290Z`
- Last outbound sync: `2026-07-08T05:59:50.319821Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

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
- Current pulse started: `2026-07-08T06:00:08.971688Z`
- Last body pulse: `2026-07-08T02:00:06.138157Z`
- Last pulse commit: `601c5ae7`
- Next scheduled pulse: `2026-07-08T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-08T06:00:08.872921Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-08T05:59:18.907700Z`; age seconds: `50`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `639659`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-08T05:59:50.319821Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-08T06:00:09.444277Z`; age seconds: `0`
