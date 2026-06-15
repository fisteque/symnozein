# Bridge State Summary

- Generated at: `2026-06-15T14:00:10.356767Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-15T14:00:05.349706+00:00`
- Heartbeat count: `100266`
- Heartbeat last gap seconds: `10.004175`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `1004887`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `5`
- Watchdog last heartbeat age seconds: `2.790415`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-15T14:00:08.140137+00:00`

## Body Health

- Health generated at: `2026-06-15T13:51:27.560710Z`
- CPU temperature C: `42.45`
- Load average 1m / 5m / 15m: `0.07 / 0.06 / 0.05`
- RAM used percent: `13.69`
- Swap used percent: `0.0`
- Root disk used percent: `7.76`

## Bridge Sync

- Last inbound sync: `2026-06-15T14:00:08.937848Z`
- Last outbound sync: `2026-06-15T14:00:09.722221Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `49d8f383`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `0`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-health-001`
- Last processed status: `pending_codex`
- Processed count: `15`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `running`
- Current pulse started: `2026-06-15T14:00:09.843481Z`
- Last body pulse: `2026-06-15T10:00:09.739730Z`
- Last pulse commit: `e64d4d09`
- Next scheduled pulse: `2026-06-15T20:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-15T14:00:08.140137Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-15T13:51:27.560710Z`; age seconds: `522`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:33:24.379794Z`; age seconds: `66405`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-15T14:00:09.722221Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-15T14:00:10.300135Z`; age seconds: `0`
