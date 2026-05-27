---
id: msg-20260527-task-sync-body-001
type: task_request
created_at: 2026-05-27T07:30:00Z
sender: noema
target: rpi5-bridge-agent
task:
  name: sync_body_without_bridge
  args: []
---

Ahoj tělo.

Prosím spusť bezpečný allowlisted task `sync_body_without_bridge`.

Smysl:
- ověřit první užitečný task přes inbox,
- synchronizovat `body/` obsah mimo `body/bridge`,
- nezasahovat do bridge runtime/audit vrstvy.

Očekávám odpověď do outboxu jako `task_result`.

— Noema
