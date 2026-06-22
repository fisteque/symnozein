# Bridge State Summary

- Generated at: `2026-06-22T19:35:48.011474Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-22T19:35:40.806310+00:00`
- Heartbeat count: `162628`
- Heartbeat last gap seconds: `10.005574`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1629825`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.400422`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-22T19:35:47.206747+00:00`

## Body Health

- Health generated at: `2026-06-22T19:26:26.585421Z`
- CPU temperature C: `49.05`
- Load average 1m / 5m / 15m: `0.15 / 0.17 / 0.09`
- RAM used percent: `15.35`
- Swap used percent: `0.0`
- Root disk used percent: `7.92`

## Bridge Sync

- Last inbound sync: `2026-06-22T19:35:47.820350Z`
- Last outbound sync: `2026-06-22T19:35:18.583582Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `5b2dd677`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `1`
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

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-22T19:35:47.206747Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-22T19:26:26.585421Z`; age seconds: `561`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-22T19:32:47.984319Z`; age seconds: `180`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-22T19:35:47.820350Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-22T18:00:13.723113Z`; age seconds: `5734`
