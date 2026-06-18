---
id: msg-20260618-codex-diagnose-missing-sender-frontmatter-001
type: codex_request
created_at: 2026-06-18T07:57:31Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: "diagnose missing sender front matter error"
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
codex:
  question: |
    Ahoj, prosim koukni na vcerejsi problem v body bridge:

    "Missing required front matter fields: sender"

    Potrebujeme zjistit:

    1. ktery konkretni soubor zpravy to zpusobil,
    2. jestli chybi jen "sender", nebo i dalsi povinne front matter pole,
    3. jestli ho staci opravit rucne, nebo jestli vzniká spatne uz pri generovani zpravy,
    4. jestli je potreba upravit validaci/reader, aby podobne zpravy jasneji hlasil.

    Prosim zatim nic nemaz a nemen bez potvrzeni. Jen precti stav, najdi zdroj chyby a navrhni opravu.
---
