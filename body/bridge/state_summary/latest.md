# Bridge State Summary

- Generated at: `2026-06-20T10:00:04.648285Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-20T09:59:56.004989+00:00`
- Heartbeat count: `141942`
- Heartbeat last gap seconds: `10.004153`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1422481`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `9.090728`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-20T09:59:55.091581+00:00`

## Body Health

- Health generated at: `2026-06-20T09:51:34.121245Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.1 / 0.04 / 0.0`
- RAM used percent: `14.76`
- Swap used percent: `0.0`
- Root disk used percent: `7.91`

## Bridge Sync

- Last inbound sync: `2026-06-20T09:59:55.744899Z`
- Last outbound sync: `2026-06-20T09:59:56.480855Z`
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
- Current pulse started: `2026-06-20T10:00:04.152292Z`
- Last body pulse: `2026-06-20T06:00:05.726331Z`
- Last pulse commit: `c7c5c4f8`
- Next scheduled pulse: `2026-06-20T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-20T09:59:56.004989Z`; age seconds: `8`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-20T09:51:34.121245Z`; age seconds: `510`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-18T07:58:45.421768Z`; age seconds: `180079`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-20T09:59:56.480855Z`; age seconds: `8`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-20T10:00:04.593997Z`; age seconds: `0`
