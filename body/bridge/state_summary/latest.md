# Bridge State Summary

- Generated at: `2026-07-25T02:00:09.046987Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-25T02:00:08.821278+00:00`
- Heartbeat count: `440816`
- Heartbeat last gap seconds: `10.005125`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4417686`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `7.836126`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-25T02:00:06.652295+00:00`

## Body Health

- Health generated at: `2026-07-25T01:55:16.311429Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.04`
- RAM used percent: `20.75`
- Swap used percent: `0.0`
- Root disk used percent: `8.56`

## Bridge Sync

- Last inbound sync: `2026-07-25T02:00:07.426998Z`
- Last outbound sync: `2026-07-25T02:00:08.285284Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `f1c00bdd`

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
- Current pulse started: `2026-07-25T02:00:08.430925Z`
- Last body pulse: `2026-07-24T22:00:07.395229Z`
- Last pulse commit: `075a269a`
- Next scheduled pulse: `2026-07-25T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-25T02:00:08.821278Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-25T01:55:16.311429Z`; age seconds: `292`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2094059`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-25T02:00:08.285284Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-25T02:00:08.939031Z`; age seconds: `0`
