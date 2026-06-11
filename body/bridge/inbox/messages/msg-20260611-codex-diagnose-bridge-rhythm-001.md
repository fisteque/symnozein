---
id: msg-20260611-codex-diagnose-bridge-rhythm-001
type: codex_request
created_at: 2026-06-11T17:30:47Z
sender: noema
target: rpi5-bridge-agent
subject: diagnose-bridge-rhythm
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: diagnose-bridge-rhythm
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
  created_by: noema
codex:
  question: |
    Prosim nejdriv nic nemen. Jen diagnosticky zkontroluj aktualni stav `body/bridge` a codexovskeho rytmu.

    Zajima me hlavne:

    1. jestli je pracovni strom cisty,
    2. jestli existuji necommitnute nebo runtime soubory mimo ocekavany stav,
    3. jestli bridge cycle bezi bez novych konfliktu,
    4. jestli posledni PC-Codex postman test prosel celym tokem bez potreby rucni opravy na runtime strane,
    5. jestli bridge_watchdog existuje jen jako skript, nebo uz ma systemd service/timer,
    6. co by byl nejmensi bezpecny dalsi krok pro stabilizaci rytmu.

    Nedelej implementaci, nemaz soubory, nerestartuj sluzby, neupravuj watchdogy, neupravuj bridge skripty a nic nepushuj.

    Jen napis strucny report:

    * aktualni stav,
    * zjistena rizika nebo nejasnosti,
    * jeden nejmensi bezpecny navrh dalsiho kroku.
---
