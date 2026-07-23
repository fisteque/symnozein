# Bridge State Summary

- Generated at: `2026-07-23T06:00:08.403619Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-23T06:00:01.339005+00:00`
- Heartbeat count: `425005`
- Heartbeat last gap seconds: `10.009998`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4259285`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `6.404259`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-23T06:00:07.743279+00:00`

## Body Health

- Health generated at: `2026-07-23T05:51:17.092465Z`
- CPU temperature C: `43.55`
- Load average 1m / 5m / 15m: `0.02 / 0.01 / 0.0`
- RAM used percent: `20.43`
- Swap used percent: `0.0`
- Root disk used percent: `8.52`

## Bridge Sync

- Last inbound sync: `2026-07-23T05:59:48.421130Z`
- Last outbound sync: `2026-07-23T05:59:49.306148Z`
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
- Current pulse started: `2026-07-23T06:00:07.836812Z`
- Last body pulse: `2026-07-23T02:00:08.442154Z`
- Last pulse commit: `b9197eb5`
- Next scheduled pulse: `2026-07-23T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-23T06:00:07.743279Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-23T05:51:17.092465Z`; age seconds: `531`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1935658`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-23T05:59:49.306148Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-23T06:00:08.348163Z`; age seconds: `0`
