# Bridge State Summary

- Generated at: `2026-07-20T18:00:06.136441Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-20T18:00:00.887369+00:00`
- Heartbeat count: `403452`
- Heartbeat last gap seconds: `10.008553`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4043283`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.543675`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-20T18:00:05.431077+00:00`

## Body Health

- Health generated at: `2026-07-20T17:56:05.140270Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.14 / 0.13 / 0.05`
- RAM used percent: `19.77`
- Swap used percent: `0.0`
- Root disk used percent: `8.48`

## Bridge Sync

- Last inbound sync: `2026-07-20T17:59:46.085318Z`
- Last outbound sync: `2026-07-20T17:59:46.884485Z`
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
- Current pulse started: `2026-07-20T18:00:05.519146Z`
- Last body pulse: `2026-07-20T14:00:10.027627Z`
- Last pulse commit: `233a9d88`
- Next scheduled pulse: `2026-07-21T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-20T18:00:05.431077Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-20T17:56:05.140270Z`; age seconds: `240`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1719656`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-20T17:59:46.884485Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-20T18:00:06.060838Z`; age seconds: `0`
