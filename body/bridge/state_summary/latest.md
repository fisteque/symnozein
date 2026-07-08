# Bridge State Summary

- Generated at: `2026-07-08T14:00:06.665891Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-08T13:59:58.919094+00:00`
- Heartbeat count: `298571`
- Heartbeat last gap seconds: `10.007885`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2992083`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `7`
- Watchdog last heartbeat age seconds: `7.102501`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-08T14:00:06.021612+00:00`

## Body Health

- Health generated at: `2026-07-08T14:00:06.125634Z`
- CPU temperature C: `46.3`
- Load average 1m / 5m / 15m: `0.02 / 0.11 / 0.09`
- RAM used percent: `17.67`
- Swap used percent: `0.0`
- Root disk used percent: `8.2`

## Bridge Sync

- Last inbound sync: `2026-07-08T13:59:46.672708Z`
- Last outbound sync: `2026-07-08T13:59:47.552924Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `ec59b5a8`

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
- Current pulse started: `2026-07-08T14:00:06.128727Z`
- Last body pulse: `2026-07-08T10:00:12.692339Z`
- Last pulse commit: `e4a5fc52`
- Next scheduled pulse: `2026-07-08T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-08T14:00:06.021612Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-08T14:00:06.125634Z`; age seconds: `0`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `668456`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-08T13:59:47.552924Z`; age seconds: `19`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-08T14:00:06.612278Z`; age seconds: `0`
