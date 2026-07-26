# Bridge State Summary

- Generated at: `2026-07-26T08:59:52.599870Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T08:59:46.401806+00:00`
- Heartbeat count: `451950`
- Heartbeat last gap seconds: `10.008707`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4529269`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.274446`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T08:59:51.676267+00:00`

## Body Health

- Health generated at: `2026-07-26T08:58:11.511629Z`
- CPU temperature C: `50.15`
- Load average 1m / 5m / 15m: `0.44 / 0.43 / 0.37`
- RAM used percent: `29.01`
- Swap used percent: `0.0`
- Root disk used percent: `8.75`

## Bridge Sync

- Last inbound sync: `2026-07-26T08:59:52.375183Z`
- Last outbound sync: `2026-07-26T08:59:23.128179Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `36b5c7b7`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-26T06:00:11.947548Z`
- Last pulse commit: `af00fdf6`
- Next scheduled pulse: `Sun 2026-07-26 12:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T08:59:51.676267Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T08:58:11.511629Z`; age seconds: `101`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2205642`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T08:59:52.375183Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T06:00:11.947548Z`; age seconds: `10780`
