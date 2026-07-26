# Bridge State Summary

- Generated at: `2026-07-26T09:32:45.683097Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T09:32:38.648232+00:00`
- Heartbeat count: `452147`
- Heartbeat last gap seconds: `10.023051`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4531242`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.147166`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T09:32:44.795415+00:00`

## Body Health

- Health generated at: `2026-07-26T09:28:14.127744Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.02 / 0.1`
- RAM used percent: `29.19`
- Swap used percent: `0.0`
- Root disk used percent: `8.75`

## Bridge Sync

- Last inbound sync: `2026-07-26T09:32:45.516182Z`
- Last outbound sync: `2026-07-26T09:32:16.650953Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `be6d1166`

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

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T09:32:44.795415Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T09:28:14.127744Z`; age seconds: `271`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2207615`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T09:32:45.516182Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T06:00:11.947548Z`; age seconds: `12753`
