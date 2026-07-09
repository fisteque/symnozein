# Bridge State Summary

- Generated at: `2026-07-09T02:00:01.490690Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-09T01:59:57.467164+00:00`
- Heartbeat count: `302880`
- Heartbeat last gap seconds: `10.004351`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3035278`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `1.882287`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-09T01:59:59.349466+00:00`

## Body Health

- Health generated at: `2026-07-09T01:51:08.701276Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.0 / 0.02 / 0.0`
- RAM used percent: `17.47`
- Swap used percent: `0.0`
- Root disk used percent: `8.21`

## Bridge Sync

- Last inbound sync: `2026-07-09T02:00:00.041495Z`
- Last outbound sync: `2026-07-09T02:00:00.844587Z`
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
- Current pulse started: `2026-07-09T02:00:00.942857Z`
- Last body pulse: `2026-07-08T22:00:09.704523Z`
- Last pulse commit: `0d5b36bf`
- Next scheduled pulse: `2026-07-09T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-09T01:59:59.349466Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-09T01:51:08.701276Z`; age seconds: `532`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `711651`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-09T02:00:00.844587Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-09T02:00:01.435318Z`; age seconds: `0`
