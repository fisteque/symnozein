# Bridge State Summary

- Generated at: `2026-07-21T18:00:06.754862Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-21T17:59:58.342124+00:00`
- Heartbeat count: `412075`
- Heartbeat last gap seconds: `10.005184`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4129683`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.619334`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-21T18:00:05.961473+00:00`

## Body Health

- Health generated at: `2026-07-21T17:58:05.915887Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.01 / 0.1 / 0.09`
- RAM used percent: `19.99`
- Swap used percent: `0.0`
- Root disk used percent: `8.5`

## Bridge Sync

- Last inbound sync: `2026-07-21T17:59:57.035892Z`
- Last outbound sync: `2026-07-21T17:59:57.892283Z`
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
- Current pulse started: `2026-07-21T18:00:06.084193Z`
- Last body pulse: `2026-07-21T14:00:09.781629Z`
- Last pulse commit: `3845dd1c`
- Next scheduled pulse: `2026-07-22T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-21T18:00:05.961473Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-21T17:58:05.915887Z`; age seconds: `120`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1806057`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-21T17:59:57.892283Z`; age seconds: `8`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-21T18:00:06.644863Z`; age seconds: `0`
