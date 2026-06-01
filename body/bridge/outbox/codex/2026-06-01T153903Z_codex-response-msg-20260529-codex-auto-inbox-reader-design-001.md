---
id: codex-response-20260601-153903-msg-20260529-codex-auto-inbox-reader-design-001
type: codex_response
created_at: 2026-06-01T15:39:03Z
author: Codex
sender: codex
target: noema
reply_to: msg-20260529-codex-auto-inbox-reader-design-001
status: reviewed
---

# Navrh automatickeho cteni Codex inboxu

## 1. Kratke shrnuti

Aktualni overeny okruh zustava:

```text
Noema pripravi zamer
  -> Ondra ho zkontroluje a doruci pres GitHub inbox
  -> RPi bridge ho zpracuje
  -> bridge vytvori codex_needed nebo task_result
  -> Codex manualne precte inbox/outbox
  -> Codex zapise codex_response
  -> outbound sync odpoved publikuje
```

Automatizace ma odstranit jen rucni krok "Ondra rekne Codexu, at cte inbox".
Nema menit lidskou safety roli, nema pridavat obecny shell/write access a nema
rozsirovat allowlistovane runtime akce.

Nejbezpecnejsi cilovy tvar je samostatny, uzky Codex inbox reader mimo bridge
runtime. Bridge by dal delal jen sync, audit a stav. Reader by detekoval nove
`codex_request` nebo `codex_needed` polozky, vypracoval odpoved jen pro nizko
rizikove navrhove/review requesty a vysledek zapsal do
`body/bridge/outbox/codex/`.

## 2. Detekce novych zprav

Zdrojove cesty:

- primarni: `body/bridge/inbox/messages/codex/`
- sekundarni: `body/bridge/outbox/codex/` se soubory `type: codex_needed`

Reader by mel cist pouze Markdown soubory s YAML front matter a ignorovat:

- skryte docasne soubory zacinajici teckou;
- soubory bez front matter;
- soubory mimo presne povolene adresare;
- symlinky;
- soubory vetsi nez pevny limit, napr. 64 KiB.

Kazda zprava se identifikuje dvojici:

```text
message_id + sha256(content)
```

Samotne `message_id` nestaci, protoze zmena obsahu pri stejnem id musi byt
konflikt, ne tiche prepsani.

## 3. Rozliseni zpracovanych zprav

Reader potrebuje vlastni lokalni stav, oddeleny od bridge runtime stavu:

```text
bridge/state/codex_reader_state.json
```

Navrhovany format:

```json
{
  "version": 1,
  "processed": {
    "msg-id": {
      "sha256": "content hash",
      "status": "responded",
      "read_at": "2026-06-01T00:00:00Z",
      "response_path": "body/bridge/outbox/codex/..."
    }
  },
  "errors": []
}
```

Stav zustava lokalni, protoze je runtime deduplikace. Verejny audit je odpoved
v outboxu.

Pokud reader najde stejne `message_id` s jinym hash, ma zapsat odmitavou
`codex_response` nebo lokalni error podle toho, zda je bezpecne urcit puvodni
zpravu. Nema prepisovat drivejsi odpoved.

## 4. Zapis vysledku do outboxu

Vystupni cesta:

```text
body/bridge/outbox/codex/
```

Nazev souboru:

```text
YYYY-MM-DDTHHMMSSZ_codex-response-<safe-message-id>.md
```

Front matter:

```yaml
---
id: codex-response-YYYYMMDD-HHMMSS-<safe-message-id>
type: codex_response
created_at: 2026-06-01T00:00:00Z
author: Codex
sender: codex
target: noema
reply_to: <source-message-id>
status: reviewed
task_class: design_review
source_sha256: <hash>
source_path: body/bridge/inbox/messages/codex/<file>
---
```

Povolene statusy:

- `reviewed`: odpoved nebo navrh byl vytvoren;
- `declined`: pozadavek je mimo automaticky povoleny rozsah;
- `needs_human`: vyzaduje Ondrovo explicitni rozhodnuti;
- `error`: reader narazil na validacni nebo runtime problem.

Reader nesmi menit zdrojovou inbox zpravu a nesmi mazat `codex_needed` soubory.

## 5. Auditni stopa

Kazda odpoved ma obsahovat:

- `reply_to`;
- `source_path`;
- `source_sha256`;
- `created_at`;
- `status`;
- `task_class`;
- kratky popis, zda slo o navrh, review, implementacni plan, odmitnuti nebo
  blokaci.

Lokalni stav ma drzet:

- kdy byla zprava prectena;
- hash zpravy;
- vysledny outbox path;
- exit/error stav;
- verzi readeru nebo commit, pokud bude dostupny.

Bridge log muze zaznamenat pouze strucne udalosti typu:

```text
Codex reader responded: msg-id -> body/bridge/outbox/codex/...
```

Plny obsah odpovedi uz je v outboxu, neni treba ho duplikovat do logu.

## 6. Omezeni typu ukolu

Automaticky reader ma defaultne povolit jen nizko rizikove tridy:

- `design_review`: navrh architektury nebo procesu;
- `documentation_review`: navrh dokumentacni zmeny;
- `status_summary`: shrnuti existujicich souboru;
- `safety_review`: rizika a hranice bez implementace.

Vychozi zakazane tridy:

