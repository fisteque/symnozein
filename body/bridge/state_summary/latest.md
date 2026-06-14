# Bridge State Summary

- Generated at: `2026-06-14T22:00:04.662238Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T21:59:59.794091+00:00`
- Heartbeat count: `94515`
- Heartbeat last gap seconds: `10.004174`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `947281`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `6.277662`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T21:59:56.067597+00:00`

## Body Health

- Health generated at: `2026-06-14T21:50:05.378165Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.01 / 0.1 / 0.07`
- RAM used percent: `13.55`
- Swap used percent: `0.0`
- Root disk used percent: `7.75`

## Bridge Sync

- Last inbound sync: `2026-06-14T21:59:56.655731Z`
- Last outbound sync: `2026-06-14T21:59:57.362714Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-14T22:00:04.143410Z`
- Last body pulse: `2026-06-14T18:00:06.762058Z`
- Last pulse commit: `d7e055bd`
- Next scheduled pulse: `2026-06-15T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T21:59:59.794091Z`; age seconds: `4`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T21:50:05.378165Z`; age seconds: `599`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `8800`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T21:59:57.362714Z`; age seconds: `7`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T22:00:04.607598Z`; age seconds: `0`
