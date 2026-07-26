# Bridge State Summary

- Generated at: `2026-07-26T17:13:09.038499Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-26T17:13:00.974074+00:00`
- Heartbeat count: `454903`
- Heartbeat last gap seconds: `10.005196`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4558866`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.124883`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-26T17:13:08.098976+00:00`

## Body Health

- Health generated at: `2026-07-26T17:08:57.849544Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.16 / 0.1 / 0.03`
- RAM used percent: `11.8`
- Swap used percent: `0.0`
- Root disk used percent: `8.86`

## Bridge Sync

- Last inbound sync: `2026-07-26T17:13:08.823331Z`
- Last outbound sync: `2026-07-26T17:12:39.642434Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `fedd7bba`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260726-codex-read-runtime-bridge-state-001`
- Last processed status: `pending_codex`
- Processed count: `28`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-07-26T14:00:03.676855Z`
- Last pulse commit: `dfa07e4e`
- Next scheduled pulse: `Sun 2026-07-26 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-26T17:13:08.098976Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-26T17:08:57.849544Z`; age seconds: `251`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-07-26T17:11:39.068722Z`; age seconds: `89`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-26T17:13:08.823331Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-26T14:00:03.676855Z`; age seconds: `11585`
