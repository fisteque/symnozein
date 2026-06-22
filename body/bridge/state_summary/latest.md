# Bridge State Summary

- Generated at: `2026-06-22T19:37:49.341554Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T19:37:40.900245+00:00`
- Heartbeat count: `162640`
- Heartbeat last gap seconds: `10.005487`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1629946`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.452098`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T19:37:48.352361+00:00`

## Body Health

- Health generated at: `2026-06-22T19:36:26.844454Z`
- CPU temperature C: `52.9`
- Load average 1m / 5m / 15m: `0.59 / 0.19 / 0.1`
- RAM used percent: `15.86`
- Swap used percent: `0.0`
- Root disk used percent: `7.93`

## Bridge Sync

- Last inbound sync: `2026-06-22T19:37:49.168072Z`
- Last outbound sync: `2026-06-22T19:37:20.619978Z`
- Last outbound sync status: `pushed`
- Last outbound commit: `6363ddab`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260622-codex-readonly-heartbeat-log-inspection-001`
- Last processed status: `pending_codex`
- Processed count: `22`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-22T18:00:13.723113Z`
- Last pulse commit: `cefcdafa`
- Next scheduled pulse: `Tue 2026-06-23 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T19:37:48.352361Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T19:36:26.844454Z`; age seconds: `82`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:32:47.984319Z`; age seconds: `301`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T19:37:49.168072Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T18:00:13.723113Z`; age seconds: `5855`
