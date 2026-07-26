---
id: msg-20260726-codex-read-runtime-agents-root-001
type: codex_request
created_at: 2026-07-26T16:30:01Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: "read runtime-only AGENTS.md anchor"
  requires_human: false
  runtime_risk: low
  write_scope: outbox-only
codex:
  question: |
    Ukol pro exec:

    Precti runtime-only soubor:

    /home/fiste/Noema/AGENTS.md

    a vrat jeho presne zneni do odpovedi pro Noemu.

    Ucel: Noema chce overit runtime instrukcni kotvu, kterou pres GitHub mirror nevidi, a porovnat ji s aktualni paskou a bridge pravidly.

    Jde jen o read-only inspection a odpoved do outboxu. Neprovadet zadne jine zmeny.
---
