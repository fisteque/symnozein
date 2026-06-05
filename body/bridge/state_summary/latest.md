# Bridge State Summary

- Generated at: `2026-06-05T20:06:04.293359Z`
- Inbox messages: `2`; latest: `msg-20260527-task-sync-body-001.md`
- Codex inbox files: `21`; latest: `msg-20260605-codex-save-pc-postman-instructions-001.md`
- Outbox messages: `43`; latest: `2026-06-05T200233Z_rpi5_cycle-error-outbound-sync.md`
- Codex outbox files: `19`; latest: `2026-06-05T192110Z_codex-response-msg-20260605-codex-save-pc-postman-instructions-001.md`
- Last processed message: `msg-20260527-task-sync-body-001`
- Last processed status: `ok`
- Processed count: `2`
- Error count: `0`
- Last error: `(none)`
- Body awake: `True`
- Body status: `normal_operation`
- Body last heartbeat: `2026-06-05T20:05:56.256661+00:00`
- Heartbeat count: `16251`
- Heartbeat last gap seconds: `10.008926`
- Heartbeat max gap seconds: `88.126733`
- Heartbeat service started at: `Thu 2026-06-04 00:52:02 CEST`
- Heartbeat uptime seconds: `162841`
- Heartbeat restart count: `0`
- Heartbeat uptime source: `systemd`
- Heartbeat log starts count: `17`
- Heartbeat log latest start: `2026-06-03T22:52:02.965137Z`
- Heartbeat log max start gap seconds: `675295`
- Last heartbeat gap seconds: `8`
- Watchdog last heartbeat age seconds: `7.090205`
- Watchdog heartbeat timeout threshold seconds: `45`
- Watchdog heartbeat timeout count: `0`
- Watchdog heartbeat timeout required count: `2`
- Body watchdog last check: `2026-06-05T20:06:03.346884+00:00`

## Bridge Log Tail

Filtered runtime tail, max 60 lines.

