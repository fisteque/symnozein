# Bridge State Summary

- Generated at: `2026-07-08T02:00:04.642463Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-08T01:59:56.495340+00:00`
- Heartbeat count: `294261`
- Heartbeat last gap seconds: `10.004193`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2948881`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `2.051979`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-08T01:59:58.547334+00:00`

## Body Health

- Health generated at: `2026-07-08T01:58:58.563957Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.0 / 0.02 / 0.0`
- RAM used percent: `17.19`
- Swap used percent: `0.0`
- Root disk used percent: `8.15`

## Bridge Sync

- Last inbound sync: `2026-07-08T01:59:39.194815Z`
- Last outbound sync: `2026-07-08T01:59:39.983440Z`
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
- Current pulse started: `2026-07-08T02:00:04.123741Z`
- Last body pulse: `2026-07-07T22:00:10.976291Z`
- Last pulse commit: `a36fbb39`
- Next scheduled pulse: `2026-07-08T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-08T01:59:58.547334Z`; age seconds: `6`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-08T01:58:58.563957Z`; age seconds: `66`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `625254`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-08T01:59:39.983440Z`; age seconds: `24`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-08T02:00:04.586799Z`; age seconds: `0`
