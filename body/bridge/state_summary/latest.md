# Bridge State Summary

- Generated at: `2026-07-07T02:00:08.976339Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-07T01:59:59.469290+00:00`
- Heartbeat count: `285640`
- Heartbeat last gap seconds: `10.00424`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2862486`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `8.854243`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-07T02:00:08.323549+00:00`

## Body Health

- Health generated at: `2026-07-07T01:56:58.160753Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.03 / 0.08`
- RAM used percent: `17.4`
- Swap used percent: `0.0`
- Root disk used percent: `8.14`

## Bridge Sync

- Last inbound sync: `2026-07-07T01:59:58.962982Z`
- Last outbound sync: `2026-07-07T01:59:59.823797Z`
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
- Current pulse started: `2026-07-07T02:00:08.433449Z`
- Last body pulse: `2026-07-06T22:00:10.691236Z`
- Last pulse commit: `a2581b36`
- Next scheduled pulse: `2026-07-07T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-07T02:00:08.323549Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-07T01:56:58.160753Z`; age seconds: `190`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `538859`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-07T01:59:59.823797Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-07T02:00:08.922775Z`; age seconds: `0`
