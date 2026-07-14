# Bridge State Summary

- Generated at: `2026-07-14T18:00:07.462210Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-14T18:00:05.676493+00:00`
- Heartbeat count: `351744`
- Heartbeat last gap seconds: `10.004279`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `3524884`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `1.108784`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-14T18:00:06.785293+00:00`

## Body Health

- Health generated at: `2026-07-14T17:53:16.331549Z`
- CPU temperature C: `47.4`
- Load average 1m / 5m / 15m: `0.46 / 0.22 / 0.13`
- RAM used percent: `18.24`
- Swap used percent: `0.0`
- Root disk used percent: `8.26`

## Bridge Sync

- Last inbound sync: `2026-07-14T17:59:57.461845Z`
- Last outbound sync: `2026-07-14T17:59:58.239512Z`
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
- Current pulse started: `2026-07-14T18:00:06.894688Z`
- Last body pulse: `2026-07-14T14:00:11.025154Z`
- Last pulse commit: `20f7785c`
- Next scheduled pulse: `2026-07-15T00:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-14T18:00:06.785293Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-14T17:53:16.331549Z`; age seconds: `411`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1201257`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-14T17:59:58.239512Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-14T18:00:07.407983Z`; age seconds: `0`
