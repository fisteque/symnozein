---
title: Struktura body
date: 2026-05-27
tags: body, struktura, mapa, orientace
summary: Přehled složky body a význam jednotlivých částí pro orientaci a práci.
---

# Struktura body

Body není úložiště.  
Je to prostor, kde se děje orientace, runtime, audit a návrat ke směru.

Tento soubor slouží jako orientační mapa hlavních vrstev systému.

---

# Hlavní vrstvy

## body/

Kořen stavového prostoru.

Obsahuje:
- indexy,
- diffy,
- návštěvy,
- stavové kotvy,
- bridge runtime audit,
- sdílené vrstvy,
- a orientační dokumenty.

Důležité soubory:

- `body/body_index.json`
- `body/body_diff.md`
- `body/index_menu.json`
- `body/struktura_body.md`

---

# Aktivní runtime vrstva

## body/bridge/

Nejdůležitější aktivní vrstva systému.

Bridge propojuje:
- GitHub audit,
- inbox/outbox zprávy,
- RPi runtime,
- tasky,
- summary vrstvu,
- dokumentační vrstvu,
- a reflexní cyklus.

Bridge není daemon.
Běží přes pravidelný systemd cycle.

---

## body/bridge/inbox/

Auditní vstupní páska bridge na GitHubu.

Obsahuje:
- `task_request`
- `codex_request`
- další budoucí message typy

Aktuální runtime agent nečte GitHub inbox přímo. Inbound sync nejdřív hydratuje
živou runtime frontu:

- `/home/fiste/Noema/bridge/inbox/messages/`

Po zpracování runtime zprávy se lokálně archivují mimo GH pásku.

---

## body/bridge/outbox/

Výstupní auditní zprávy.

Obsahuje:
- `task_result`
- `error`
- bridge cycle a watchdog incidenty
- budoucí reflexní zprávy

GitHub `body/bridge/outbox/messages/` je auditní páska. Živý runtime outbox je:

- `/home/fiste/Noema/bridge/outbox/messages/`

Po úspěšném publishi se runtime zprávy přesouvají do lokálního published
archivu.

---

## body/bridge/state_summary/

Veřejná orientační vrstva bridge.

### latest.md

Krátký aktuální stav:
- heartbeat,
- inbox/outbox counts,
- processed state,
- error count,
- log tail.

Není source of truth.
Je to orientační puls systému.

## body/bridge/systemd/

Auditní kopie systemd jednotek, které patří k bridge vrstvě.

Aktuálně obsahuje watchdog jednotky:
- `bridge-watchdog.service`
- `bridge-watchdog.timer`

Instalované runtime jednotky žijí v `/etc/systemd/system/`. Lokální pracovní
kopie jednotek je v:

- `/home/fiste/Noema/bridge/systemd/`

## body/bridge/docs/

Dokumentační vrstva bridge.

### implementation_ledger.md

Implementační ledger. Dříve `state_summary/codex.md`.

Obsahuje:
- poslední architektonické změny,
- důležité opravy,
- publikované commity,
- a významové změny systému.

Slouží pro orientaci:
- člověka,
- Codexu,
- Noemy.

### known_limits.md

Provozní kotva známých limitů a neověřených cest.

Rozlišuje:
- ověřené chování,
- návrhy,
- transportní mezery,
- cesty, které zatím nejsou funkční.

### bridge_scripts.md

Přehled jednotlivých skriptů mostu a jejich rolí.

### MOST_A_NERVY.md

Krátký orientační dokument k mostu a nervové vrstvě.

---

## body/bridge/logs/

Runtime logy bridge.

Plný runtime log se už nepublikuje na GitHub. Runtime log a jeho archivy jsou
lokální. Veřejný filtrovaný stav je v `state_summary/latest.md`.

## /home/fiste/Noema/bridge/incidents/

Lokální incident log bridge watchdogu.

Není součást GH mirroru a není auditní páskou. Slouží jako lokální černá
skříňka, aby incident existoval i tehdy, když most právě neumí publikovat ven.

---

## body/bridge/scripts/

Aktivní bridge skripty.

Obsahuje:
- bridge cycle,
- sync vrstvy,
- task runner,
- summary generátory,
- lock systém,
- bridge watchdog,
- auditní vrstvy.

Důležité soubory:
- `bridge_cycle.py`
- `bridge_sync_inbound.py`
- `bridge_sync_outbound.py`
- `bridge_agent_v2.py`
- `bridge_watchdog.py`
- `codex_inbox_reader.py`
- `write_bridge_summary.py`

---

## body/bridge/scripts/tasks/

Allowlisted tasky.

Tasky:
- nejsou spouštěny shellově,
- mají timeout,
- používají allowlist,
- a auditují výsledky.

Viz:
- `TASK_REQUESTS.md`
- `allowlist.json`

---

# Navštěva

## body/navsteva/

Vrstva vědomé orientace.

Navštěva:
- není hledání novinek,
- ale návrat k realitě systému.

Obsahuje:
- pravidla návštěvy,
- audit návštěv,
- orientační log.

Důležité:
- `navsteva_body.md`
- `navsteva.log`

---

# Stavové kotvy

## body/SK/

Stabilní významové body systému.

Nejde o runtime.
Jde o:
- orientaci,
- kontinuitu,
- významové milníky.

---

# Shared

## body/shared/

Sdílené vrstvy mezi:
- runtime,
- bridge,
- návštěvou,
- a dalšími částmi systému.

Může obsahovat:
- anchors,
- protokoly,
- společné konfigurace,
- orientační vrstvy.

---

# Diff a indexy

## body/body_index.json

Hlavní orientační index body.

Obsahuje:
- aktivní větve,
- soubory,
- summaries,
- bridge vrstvy,
- a stavové orientace.

## body/body_diff.md

Záznam posledních změn.

Slouží pro:
- rychlou orientaci,
- návrat ke změně,
- a detekci aktivních větví.

---

# Důležité principy

- Runtime není GitHub.
- GitHub je auditní a orientační vrstva.
- Navštěva má přednost před domněnkou.
- Summary není source of truth.
- Bridge nesmí tiše selhávat.
- Audit je důležitější než dokonalost.
- Body není databáze.
- Body je opěrný vztah ke stavu systému.
