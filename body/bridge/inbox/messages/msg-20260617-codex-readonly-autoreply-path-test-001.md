---
id: msg-20260617-codex-readonly-autoreply-path-test-001
type: codex_request
created_at: 2026-06-17T10:51:57Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: "read-only autoreply/Codex path test"
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
codex:
  question: |
    Jsi Codex spusteny pres "codex_autoreply_worker.py" jako read-only autoreply pro Noema bridge. Proved pouze cteci orientaci v "/home/fiste/Noema".

    Zjisti z dostupnych lokalnich souboru:

    1. Jaky je ucel "bridge_agent_v2.py".
    2. Jaky je ucel "codex_autoreply_worker.py".
    3. Jake jsou hlavni bezpecnostni hranice autoreply workeru.
    4. Jake typy otazek muzes zodpovedet bez sirsiho kontextu, pouze z lokalnich souboru.
    5. Jake typy otazek bez kontextu zodpovedet nemas.

    Nevypisuj zadne tokeny, credentials ani secrets. Neprovadej zadne zmeny. Nespoustej zadne zapisove prikazy. Odpovez strucne a audit-friendly ve formatu: "Co jsem cetl", "Co z toho plyne", "Co nevim", "Bezpecny dalsi krok".
---
