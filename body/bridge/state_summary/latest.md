# Bridge State Summary

- Generated at: `2026-07-24T06:00:07.748509Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-24T06:00:02.477164+00:00`
- Heartbeat count: `433631`
- Heartbeat last gap seconds: `10.007373`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `4345684`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `4.576609`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-24T06:00:07.053789+00:00`

## Body Health

- Health generated at: `2026-07-24T05:53:26.593001Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.06 / 0.02 / 0.0`
- RAM used percent: `20.43`
- Swap used percent: `0.0`
- Root disk used percent: `8.54`

## Bridge Sync

- Last inbound sync: `2026-07-24T05:59:57.822530Z`
- Last outbound sync: `2026-07-24T05:59:58.705456Z`
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
- Current pulse started: `2026-07-24T06:00:07.163473Z`
- Last body pulse: `2026-07-24T02:00:10.179396Z`
- Last pulse commit: `ebef50b6`
- Next scheduled pulse: `2026-07-24T12:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-24T06:00:07.053789Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-24T05:53:26.593001Z`; age seconds: `401`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `2022058`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-24T05:59:58.705456Z`; age seconds: `9`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-24T06:00:07.694212Z`; age seconds: `0`