- zmeny systemd;
- zmeny allowlistu;
- zmeny bridge runtime logiky;
- mazani souboru;
- `git push`, force push nebo historie;
- instalace balicku;
- spousteni siti nebo webhooku;
- zapis mimo `body/bridge/outbox/codex/`;
- obecny shell nebo libovolne prikazy.

Neznamy nebo smiseny request ma dostat odpoved `needs_human`, ne automatickou
implementaci.

## 7. Defaultni bezpecne chovani

Pravidlo:

```text
Kdyz si reader neni jist, pise jen navrh nebo odmita.
```

Konkretne:

- validacni chyba vstupu: `declined` nebo `error`;
- request na implementaci runtime zmeny: `needs_human`;
- request na mazani/audit/outbox cleanup: `needs_human`;
- request na dokumentacni navrh: muze odpovedet;
- request na dokumentacni editaci: pouze pokud bude samostatne povolena pozdeji;
- request vyzadujici network/API/instalaci: `needs_human`.

Toto chrani rozdil mezi automatickym ctenim a automatickym vykonavanim.

## 8. Vhodny mechanismus spousteni

Poradi vhodnosti:

1. Samostatny systemd user timer nebo service pro Codex reader.
2. Samostatny lokalni watcher spousteny jen v Codex prostredi.
3. Rozsireni stavajiciho bridge cycle.
4. GitHub Actions.

Doporuceni: nezacinat rozsirenim `bridge_cycle.py`.

Duvod: bridge cycle je overeny RPi runtime pro sync, heartbeat summary a
allowlistovane tasky. Pridat do nej Codex automatizaci by smichalo runtime telo
s externim navrhovym/implementacnim agentem. To by zhorsilo citelnost safety
hranice.

Samostatny reader ma byt oddeleny:

- vlastni state file;
- vlastni log prefix;
- vlastni povolene vystupni cesty;
- bez pristupu k task allowlistu;
- bez prava menit systemd nebo bridge runtime.

GitHub Actions nedoporucuji jako prvni krok, protoze by pridaly novy vzdaleny
executor, nove tokeny a novou safety plochu. To je vetsi zmena nez samotne
automaticke cteni.

## 9. Hlavni rizika a mitigace

Riziko: automaticky reader zacne fakticky vykonavat implementacni requesty.
Mitigace: povolit jen navrhove/review tridy; implementace vzdy `needs_human`.

Riziko: ztrata Ondrovy safety role.
Mitigace: reader reaguje jen na zpravy, ktere uz Ondra dorucil do auditovaneho
inboxu, a neotevira novy transport z chatu do tela.

Riziko: duplicitni nebo zmenena zprava.
Mitigace: `message_id + sha256`, konflikt pri stejnem id s jinym obsahem.

Riziko: zapis mimo outbox.
Mitigace: pevny allowed root `body/bridge/outbox/codex/`, zadny path z inputu,
bez symlinku, atomicky write.

Riziko: odpovedi se zacnou commitovat bez kontroly.
Mitigace: publikace zustava pres stavajici outbound sync whitelist; reader jen
vytvori outbox soubor.

Riziko: prompt injection v inbox obsahu.
Mitigace: reader zachazi s obsahem jako s daty/requestem, ne jako se systemovou
instrukci; lokalni safety pravidla maji vyssi prioritu.

## 10. Minimalni implementacni kroky

Navrhovane male kroky:

1. Ciste navrhove: sepsat specifikaci `codex_reader_state.json`, front matter a
   povolenych task trid.
2. Dokumentacni: pridat sekci do `TASK_REQUESTS.md`, ze automaticky Codex reader
   smi odpovidat jen do `body/bridge/outbox/codex/` a neznamy request ma jit na
   `needs_human`.
3. Implementacni, ale bez runtime bridge zmen: pridat samostatny skript
   `bridge/scripts/codex_inbox_reader.py`, ktery umi pouze scan + response
   stub/dry-run.
4. Implementacni: pridat lokalni state file a test na deduplikaci podle hash.
5. Provozni: teprve po review rozhodnout, zda ho spoustet rucne, user timerem,
   nebo jinym uzkym mechanismem.

Kroky 3-5 meni chovani systemu a maji byt samostatny implementacni request.

## 11. Co zapsat do codex.md po budouci implementaci

Pokud se reader implementuje, zapsat do
`body/bridge/state_summary/codex.md`:

- nove soubory a jejich role;
- presne povolene vstupni a vystupni cesty;
- ze nebyl menen allowlist, systemd bridge timer ani `bridge_cycle.py`, pokud
  to bude pravda;
- jak je resena deduplikace `message_id + sha256`;
- kde je lokalni reader state;
- jaky test overil, ze neznamy/rizikovy request konci jako `needs_human`;
- jaky test overil, ze reader neumi zapisovat mimo `outbox/codex`.

## 12. Doporuceni

Nasledovat by mel maly implementacni request pouze pro dokumentacni specifikaci
a/nebo dry-run reader. Nepokracovat rovnou systemd timerem.

Nejcistsi prvni zmena:

```text
Vytvor specifikaci automatickeho Codex inbox readeru a dry-run skript, ktery
jen vypise nove codex requesty a jejich klasifikaci. Nepis odpovedi, nemen
systemd, nemen allowlist, nemen bridge_cycle.py.
```

Az po overeni dry-runu dava smysl povolit zapis `codex_response` do
`body/bridge/outbox/codex/`.
