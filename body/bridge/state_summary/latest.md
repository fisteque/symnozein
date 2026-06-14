# Bridge State Summary

- Generated at: `2026-06-14T19:28:53.790115Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-06-14T19:28:53.063375+00:00`
- Heartbeat count: `93613`
- Heartbeat last gap seconds: `10.006477`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `938210`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `0`
- Watchdog last heartbeat age seconds: `9.954829`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-14T19:28:53.011743+00:00`

## Body Health

- Health generated at: `2026-06-14T19:19:52.309582Z`
- CPU temperature C: `44.1`
- Load average 1m / 5m / 15m: `0.0 / 0.0 / 0.0`
- RAM used percent: `13.4`
- Swap used percent: `0.0`
- Root disk used percent: `7.75`

## Bridge Sync

- Last inbound sync: `2026-06-14T19:28:53.628905Z`
- Last outbound sync: `2026-06-14T19:28:24.438389Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `e8f951aa`

## Queues

- Bridge inbox pending: `0`
- Bridge outbox pending: `1`
- Codex runtime inbox files: `0`
- Needs human count: `0`
- Last processed message: `msg-20260614-read-full-body-pulse-state-001`
- Last processed status: `pending_codex`
- Processed count: `14`
- Error count: `1`
- Last error: `Missing required front matter fields: sender`

## Pulse

- Current pulse status: `idle`
- Last body pulse: `2026-06-14T18:00:06.762058Z`
- Last pulse commit: `d7e055bd`
- Next scheduled pulse: `Mon 2026-06-15 00:00:00 CEST`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-06-14T19:28:53.063375Z`; age seconds: `0`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-06-14T19:19:52.309582Z`; age seconds: `541`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-14T19:28:23.771106Z`; age seconds: `30`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-06-14T19:28:53.628905Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-06-14T18:00:06.762058Z`; age seconds: `5327`
