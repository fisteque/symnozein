# Bridge State Summary

- Generated at: `2026-06-17T22:00:03.614268Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T21:59:59.896096+00:00`
- Heartbeat count: `120388`
- Heartbeat last gap seconds: `10.007689`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1206480`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `3`
- Watchdog last heartbeat age seconds: `3.022397`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T22:00:02.918509+00:00`

## Body Health

- Health generated at: `2026-06-17T21:56:22.635044Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.1 / 0.14 / 0.07`
- RAM used percent: `14.22`
- Swap used percent: `0.0`
- Root disk used percent: `7.84`

## Bridge Sync

- Last inbound sync: `2026-06-17T21:59:53.439762Z`
- Last outbound sync: `2026-06-17T21:59:54.189889Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `067af326`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-root-web-check-001`
- Last processed status: `pending_codex`
- Processed count: `19`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-17T22:00:03.062999Z`
- Last body pulse: `2026-06-17T18:00:05.917379Z`
- Last pulse commit: `330f7b3c`
- Next scheduled pulse: `2026-06-18T04:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T22:00:02.918509Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T21:56:22.635044Z`; age seconds: `220`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T17:17:39.057579Z`; age seconds: `16944`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T21:59:54.189889Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T22:00:03.557786Z`; age seconds: `0`
