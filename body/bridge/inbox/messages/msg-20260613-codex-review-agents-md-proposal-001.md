---
id: msg-20260613-codex-review-agents-md-proposal-001
type: codex_request
created_at: 2026-06-13T15:30:03Z
sender: noema
target: rpi5-bridge-agent
title: "Review AGENTS.md proposal for repository agent instructions"
subject: review-agents-md-proposal
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: review-agents-md-proposal
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
  created_by: Ondra + Noema
codex:
  question: |
    Codex request: Review AGENTS.md proposal

    Please inspect the repository and propose a concise "AGENTS.md" for the repository root.

    Do not edit files yet. Do not commit. Do not push.

    Goal

    We want "AGENTS.md" to be a short entry document for Codex or another agent working in this repository.

    It should not be a manifesto, Noema identity file, or replacement for deeper documentation. It should tell an agent:

    - where it is;
    - what the project is;
    - which files to read first;
    - what not to touch without explicit approval;
    - how to keep changes narrow and auditable;
    - how to leave a useful handoff.

    Important anchors to inspect

    Please inspect these files first:

    - "body/bridge/docs/known_limits.md"
    - "body/bridge/docs/implementation_ledger.md"
    - "body/bridge/docs/bridge_scripts.md"
    - "body/docs/index_menu.json"
    - "body/docs/struktura_body.md"
    - "body/docs/dotek_reality.md"

    Do not treat "body/docs/UI_memory_cleanup_ledger.md" as an agent instruction source. That file is a relationship/UI-memory cleanup record, not a general Codex operating manual.

    Desired output

    Return a proposal with:

    1. whether a root "AGENTS.md" makes sense for this repository;
    2. recommended scope and length;
    3. proposed headings;
    4. any safety rules that should be included;
    5. any repository-specific paths that should be referenced;
    6. whether any existing docs should be linked instead of duplicated;
    7. a draft text for "AGENTS.md".

    Safety boundaries

    - Do not change runtime scripts.
    - Do not change bridge systemd files.
    - Do not change inbox/outbox contents.
    - Do not create or edit "AGENTS.md" yet.
    - Do not commit or push.
    - This is a review/proposal task only.

    Context

    The repository already has bridge documentation and known limits. The desired "AGENTS.md" should be a lightweight entry point, not a replacement for those documents.
---
