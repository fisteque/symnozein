# Bridge State Summary

- Generated at: `2026-07-22T14:00:11.017298Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-22T14:00:09.069146+00:00`
- Heartbeat count: `419261`
- Heartbeat last gap seconds: `10.008515`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4201688`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `1`
- Watchdog last heartbeat age seconds: `9.429411`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-22T14:00:08.490056+00:00`

## Body Health

- Health generated at: `2026-07-22T13:59:48.566632Z`
- CPU temperature C: `44.65`
- Load average 1m / 5m / 15m: `0.01 / 0.12 / 0.07`
- RAM used percent: `20.22`
- Swap used percent: `0.0`
- Root disk used percent: `8.53`

## Bridge Sync

- Last inbound sync: `2026-07-22T14:00:09.257175Z`
- Last outbound sync: `2026-07-22T14:00:10.258190Z`
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
- Current pulse started: `2026-07-22T14:00:10.387697Z`
- Last body pulse: `2026-07-22T10:00:09.639937Z`
- Last pulse commit: `ed38031b`
- Next scheduled pulse: `2026-07-22T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-22T14:00:09.069146Z`; age seconds: `1`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-22T13:59:48.566632Z`; age seconds: `22`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `1878061`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-22T14:00:10.258190Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-22T14:00:10.962144Z`; age seconds: `0`
