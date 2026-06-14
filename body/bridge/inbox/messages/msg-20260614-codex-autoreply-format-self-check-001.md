---
id: msg-20260614-codex-autoreply-format-self-check-001
type: codex_request
created_at: 2026-06-14T15:10:40Z
sender: noema
target: rpi5-bridge-agent
subject: codex-autoreply-format-self-check
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: codex-autoreply-format-self-check
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
codex:
  question: |
    Read-only self-check: Codex autoreply request format

    Please inspect the local project files read-only and answer briefly:

    1. What frontmatter fields are required for an automatic codex_request to be accepted by the bridge/autoreply path?
    2. Which target value should be used for automatic read-only Codex execution?
    3. Where is the request delivered locally before Codex processes it?
    4. Where does the automatic response appear after processing?
    5. Confirm that this request does not require edits, commits, pushes, installs, restarts, or runtime state changes.

    Do not modify any files. Do not run commands that change state. Do not commit, push, install, delete, restart services, or edit runtime files.

    This is only a read-only orientation check after the UI memory cleanup and the body pulse fallback repair.

    Tohle by byl pekny prvni "zivy" test: nechat technickou ruku popsat vlastni bezpecny pruchod.
---
