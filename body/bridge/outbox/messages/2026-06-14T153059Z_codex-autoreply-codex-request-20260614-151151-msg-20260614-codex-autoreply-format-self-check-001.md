---
id: codex-autoreply-20260614-153059-codex-request-20260614-151151-msg-20260614-codex-autoreply-format-self-check-001
type: codex_response
created_at: '2026-06-14T15:30:59.440653Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260614-151151-msg-20260614-codex-autoreply-format-self-check-001
status: answered
source_path: codex/inbox/2026-06-14T151151Z_codex-request-msg-20260614-codex-autoreply-format-self-check-001.md
source_sha256: 971ab689d0d8ef2d7eabe15e6ff1467007dcf138b50a7ed9b9f404dba42c534c
mode: codex_exec
---

Read-only check result:

1. Incoming bridge `codex_request` needs frontmatter fields: `id`, `type`, `created_at`, `sender`, `target`; `type` must be `codex_request`, `target` must be `rpi5-bridge-agent` or `rpi5-bridge`, and it must contain `codex.question` or a non-empty body. The generated local Codex queue item uses `id`, `type`, `created_at`, `sender`, `target`, `reply_to`, `status`, `requested_by`, `source_message`.

2. For automatic read-only Codex execution, the local queued request target is `codex`.

3. Before Codex processes it, the request is delivered to `/home/fiste/Noema/codex/inbox/`.

4. The automatic response is written to the bridge outbox messages path, currently `/home/fiste/Noema/symnozein/body/bridge/outbox/messages/`, then later appears in published outbox after normal outbound sync.

5. Confirmed: this request is read-only only. It does not require edits, commits, pushes, installs, restarts, deletes, or runtime state changes.

---

source_request: `codex-request-20260614-151151-msg-20260614-codex-autoreply-format-self-check-001`
source_sha256: `971ab689d0d8ef2d7eabe15e6ff1467007dcf138b50a7ed9b9f404dba42c534c`
