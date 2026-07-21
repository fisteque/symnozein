# Bridge State Summary

- Generated at: `2026-07-21T02:00:07.844296Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-21T02:00:03.983602+00:00`
- Heartbeat count: `406327`
- Heartbeat last gap seconds: `10.004488`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4072084`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `1.653081`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-21T02:00:05.636698+00:00`

## Body Health

- Health generated at: `2026-07-21T01:56:45.475741Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.0 / 0.01 / 0.04`
- RAM used percent: `19.93`
- Swap used percent: `0.0`
- Root disk used percent: `8.49`

## Bridge Sync

- Last inbound sync: `2026-07-21T02:00:06.351427Z`
- Last outbound sync: `2026-07-21T02:00:07.162872Z`
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
- Current pulse started: `2026-07-21T02:00:07.267997Z`
- Last body pulse: `2026-07-20T22:00:08.187048Z`
- Last pulse commit: `fcc8b3c8`
- Next scheduled pulse: `2026-07-21T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-21T02:00:05.636698Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-21T01:56:45.475741Z`; age seconds: `202`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1748458`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-21T02:00:07.162872Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-21T02:00:07.791449Z`; age seconds: `0`
