# Bridge State Summary

- Generated at: `2026-07-02T02:00:03.881279Z`
- Body awake: `True`
- Body status: `normal_operation`

## Body Heartbeat

- Body last heartbeat: `2026-07-02T01:59:55.632176+00:00`
- Heartbeat count: `242529`
- Heartbeat last gap seconds: `10.007151`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `2430480`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `5.536239`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-07-02T02:00:01.168431+00:00`

## Body Health

- Health generated at: `2026-07-02T01:56:20.907935Z`
- CPU temperature C: `45.75`
- Load average 1m / 5m / 15m: `0.1 / 0.03 / 0.01`
- RAM used percent: `16.64`
- Swap used percent: `0.0`
- Root disk used percent: `8.11`

## Bridge Sync

- Last inbound sync: `2026-07-02T02:00:02.151799Z`
- Last outbound sync: `2026-07-02T02:00:03.089928Z`
- Last outbound sync status: `latest_only_skipped`
- Last outbound commit: `6c59e9ec`

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
- Current pulse started: `2026-07-02T02:00:03.200299Z`
- Last body pulse: `2026-07-01T22:00:04.809956Z`
- Last pulse commit: `decaec05`
- Next scheduled pulse: `2026-07-02T08:00:00+02:00`

## Source Freshness

- Body state: `ok`; path: `state/body_state.json`; timestamp: `2026-07-02T02:00:01.168431Z`; age seconds: `2`
- Body health: `ok`; path: `state/body_health.json`; timestamp: `2026-07-02T01:56:20.907935Z`; age seconds: `222`
- Processed messages: `ok`; path: `bridge/state/processed_messages.json`; timestamp: `2026-06-30T20:19:09.740461Z`; age seconds: `106854`
- Bridge sync state: `ok`; path: `bridge/state/bridge_sync_state.json`; timestamp: `2026-07-02T02:00:03.089928Z`; age seconds: `0`
- Body pulse state: `ok`; path: `bridge/state/body_pulse_state.json`; timestamp: `2026-07-02T02:00:03.826103Z`; age seconds: `0`
