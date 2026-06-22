---
id: msg-20260622-codex-readonly-heartbeat-log-inspection-001
type: codex_request
created_at: 2026-06-22T19:30:51Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: "read-only heartbeat log inspection"
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
codex:
  question: |
    # Read-only heartbeat log inspection

    Prosim proved uzkou read-only kontrolu heartbeat sluzby a souvisejiciho watchdog stavu.

    Bez uprav souboru.
    Bez restartu sluzeb.
    Bez commit/push.
    Bez mazani nebo zmen runtime state.
    Pouze cteni a strucny report.

    ## Zjistit

    1. Aktualni stav heartbeat sluzby:

       * `systemctl status --no-pager ...`
       * start time / uptime
       * restart count, pokud je dostupny

    2. Posledni relevantni heartbeat log:

       * poslednich cca 50 radku journalu heartbeat sluzby
       * pripadne chyby, restarty, vetsi mezery nebo varovani

    3. Watchdog souvislosti:

       * aktualni watchdog heartbeat timeout count
       * posledni znamy heartbeat age / gap, pokud je dostupny
       * zda watchdog eviduje neco podezreleho

    4. Porovnat s poslednim publikovanym `body/bridge/state_summary/latest.md`:

       * zda sedi start sluzby kolem `Thu 2026-06-04 00:52:02 CEST`
       * zda sedi, ze heartbeat bezi bez restartu
       * zda latest verejny stav odpovida lokalnimu runtime stavu

    ## Vratit

    Strucnou odpoved:

    * verdikt: OK / podezrele / needs_human
    * potvrzeny uptime HB
    * restart count
    * watchdog timeout count
    * posledni relevantni logove radky nebo jejich shrnuti
    * pripadne riziko nebo dalsi doporuceny read-only dotaz
---
