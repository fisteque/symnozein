# Bridge State Summary

- Generated at: `2026-06-17T17:24:39.694419Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-17T17:24:37.288737+00:00`
- Heartbeat count: `118739`
- Heartbeat last gap seconds: `10.005272`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1189956`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `2`
- Watchdog last heartbeat age seconds: `1.612085`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-17T17:24:38.900844+00:00`

## Body Health

- Health generated at: `2026-06-17T17:15:58.092444Z`
- CPU temperature C: `45.2`
- Load average 1m / 5m / 15m: `0.02 / 0.02 / 0.0`
- RAM used percent: `14.15`
- Swap used percent: `0.0`
- Root disk used percent: `7.83`

## Bridge Sync

- Last inbound sync: `2026-06-17T17:24:39.513762Z`
- Last outbound sync: `2026-06-17T17:24:10.253927Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `40735d65`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260617-codex-readonly-root-web-check-001`
- Last processed status: `pending_codex`
- Processed count: `19`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-17T14:00:06.516226Z`
- Last pulse commit: `4fcdd19f`
- Next scheduled pulse: `Wed 2026-06-17 20:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-17T17:24:38.900844Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-17T17:15:58.092444Z`; age seconds: `521`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-17T17:17:39.057579Z`; age seconds: `420`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-17T17:24:39.513762Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-17T14:00:06.516226Z`; age seconds: `12273`
