# Bridge State Summary

- Generated at: `2026-07-02T10:00:02.913935Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-02T09:59:58.479474+00:00`
- Heartbeat count: `245401`
- Heartbeat last gap seconds: `10.007686`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2459279`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `4`
- Watchdog last heartbeat age seconds: `2.960203`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-02T10:00:01.439692+00:00`

## Body Health

- Health generated at: `2026-07-02T09:57:01.234215Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.11 / 0.03 / 0.04`
- RAM used percent: `16.39`
- Swap used percent: `0.0`
- Root disk used percent: `8.11`

## Bridge Sync

- Last inbound sync: `2026-07-02T09:59:42.074759Z`
- Last outbound sync: `2026-07-02T09:59:42.862938Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `6c59e9ec`

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
- Current pulse started: `2026-07-02T10:00:01.531912Z`
- Last body pulse: `2026-07-02T06:00:05.514274Z`
- Last pulse commit: `8d1a2e7b`
- Next scheduled pulse: `2026-07-02T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-02T10:00:01.439692Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-02T09:57:01.234215Z`; age seconds: `181`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `135653`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-02T09:59:42.862938Z`; age seconds: `20`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-02T10:00:02.858343Z`; age seconds: `0`
