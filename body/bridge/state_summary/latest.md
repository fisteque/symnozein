# Bridge State Summary

- Generated at: `2026-07-23T02:00:06.776340Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-23T01:59:58.458957+00:00`
- Heartbeat count: `423568`
- Heartbeat last gap seconds: `10.00755`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4244883`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.659697`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-23T02:00:06.118670+00:00`

## Body Health

- Health generated at: `2026-07-23T01:50:55.454218Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `19.9`
- Swap used percent: `0.0`
- Root disk used percent: `8.53`

## Bridge Sync

- Last inbound sync: `2026-07-23T01:59:56.883616Z`
- Last outbound sync: `2026-07-23T01:59:57.753276Z`
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
- Current pulse started: `2026-07-23T02:00:06.200733Z`
- Last body pulse: `2026-07-22T22:00:03.339674Z`
- Last pulse commit: `bb069f97`
- Next scheduled pulse: `2026-07-23T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-23T02:00:06.118670Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-23T01:50:55.454218Z`; age seconds: `551`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1921257`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-23T01:59:57.753276Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-23T02:00:06.699681Z`; age seconds: `0`
