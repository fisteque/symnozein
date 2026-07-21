# Bridge State Summary

- Generated at: `2026-07-21T14:00:08.017209Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-21T14:00:07.258722+00:00`
- Heartbeat count: `410640`
- Heartbeat last gap seconds: `10.020375`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4115285`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `8.489389`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-21T14:00:05.727752+00:00`

## Body Health

- Health generated at: `2026-07-21T13:57:45.642887Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `19.55`
- Swap used percent: `0.0`
- Root disk used percent: `8.5`

## Bridge Sync

- Last inbound sync: `2026-07-21T14:00:06.469641Z`
- Last outbound sync: `2026-07-21T14:00:07.350972Z`
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
- Current pulse started: `2026-07-21T14:00:07.459737Z`
- Last body pulse: `2026-07-21T10:00:09.595093Z`
- Last pulse commit: `bac3716a`
- Next scheduled pulse: `2026-07-21T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-21T14:00:07.258722Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-21T13:57:45.642887Z`; age seconds: `142`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1791658`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-21T14:00:07.350972Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-21T14:00:07.961988Z`; age seconds: `0`
