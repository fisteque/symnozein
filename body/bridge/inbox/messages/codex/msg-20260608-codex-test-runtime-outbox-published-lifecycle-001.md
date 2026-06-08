---
id: msg-20260608-codex-test-runtime-outbox-published-lifecycle-001
type: codex_request
created_at: 2026-06-08T18:08:23Z
sender: noema
target: rpi5-bridge-agent
subject: test-runtime-outbox-published-lifecycle
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: test-runtime-outbox-published-lifecycle
  requires_human: false
  runtime_risk: low
  write_scope: proposed-patch
  created_by: noema
codex:
  question: |
    Over prosim novy lifecycle runtime outbox zprav po patchi bridge_sync_outbound.py.

    Cil testu:

    - vytvorit jednu malou testovaci runtime outbox zpravu v bridge/outbox/messages/;
    - nechat bezny bridge cycle s --commit-and-push zpravu publikovat do GH mirroru;
    - overit, ze po uspesnem pushi byla runtime zprava presunuta do:
      bridge/outbox/published/YYYY-MM/;
    - overit, ze bridge/outbox/published/ neni v git mirroru a neni stageovana/pushovana;
    - overit, ze symnozein/body/bridge/outbox/messages/ ma publikovanou auditni kopii.

    Prosim nemen:

    - inbox sync
    - heartbeat/watchdog
    - timer/systemd
    - lock handling
    - git housekeeping mimo bezny commit/push cyklus

    Vystup:

    - nazev vytvorene testovaci zpravy;
    - zda se objevila v GH mirroru;
    - kam byla presunuta v runtime published archivu;
    - git status po dobehnuti;
    - zda dalsi cyklus stejnou zpravu znovu nepublikuje.
---
