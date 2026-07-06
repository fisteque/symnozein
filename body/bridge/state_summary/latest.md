# Bridge State Summary

- Generated at: `2026-07-06T14:00:39.757025Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-06T14:00:36.335205+00:00`
- Heartbeat count: `281329`
- Heartbeat last gap seconds: `10.007579`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2819316`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `2.38112`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-06T14:00:38.716341+00:00`

## Body Health

- Health generated at: `2026-07-06T13:55:58.440229Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.01 / 0.07 / 0.08`
- RAM used percent: `17.17`
- Swap used percent: `0.0`
- Root disk used percent: `8.13`

## Bridge Sync

- Last inbound sync: `2026-07-06T14:00:39.594158Z`
- Last outbound sync: `2026-07-06T13:59:40.101199Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `3129f63c`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `2`
- Needs human count: `1`
- Last processed message: `msg-20260630-codex-check-last-message-processing-state-001`
- Last processed status: `pending_codex`
- Processed count: `26`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-06T14:00:11.045692Z`
- Last pulse commit: `03fcad5b`
- Next scheduled pulse: `Mon 2026-07-06 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-06T14:00:38.716341Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-06T13:55:58.440229Z`; age seconds: `281`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `495690`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-06T14:00:39.594158Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-06T14:00:11.045692Z`; age seconds: `28`