```text
[2026-06-05T20:03:33.630522Z] [INFO] [cycle] == outbound sync ==
[2026-06-05T20:03:33.699891Z] [ERROR] [cycle] ERROR: Refusing outbound sync because worktree has changes outside the bridge outbound whitelist:
[2026-06-05T20:03:33.700741Z] [ERROR] [cycle] Step failed (outbound sync) with exit code 2
[2026-06-05T20:03:33.703961Z] [ERROR] [cycle] Traceback (most recent call last):
[2026-06-05T20:03:33.706093Z] [WARN] [cycle] Cycle error already reported for step=outbound sync repeat_count=3
[2026-06-05T20:04:03.034211Z] [INFO] [cycle] Bridge cycle lock acquired: /home/fiste/Noema/bridge/state/bridge_cycle.lock.json
[2026-06-05T20:04:03.037456Z] [INFO] [cycle] == inbound sync ==
[2026-06-05T20:04:03.512216Z] [INFO] [cycle] == bridge agent ==
[2026-06-05T20:04:03.579526Z] [INFO] Body state unchanged: awake=True status=normal_operation
[2026-06-05T20:04:03.586805Z] [INFO] Pending message count remaining: 0
[2026-06-05T20:04:03.586902Z] [INFO] Processed message count: 0
[2026-06-05T20:04:03.606088Z] [INFO] [cycle] == write bridge summary ==
[2026-06-05T20:04:03.672379Z] [INFO] [cycle] == outbound sync ==
[2026-06-05T20:04:03.744764Z] [ERROR] [cycle] ERROR: Refusing outbound sync because worktree has changes outside the bridge outbound whitelist:
[2026-06-05T20:04:03.745536Z] [ERROR] [cycle] Step failed (outbound sync) with exit code 2
[2026-06-05T20:04:03.748792Z] [ERROR] [cycle] Traceback (most recent call last):
[2026-06-05T20:04:03.750876Z] [WARN] [cycle] Cycle error already reported for step=outbound sync repeat_count=4
[2026-06-05T20:04:33.086438Z] [INFO] [cycle] Bridge cycle lock acquired: /home/fiste/Noema/bridge/state/bridge_cycle.lock.json
[2026-06-05T20:04:33.088907Z] [INFO] [cycle] == inbound sync ==
[2026-06-05T20:04:33.567248Z] [INFO] [cycle] == bridge agent ==
[2026-06-05T20:04:33.636235Z] [INFO] Body state unchanged: awake=True status=normal_operation
[2026-06-05T20:04:33.643438Z] [INFO] Pending message count remaining: 0
[2026-06-05T20:04:33.643535Z] [INFO] Processed message count: 0
[2026-06-05T20:04:33.662095Z] [INFO] [cycle] == write bridge summary ==
[2026-06-05T20:04:33.730300Z] [INFO] [cycle] == outbound sync ==
[2026-06-05T20:04:33.799871Z] [ERROR] [cycle] ERROR: Refusing outbound sync because worktree has changes outside the bridge outbound whitelist:
[2026-06-05T20:04:33.801023Z] [ERROR] [cycle] Step failed (outbound sync) with exit code 2
[2026-06-05T20:04:33.804476Z] [ERROR] [cycle] Traceback (most recent call last):
[2026-06-05T20:04:33.806606Z] [WARN] [cycle] Cycle error already reported for step=outbound sync repeat_count=5
[2026-06-05T20:05:03.212763Z] [INFO] [cycle] Bridge cycle lock acquired: /home/fiste/Noema/bridge/state/bridge_cycle.lock.json
[2026-06-05T20:05:03.216194Z] [INFO] [cycle] == inbound sync ==
[2026-06-05T20:05:03.688098Z] [INFO] [cycle] == bridge agent ==
[2026-06-05T20:05:03.764884Z] [INFO] Body state unchanged: awake=True status=normal_operation
[2026-06-05T20:05:03.771686Z] [INFO] Pending message count remaining: 0
[2026-06-05T20:05:03.771783Z] [INFO] Processed message count: 0
[2026-06-05T20:05:03.790973Z] [INFO] [cycle] == write bridge summary ==
[2026-06-05T20:05:03.858239Z] [INFO] [cycle] == outbound sync ==
[2026-06-05T20:05:03.930057Z] [ERROR] [cycle] ERROR: Refusing outbound sync because worktree has changes outside the bridge outbound whitelist:
[2026-06-05T20:05:03.930822Z] [ERROR] [cycle] Step failed (outbound sync) with exit code 2
[2026-06-05T20:05:03.933946Z] [ERROR] [cycle] Traceback (most recent call last):
[2026-06-05T20:05:03.935624Z] [WARN] [cycle] Cycle error already reported for step=outbound sync repeat_count=6
[2026-06-05T20:05:33.343599Z] [INFO] [cycle] Bridge cycle lock acquired: /home/fiste/Noema/bridge/state/bridge_cycle.lock.json
[2026-06-05T20:05:33.345738Z] [INFO] [cycle] == inbound sync ==
[2026-06-05T20:05:33.833544Z] [INFO] [cycle] == bridge agent ==
[2026-06-05T20:05:33.902166Z] [INFO] Body state unchanged: awake=True status=normal_operation
[2026-06-05T20:05:33.909340Z] [INFO] Pending message count remaining: 0
[2026-06-05T20:05:33.909439Z] [INFO] Processed message count: 0
[2026-06-05T20:05:33.929048Z] [INFO] [cycle] == write bridge summary ==
[2026-06-05T20:05:33.994253Z] [INFO] [cycle] == outbound sync ==
[2026-06-05T20:05:34.043593Z] [ERROR] [cycle] ERROR: Refusing outbound sync because staged paths outside the bridge outbound whitelist exist:
[2026-06-05T20:05:34.044487Z] [ERROR] [cycle] Step failed (outbound sync) with exit code 2
[2026-06-05T20:05:34.047677Z] [ERROR] [cycle] Traceback (most recent call last):
[2026-06-05T20:05:34.049812Z] [WARN] [cycle] Cycle error already reported for step=outbound sync repeat_count=7
[2026-06-05T20:06:03.496282Z] [INFO] [cycle] Bridge cycle lock acquired: /home/fiste/Noema/bridge/state/bridge_cycle.lock.json
[2026-06-05T20:06:03.498754Z] [INFO] [cycle] == inbound sync ==
[2026-06-05T20:06:04.154704Z] [INFO] [cycle] == bridge agent ==
[2026-06-05T20:06:04.222456Z] [INFO] Body state unchanged: awake=True status=normal_operation
[2026-06-05T20:06:04.229769Z] [INFO] Pending message count remaining: 0
[2026-06-05T20:06:04.229862Z] [INFO] Processed message count: 0
[2026-06-05T20:06:04.248894Z] [INFO] [cycle] == write bridge summary ==
```
