# Bridge State Summary

- Generated at: `2026-07-26T16:32:25.463116Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T16:32:18.761850+00:00`
- Heartbeat count: `454659`
- Heartbeat last gap seconds: `10.008324`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4556422`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `6`
- Watchdog last heartbeat age seconds: `5.751661`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T16:32:24.513528+00:00`

## Body Health

- Health generated at: `2026-07-26T16:28:54.119311Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `11.73`
- Swap used percent: `0.0`
- Root disk used percent: `8.86`

## Bridge Sync

- Last inbound sync: `2026-07-26T16:32:25.302637Z`
- Last outbound sync: `2026-07-26T16:31:56.179325Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `a69f23e8`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260726-codex-read-runtime-agents-root-001`
- Last processed status: `pending_codex`
- Processed count: `27`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-26T14:00:03.676855Z`
- Last pulse commit: `dfa07e4e`
- Next scheduled pulse: `Sun 2026-07-26 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T16:32:24.513528Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T16:28:54.119311Z`; age seconds: `211`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T16:31:25.502470Z`; age seconds: `59`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T16:32:25.302637Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T14:00:03.676855Z`; age seconds: `9141`
