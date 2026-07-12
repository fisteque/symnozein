# Bridge State Summary

- Generated at: `2026-07-12T14:00:06.640546Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-12T13:59:57.215218+00:00`
- Heartbeat count: `333058`
- Heartbeat last gap seconds: `10.004094`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3337683`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `9`
- Watchdog last heartbeat age seconds: `8.781032`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-12T14:00:05.996270+00:00`

## Body Health

- Health generated at: `2026-07-12T13:58:55.000842Z`
- CPU temperature C: `48.5`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `18.45`
- Swap used percent: `0.0`
- Root disk used percent: `8.23`

## Bridge Sync

- Last inbound sync: `2026-07-12T13:59:56.645248Z`
- Last outbound sync: `2026-07-12T13:59:57.425959Z`
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
- Current pulse started: `2026-07-12T14:00:06.092244Z`
- Last body pulse: `2026-07-12T10:00:05.212814Z`
- Last pulse commit: `c2ddb75e`
- Next scheduled pulse: `2026-07-12T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-12T14:00:05.996270Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-12T13:58:55.000842Z`; age seconds: `71`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1014056`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-12T13:59:57.425959Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-12T14:00:06.584950Z`; age seconds: `0`
