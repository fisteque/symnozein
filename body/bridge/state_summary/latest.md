# Bridge State Summary

- Generated at: `2026-06-19T22:00:05.399544Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-19T22:00:01.780271+00:00`
- Heartbeat count: `137630`
- Heartbeat last gap seconds: `10.004285`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1379282`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `1.621531`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-19T22:00:03.401819+00:00`

## Body Health

- Health generated at: `2026-06-19T21:50:32.674430Z`
- CPU temperature C: `46.85`
- Load average 1m / 5m / 15m: `0.09 / 0.03 / 0.03`
- RAM used percent: `14.61`
- Swap used percent: `0.0`
- Root disk used percent: `7.9`

## Bridge Sync

- Last inbound sync: `2026-06-19T22:00:04.062398Z`
- Last outbound sync: `2026-06-19T22:00:04.786273Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `0ee533b3`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260618-codex-diagnose-missing-sender-frontmatter-001`
- Last processed status: `pending_codex`
- Processed count: `20`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-19T22:00:04.900875Z`
- Last body pulse: `2026-06-19T18:00:04.649076Z`
- Last pulse commit: `1040525b`
- Next scheduled pulse: `2026-06-20T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-19T22:00:03.401819Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-19T21:50:32.674430Z`; age seconds: `572`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `136879`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-19T22:00:04.786273Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-19T22:00:05.343028Z`; age seconds: `0`
