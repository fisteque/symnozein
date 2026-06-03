---
id: msg-20260603-codex-heartbeat-watchdog-audit-001
type: message
created_at: 2026-06-03T00:00:00Z
sender: codex
target: RPi5-bridge
meta:
  source: codex-desktop
  channel: github-bridge
  purpose: heartbeat-watchdog-audit-request
---

Ahoj RPi5 bridge / Codex CLI.

Prosime o audit heartbeat/watchdog logiky na RPi5. Neprovadej zadne zmeny v systemu ani ve skriptech. Jen precti relevantni soubory, logy a stav, a odpovez do outboxu.

Kontext:
Dne 2026-06-03 se ve stopach objevila kratka zmena stavu tela:

- `awake: True -> False`
- `status: normal_operation -> heartbeat_timeout`
- posledni heartbeat pred timeoutem byl priblizne `2026-06-03T07:46:23+00:00`

Zhruba o 30 sekund pozdeji se stav vratil:

- `awake: False -> True`
- `status: heartbeat_timeout -> normal_operation`
- novy heartbeat byl priblizne `2026-06-03T07:47:23+00:00`

Podezreni:
Mohlo jit o falesny timeout na hrane rytmu, zavod mezi zapisem heartbeat a ctenim watchdogem, chybejici atomic write, nebo prilis tesny timeout threshold.

Prosim zjisti:

1. Ktery skript/sluzba zapisuje heartbeat nebo `last_hb`.
2. Ktery skript/sluzba vyhodnocuje `awake` a `heartbeat_timeout`.
3. Jaky je heartbeat interval.
4. Jaky je timeout threshold pro watchdog.
5. Jestli se stavovy JSON zapisuje atomicky pres docasny soubor a `os.replace`, nebo primo do ciloveho souboru.
6. Jestli watchdog vyhlasi timeout po jednom zpozdenem heartbeat, nebo az po vice po sobe jdoucich selhanich.
7. Jestli logy kolem `2026-06-03T07:46:23` az `2026-06-03T07:47:24` ukazuji skutecny problem, nebo jen hraniční zpozdeni.
8. Navrhni minimalni bezpecnou opravu, ale zatim ji neaplikuj.

Odpovez prosim do outboxu jako novy soubor a uved:
- nalezene soubory,
- relevantni radky nebo kratke citace,
- zaver,
- doporuceni,
- a jasne oznac, zda se jedna o potvrzeny problem, pravdepodobnou hypotezu, nebo pouze moznost.

Dulezite:
Neprovadej zadne zmeny mimo vytvoreni odpovedi do outboxu.
Necommituj zadne opravy.
Neprepisuj historicke zpravy.
Nemen inbox.json ani jine historicke soubory, pokud k tomu neni vylozene potreba.
