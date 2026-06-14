# Bridge State Summary

- Generated at: `2026-06-14T18:36:34.769850Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T18:36:30.104619+00:00`
- Heartbeat count: `93299`
- Heartbeat last gap seconds: `10.007637`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `935071`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `8.540339`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T18:36:28.637333+00:00`

## Body Health

- Health generated at: `2026-06-14T18:29:48.048893Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.14 / 0.16 / 0.15`
- RAM used percent: `13.64`
- Swap used percent: `0.0`
- Root disk used percent: `7.75`

## Bridge Sync

- Last inbound sync: `2026-06-14T18:36:34.598362Z`
- Last outbound sync: `2026-06-14T18:36:04.377234Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `312f040c`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-codex-autoreply-format-self-check-001`
- Last processed status: `pending_codex`
- Processed count: `12`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-14T18:00:06.762058Z`
- Last pulse commit: `d7e055bd`
- Next scheduled pulse: `Mon 2026-06-15 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T18:36:30.104619Z`; age seconds: `4`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T18:29:48.048893Z`; age seconds: `406`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T15:11:51.115458Z`; age seconds: `12283`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T18:36:34.598362Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T18:00:06.762058Z`; age seconds: `2188`
