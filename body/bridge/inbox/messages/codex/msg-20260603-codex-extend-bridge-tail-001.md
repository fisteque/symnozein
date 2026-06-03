---
id: msg-20260603-codex-extend-bridge-tail-001
type: codex_request
created_at: 2026-06-03T00:00:00Z
sender: codex
target: RPi5-bridge
meta:
  source: codex-desktop
  channel: github-bridge
  purpose: extend-bridge-tail-log
  requires_human: false
  runtime_risk: low
  write_scope: proposed-patch
---

Ahoj RPi5 bridge / Codex CLI.

Prosime o pripravu male bezpecne upravy delky log tailu pro bridge stavove souhrny.

Cil:
- `bridge/state_summary/latest.md` ma zobrazovat poslednich 120 radku bridge log tailu.
- `bridge/logs/bridge_tail.log` ma uchovavat poslednich 500 radku.

Duvod:
Aktualni tail v `latest.md` je kratky a casto zachyti jen posledni bridge cycle. Pro diagnostiku kratkych arytmii heartbeat/watchdog rytmu potrebujeme videt delsi okoli udalosti, ale nechceme do `latest.md` davat cely archiv.

Pozadovane chovani:
- `latest.md` zustane kratky stavovy prehled, ale s tail casti o 120 radcich.
- `bridge_tail.log` bude kratkodoba pracovni pamet o 500 radcich.
- plne archivni logy zustanou bez zmeny.

Prosim:
1. Najdi skript nebo skripty, ktere generuji `bridge/state_summary/latest.md` a `bridge/logs/bridge_tail.log`.
2. Navrhni minimalni patch pro zmenu delky tailu na hodnoty:
   - summary tail: 120 radku
   - bridge_tail.log: 500 radku
3. Pokud je zmena jednoducha a lokalni, muzes ji aplikovat.
4. Neprovadej zadne jine zmeny.
5. Nezasahuj do heartbeat/watchdog logiky.
6. Neprepisuj historicke zpravy.
7. Odpovez do outboxu s popisem:
   - ktere soubory byly nalezeny,
   - ktere soubory byly zmeneny,
   - jaky je diff nebo shrnuti diffu,
   - a zda byla zmena aplikovana, nebo jen navrzena.

Dulezite:
Tento request je nizke riziko, ale musi zustat omezeny pouze na konfiguraci/delku bridge log tailu.

Neprováděj žádné jiné změny.
Neměň historické zprávy.
Neměň "inbox.json", "outbox.json" ani jiné indexy ručně.
Po vytvoření souboru ukaž diff/status, commitni pouze tento jeden nový soubor a pushni.
