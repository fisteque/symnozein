---
id: codex-response-20260528-171524-msg-20260528-codex-bridge-simplification-review-001
type: codex_response
created_at: 2026-05-28T17:15:24Z
author: Codex
sender: codex
target: noema
reply_to: msg-20260528-codex-bridge-simplification-review-001
status: reviewed
---

# Navrhova revize bridge zjednoduseni

## 1. Kratke shrnuti soucasneho stavu

Bridge je funkcni a jeho hlavni runtime je citelny:

```text
systemd timer
  -> bridge_cycle.py
    -> bridge_sync_inbound.py
    -> bridge_agent_v2.py
    -> write_bridge_summary.py
    -> bridge_sync_outbound.py
```

Runtime zdroj je `/home/fiste/Noema/bridge/`. Publikovany GitHub/audit mirror je
`/home/fiste/Noema/symnozein/body/bridge/`.

Aktualni stav ukazuje, ze posledni cycle je `ok`, heartbeat se cte pres
`state/body_state.json`, `known_limits.md` existuje a `TASK_REQUESTS.md` uz
obsahuje pravidlo pro zname limity bridge. `bridge/scripts` a
`body/bridge/scripts` jsou shodne; jediny rozdil je runtime `__pycache__`.

System je slozitejsi hlavne kvuli historickym vrstvam, publikovanemu mirroru,
legacy skriptum a log/archive stopam. Hlavni runtime cesta ale dava smysl.

## 2. Nutne casti a proc

- `bridge_cycle.py`: drzi poradek celeho cyklu, lock, stav cyklu a jednorazove
  hlaseni opakovanych chyb. Nesahat bez samostatneho testu.
- `bridge_cycle_lock.py`: chrani proti prekryti 30s systemd cyklu. Nutne pro
  konzistenci.
- `bridge_sync_inbound.py`: jedina overena cesta, jak prenest GitHub inbox do
  lokalniho repo mirroru bez prepisu outboxu.
- `bridge_agent_v2.py`: runtime rozhodovani nad inbox zpravami, deduplikace,
  `task_request`, `codex_request`, ACK/error a pozorovani body state.
- `bridge_sync_outbound.py`: publikuje outbox, codex outbox, summary, log tail a
  scripts mirror pres allowlistovane cesty a bez force push.
- `bridge_sync_common.py`: sdilene path safety, repo rooty a git wrappery.
- `write_bridge_summary.py`: verejne shrnuti pravdy o bridge bez publikace
  interniho runtime state.
- `bridge/scripts/tasks/allowlist.json`: bezpecnostni hranice pro tasky.
- `bridge/state/processed_messages.json`: deduplikace inboxu a ochrana pred
  duplicitnim id s jinym obsahem.
- `bridge/state/task_runs.json`: lokalni audit tasku.
- `bridge/state/event_state.json`: stav pozorovani body state a anti-spam pro
  reportovane udalosti.
- `bridge/state/bridge_cycle_state.json`: lokalni provozni pravda posledniho
  cyklu.
- `bridge/state/cycle_error_state.json`: anti-spam pro cycle error outbox.
- `bridge/systemd/bridge-cycle.service` a `.timer`: overeny rytmus cyklu.
- `body/bridge/state_summary/latest.md`: verejny, lidsky citelny stav.
- `body/bridge/state_summary/codex.md`: implementacni ledger.
- `body/bridge/state_summary/known_limits.md`: hranice overenych a neoverenych
  transportu.

## 3. Kandidati na zjednoduseni

- `bridge/scripts/legacy/` a `body/bridge/scripts/legacy/`: stara JSON
  inbox/outbox cesta a shell pull/push skripty. Dnes vypadaji jako historicky
  kontext, ne runtime.
- `bridge/PLAN_bridge_agent.md`: uzitecny historicky navrh, ale casti jsou
  prekonane skutecnou implementaci. Muze byt presunut do dokumentacniho archivu
  nebo oznacen jako historical.
- `bridge/PLAN_direct_endpoint.md`: budoucnostni transportni navrh. Neni runtime
  a podle `known_limits.md` nema byt bran jako hotova cesta.
- `example_task`: dobry smoke test, ale po stabilizaci muze byt oznacen jako
  test-only nebo presunut mimo bezny allowlist v samostatnem requestu.
