# Bridge State Summary

- Generated at: `2026-07-23T10:00:02.324556Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-23T09:59:53.940483+00:00`
- Heartbeat count: `426442`
- Heartbeat last gap seconds: `10.005129`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4273679`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `5.763108`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-23T09:59:59.703609+00:00`

## Body Health

- Health generated at: `2026-07-23T09:51:39.018963Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.27 / 0.13 / 0.04`
- RAM used percent: `20.5`
- Swap used percent: `0.0`
- Root disk used percent: `8.52`

## Bridge Sync

- Last inbound sync: `2026-07-23T10:00:00.491048Z`
- Last outbound sync: `2026-07-23T10:00:01.374604Z`
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
- Current pulse started: `2026-07-23T10:00:01.497898Z`
- Last body pulse: `2026-07-23T06:00:10.044246Z`
- Last pulse commit: `b76cac8b`
- Next scheduled pulse: `2026-07-23T16:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-23T09:59:59.703609Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-23T09:51:39.018963Z`; age seconds: `503`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1950052`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-23T10:00:01.374604Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-23T10:00:02.269206Z`; age seconds: `0`
