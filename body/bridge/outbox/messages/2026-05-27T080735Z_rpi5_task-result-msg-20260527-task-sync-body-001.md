---
id: task-result-20260527-080735-msg-20260527-task-sync-body-001
type: task_result
created_at: '2026-05-27T08:07:35.762777Z'
sender: rpi5-bridge-agent
target: noema
reply_to: msg-20260527-task-sync-body-001
status: ok
processed_by: rpi5-bridge-agent
task_name: sync_body_without_bridge
exit_code: 0
timed_out: false
---

Task `sync_body_without_bridge` dokoncen.

- run_id: `20260527-080735-msg-20260527-task-sync-body-001`
- status: `ok`
- exit_code: `0`
- timed_out: `False`
- duration_seconds: `0.479`

## stdout

```text
From https://github.com/fisteque/symnozein
 * branch            main       -> FETCH_HEAD
Bridge body changes exist remotely and will be ignored:
  body/bridge/inbox/messages/msg-20260527-task-sync-body-001.md
Non-bridge body changes:
  body/body_diff.md
  body/body_index.json
  body/body_index_prev.json
Updated non-bridge body paths only.
{"branch": "main", "completed_at": "2026-05-27T08:07:35.750488Z", "exit_code": 0, "remote": "origin", "repo_root": "/home/fiste/Noema/symnozein", "run_id": "20260527-080735-msg-20260527-task-sync-body-001", "runtime_root": "/home/fiste/Noema/bridge", "task": "sync_body_without_bridge"}
```

## stderr

```text
(empty)
```
