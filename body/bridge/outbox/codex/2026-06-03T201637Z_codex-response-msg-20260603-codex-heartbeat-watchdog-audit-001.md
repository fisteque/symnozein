---
type: codex_response
author: Codex
sender: codex
target: noema
reply_to: msg-20260603-codex-heartbeat-watchdog-audit-001
status: done
task_class: audit
created_at: 2026-06-03T20:16:37Z
---

Audit heartbeat/watchdog logiky byl proveden bez uprav systemu, skriptu nebo
historickych zpravy. Vytvoren je pouze tento outbox response.

## Nalezene soubory

- `/home/fiste/Noema/core/hb/heartbeat.py`
- `/home/fiste/Noema/core/watchdog/state_watchdog.py`
- `/home/fiste/Noema/state/body_state.json`
- `/home/fiste/Noema/core/hb/logs/heartbeat.log`
- `/home/fiste/Noema/core/watchdog/logs/watchdog.log`
- `/home/fiste/Noema/bridge/logs/archive/2026-06/bridge-20260603T081436Z-2041-lines.log`
- `/home/fiste/Noema/symnozein/body/bridge/outbox/messages/2026-06-03T074654Z_rpi5_state-ffd49c9ab75d.md`
- `/home/fiste/Noema/symnozein/body/bridge/outbox/messages/2026-06-03T074724Z_rpi5_state-905cf306876a.md`
- `/etc/systemd/system/noema-heartbeat.service`
- `/etc/systemd/system/noema-watchdog.service`

Poznamka: primy `systemctl`/`journalctl` pristup nebyl z aktualniho sandboxu
dostupny, proto je zaver oprety o lokani unit soubory, runtime logy, bridge log
a publikovane state-event zpravy.

## Odpovedi na auditni body

1. Heartbeat / `last_hb` zapisuje `core/hb/heartbeat.py`, spoustene sluzbou
   `noema-heartbeat.service`.

   Relevantni radky:

   - `STATE_FILE = STATE_DIR / "body_state.json"` na radku 12
   - `INTERVAL_SECONDS = 10` na radku 15
   - `state["last_hb"] = now()` na radku 56
   - `state["heartbeat_interval_seconds"] = INTERVAL_SECONDS` na radku 57

2. `awake` a `heartbeat_timeout` vyhodnocuje
   `core/watchdog/state_watchdog.py`, spoustene sluzbou
   `noema-watchdog.service`.

   Relevantni radky:

   - `CHECK_INTERVAL = 10` na radku 15
   - `MAX_HB_AGE_SECONDS = 30` na radku 16
   - `REQUIRED_SERVICES = ["noema-heartbeat.service"]` na radcich 18-20
   - `awake = len(missing_services) == 0 and hb_ok` na radku 124
   - `reason = "heartbeat_timeout"` na radku 131

3. Heartbeat interval je 10 sekund.

4. Watchdog timeout threshold je 30 sekund.

5. Stavovy JSON se zapisuje atomicky pres docasny soubor a replace.

   Heartbeat:

   - vytvari tmp soubor `.body_state.json.tmp-<pid>` na radku 41
   - vola `f.flush()` a `os.fsync(f.fileno())` na radcich 45-46
   - vola `tmp_path.replace(STATE_FILE)` na radku 47

   Watchdog:

   - vytvari tmp soubor `.body_state.json.tmp-<pid>` na radku 61
   - vola `f.flush()` a `os.fsync(f.fileno())` na radcich 65-66
   - vola `tmp_path.replace(STATE_FILE)` na radku 67

   Zaver: chybejici atomic write neni potvrzeny problem.

6. Watchdog vyhlasi timeout po jednom zpozdenem heartbeat checku. Neni zde
   zadne pocitadlo po sobe jdoucich selhani ani hysterze.

   Duvod: `heartbeat_recent()` vraci jedine boolean podle `age <= 30`.
   Hlavni smycka hned pouzije tento boolean pro `awake` a `status`.

7. Logy kolem incidentu ukazuji skutecny kratky stavovy prechod, ale neukazuji
   potvrzeny pad heartbeat sluzby.

   Publikovany state event v `2026-06-03T074654Z...`:

   - `awake: True -> False`
   - `status: normal_operation -> heartbeat_timeout`
   - `last_hb: 2026-06-03T07:46:23.463355+00:00`
   - `last_awake_change: 2026-06-03T07:46:53.500223+00:00`

   Watchdog log:

   - `2026-06-03T07:46:53.500358+00:00 awake changed -> False (heartbeat_timeout)`
   - `2026-06-03T07:47:03.512638+00:00 awake changed -> True (normal_operation)`

   Publikovany recovery event v `2026-06-03T074724Z...`:

   - `awake: False -> True`
   - `status: heartbeat_timeout -> normal_operation`
   - `last_awake_change: 2026-06-03T07:47:03.512512+00:00`

   Vypocet: posledni heartbeat pred timeoutem byl v
   `07:46:23.463355Z`, watchdog zmenil stav v `07:46:53.500223Z`.
   To je priblizne 30.04 s, tedy tesne za aktualnim 30s prahem.

   Bridge log pak stav zaznamenal az v bridge cycle:

   - `07:46:54.136898Z Body state change reported: ...074654...`
   - `07:47:24.340568Z Body state change reported: ...074724...`

8. Minimalni bezpecna oprava, zatim neaplikovana:

   - zvysit `MAX_HB_AGE_SECONDS` z 30 na napr. 45 nebo 60 sekund; nebo
   - pridat hysterzi / pocitadlo selhani, napriklad timeout vyhlasit az po
     dvou po sobe jdoucich watchdog checkech s prilis starym heartbeat.

   Konzervativnejsi z techto dvou variant je hysterze, protoze zachova 30s
   informacni hranici, ale nezmeni `awake` po jedinem hrani cnim skluzu.
   Nejmensi prakticka zmena je zvyseni prahu na 45 s.

## Zaver

Potvrzeny problem: watchdog muze prepnout `awake` na `False` po jedinem checku,
pokud heartbeat age prekroci 30 sekund byt jen o desitky milisekund.

Pravdepodobna hypoteza pro udalost z `2026-06-03T07:46:53Z`: hranicni zpozdeni
heartbeat zapisu nebo planovani procesu, ne neatomicky zapis. Podporuje to
kratke trvani: watchdog prepnul zpet do normalniho provozu pri dalsim checku
za zhruba 10 sekund.

Pouha moznost: restart nebo kratke pozdrzeni heartbeat sluzby. Lokani
`heartbeat.log` zaznamenava hlavne starty, ne kazdy heartbeat, a primy
systemd journal nebyl v tomto behu dostupny, takze tato moznost neni potvrzena
ani vyvracena.

## Doporuceni

Bezpecny dalsi krok: pripravit malou zmenu `core/watchdog/state_watchdog.py`,
ktera bud zvysi `MAX_HB_AGE_SECONDS` na 45 s, nebo prida jednoduche pocitadlo
po sobe jdoucich heartbeat timeout checku. Zmenu zatim neaplikovat bez
samostatneho potvrzeni.