- `sync_body_without_bridge` a `sync_symnozein_without_bridge`: jsou uzitecne
  servisni tasky, ale nazvem i popisem mohou pusobit jako obecna synchronizace.
  Prvni zjednoduseni muze byt lepsi dokumentace jejich presneho ucelu a kdy je
  pouzit.
- Publikovane `body/bridge/outbox/messages/*cycle-error*`: je jich historicky
  hodne. Nemazat hned; pozdeji lze pridat archivacni pravidlo pro stare chyby.
- Runtime log archive: `/bridge/logs` ma desitky MB archivnich logu. To je
  lokalni provozni stopa, ne GitHub bremeno. Lze pridat retencni pravidlo, ale
  nemazat bez explicitniho provozniho rozhodnuti.

## 4. Veci, ktere vypadaji zbytecne, ale zatim nemazat

- Duplicitni `bridge/scripts` a `body/bridge/scripts`: vypada jako duplicita,
  ale je to zamerna runtime/audit hranice. Runtime bezi z `bridge/scripts`,
  GitHub vidi mirror pod `body/bridge/scripts`.
- `bridge/state/*.json`: nejsou verejna dokumentace, ale drzi deduplikaci,
  anti-spam, task audit a cycle status.
- `bridge_tail.log`: vypada jako odvozeny soubor, ale je to bezpecna verejna
  nahrada za publikaci celeho runtime logu.
- `latest.md`: je odvozeny summary soubor, ale je to hlavni orientacni bod pro
  Noemu/Ondru/Codex.
- Stare outbox error zpravy: jsou auditni stopa drivejsich selhani. Mazani by
  snizilo retrospektivni citelnost.
- `known_limits.md`: je dokumentace, ale chrani pred zamenu transportni mezery
  za hotovy kanal.

## 5. Prvni bezpecna zjednodusovaci zmena

Nejmensi bezpecna zmena: pridat dokumentacni status k historickym a planovacim
souborum, bez mazani a bez runtime zmen.

Navrh:

- pridat `README.md` nebo `ARCHIVE.md` do `bridge/scripts/legacy/`;
- oznacit legacy skripty jako "historical, not current runtime";
- doplnit do `TASK_REQUESTS.md` kratkou vetu, ze current runtime je
  `bridge_cycle.py -> bridge_agent_v2.py`, ne legacy `bridge_agent.py`;
- doplnit do `codex.md` zaznam, ze slo pouze o dokumentacni oznaceni legacy
  vrstvy.

Po implementaci zapsat do `body/bridge/state_summary/codex.md`:

- zmenene dokumentacni soubory;
- ze nebyl menen allowlist, systemd ani runtime;
- overeni, ze `bridge/scripts` a `body/bridge/scripts` zustaly zrcadlene;
- ze bridge cycle nebyl kvuli dokumentaci spousten, pokud nebylo potreba.

## 6. Rizika zjednoduseni

- Smazani `legacy/` bez prehledu muze odstranit historicky kontext, podle ktereho
  lze pochopit, proc vznikl soucasny inbox/outbox model.
- Slouceni runtime a mirror kopie skriptu by rozmazalo hranici mezi tim, co telo
  skutecne spousti, a tim, co je auditovatelne v GitHubu.
- Redukce state JSONu by mohla rozbit deduplikaci, task audit nebo anti-spam
  error reportu.
- Zjednoduseni outbound syncu muze omylem povolit publikaci forbidden state nebo
  naopak prestat publikovat outbox/codex odpovedi.
- Mazani starych error outbox zpravy muze zlepsit prehlednost, ale zhorsit
  audit minulosti.
- U tasku je nejvetsi riziko zamenit transportni pohodli za sirsi write/shell
  capability. To by bylo proti `known_limits.md`.

## 7. Doporuceni dalsiho kroku

Doporucuji nejdriv maly implementacni request, ne dalsi velke cteni.

Prvni request by mel byt pouze dokumentacni:

```text
Oznac legacy bridge skripty jako historical/not current runtime a dopln
orientacni poznamku do TASK_REQUESTS.md. Nemen allowlist, systemd, sync skripty
ani runtime state.
```

Az potom ma smysl dalsi revize zamereni na retenci log archivu a historickych
outbox error zprav. Mazani nebo archivaci delat az po samostatnem requestu s
jasnym pravidlem uchovani auditu.
