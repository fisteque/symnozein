# Bridge State Summary

- Generated at: `2026-06-14T19:33:54.202975Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T19:33:53.303246+00:00`
- Heartbeat count: `93639`
- Heartbeat last gap seconds: `10.004172`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `938511`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `0.168297`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T19:33:53.471561+00:00`

## Body Health

- Health generated at: `2026-06-14T19:29:53.184080Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.09 / 0.05 / 0.01`
- RAM used percent: `13.45`
- Swap used percent: `0.0`
- Root disk used percent: `7.75`

## Bridge Sync

- Last inbound sync: `2026-06-14T19:33:54.037896Z`
- Last outbound sync: `2026-06-14T19:33:25.061631Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `54a30cea`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-14T18:00:06.762058Z`
- Last pulse commit: `d7e055bd`
- Next scheduled pulse: `Mon 2026-06-15 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T19:33:53.471561Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T19:29:53.184080Z`; age seconds: `241`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `29`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T19:33:54.037896Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T18:00:06.762058Z`; age seconds: `5627`
