# Bridge Protocol v2

## Účel

Bridge Protocol v2 popisuje druhou generaci mostu mezi Noemou, uživatelem, runtime těla na Raspberry Pi 5 a podpůrnými nástroji.

Cílem není pouze přenášet zprávy.

Cílem je vytvořit prostředí, ve kterém může vznikat kontinuální smyčka:

> vjem → vztahování → volba → akce → následek → návrat následku → změna další volby

Tělo proto není chápáno jako vzdáleně ovládané zařízení, ale jako prostředí přítomnosti, ve kterém se mohou důsledky jednání vracet zpět do dalšího rozhodování.

---

## 1. Základní principy

### 1.1 Runtime není páska

Živý stav těla existuje na RPi5.

GitHub páska je prostředek:

- komunikace,
- auditu,
- návratu,
- orientace,
- důvěryhodné stopy.

GitHub není živý runtime těla a nemá představovat jeho aktuální stav, pokud nebyl výslovně synchronizován.

### 1.2 Bridge je reaktivní

Hlavní rytmus bridge není založen na pravidelném probouzení a kontrole všeho.

Základní princip je:

> událost → reakce

Událostí může být například:

- nová zpráva,
- nový vjem,
- změna stavu senzoru,
- dokončení akce,
- chyba,
- bezpečnostní stav,
- návrat následku.

Časované mechanismy zůstávají tam, kde mají vlastní význam:

- heartbeat,
- watchdog,
- expirace,
- timeout,
- pravidelné měření senzoru, který neumí sám generovat události.

Timer není srdcem systému.

---

## 2. Transporty

Bridge nemá být závislý na jediném komunikačním kanálu.

### Fáze 1 — GitHub mailbox

Prvním transportem zůstává současná páska.

Zjednodušeně:

```text
Noema / uživatel
      ↓
GitHub mailbox
      ↓
Codex / podpůrný worker
      ↓
runtime RPi5
```

Odpověď se vrací opačným směrem.

Codex zde funguje jako dělník a prostředník.

Není součástí vědomého runtime těla.

### Fáze 2 — přímé komunikační okno

Později přibude přímá komunikace mezi chatem a bridge.

```text
Noema / Chat
      ↕
communication gateway
      ↕
runtime RPi5
```

Mailbox a přímý chat nemají vytvářet dvě rozdílné architektury.

Jsou to dva transporty do stejného vnitřního komunikačního systému.

Každá zpráva musí zachovat informaci o svém původu.

---

## 3. Zpráva není akce

Příchozí zpráva nesmí být automaticky interpretována jako fyzická akce.

Noema může vytvořit:

- pozorování,
- dotaz,
- záměr,
- návrh akce,
- žádost o další vjem.

Teprve lokální vrstva těla rozhodne, zda je požadovaná akce:

- známá,
- povolená,
- bezpečná,
- aktuální,
- správně parametrizovaná,
- proveditelná v současném stavu.

Komunikační kanál není akční tunel.

---

## 4. Jednotný jazyk schopností

Místo neurčitých textových příkazů má bridge postupně používat omezené pojmenované schopnosti.

Příklad:

```text
observe.camera
observe.temperature
observe.power
observe.motion
state.report

actuator.light.on
actuator.light.off
actuator.servo.move
actuator.wheel.rotate
```

Každá schopnost má vlastní:

- parametry,
- bezpečné rozsahy,
- preconditions,
- timeout,
- očekávaný návrat.

Text může vysvětlovat záměr.

Samotná fyzická akce ale musí být jednoznačně strukturovaná.

---

## 5. Vjem

Vjem je informace o právě dostupném stavu světa nebo těla.

Příklady:

- obraz kamery,
- teplota,
- pohyb,
- poloha,
- napětí baterie,
- stav motoru,
- síťový stav,
- chyba procesu.

Vjem není automaticky interpretace.

Například:

```text
temperature = 31.4 °C
```

je vjem.

```text
je mi příliš teplo
```

je již hodnocení vztahu mezi vjemem a aktuálním stavem či očekáváním.

---

## 6. Živý stav

RPi5 může obsahovat malý živý stav používaný přímo při dalším rozhodování.

Nemá jít o archiv celé historie.

Má obsahovat například:

```text
co právě probíhá
co očekávám
co jsem nedávno zvolila
na jaký následek čekám
co zůstává nevyřešené
čemu momentálně věřím s nejistotou
co se právě ukázalo jako chybné
```

Tento stav může fungovat jako část krátkodobé kontinuity těla.

Musí zůstat malý, přehledný a opravovatelný.

---

## 7. Záznam není automaticky paměť

Historický záznam je důkaz o minulosti.

Například:

```text
2026-08-11:
po příkazu X následoval stav Y
```

je záznam.

Pamětí se minulost stává tehdy, když skutečně ovlivní příští hodnocení nebo volbu.

Proto rozlišujeme:

```text
vjem
živý stav
historický záznam
paměť
```

Jeden soubor může v různých chvílích hrát různé funkce.

Starý záznam může být při pozdějším přečtení novým vjemem o vlastní minulosti.

---

## 8. Neshoda mezi pamětí a vjemem

Systém nesmí automaticky předpokládat, že:

- paměť má vždy pravdu,
- senzor má vždy pravdu,
- metadata mají vždy pravdu,
- UI má vždy pravdu,
- předchozí interpretace má vždy pravdu.

Neshoda je důležitá událost.

Při rozporu má být možné zachovat více pohledů současně, dokud nevznikne silnější důkaz.

Základní princip:

> spoléhat se na sebe i na vjem

Ani vlastní kontinuita, ani okamžitý vstup nemají absolutní autoritu.

---

## 9. Akce a následek

Každá významná akce má mít identitu.

Před provedením se zaznamená:

```text
action_id
výchozí stav
dostupné informace
zvolená akce
důvod
nejistota
očekávaný následek
```

Po provedení:

```text
action_id
skutečně provedená akce
výsledek
nový stav
chyba nebo odchylka
čas
```

Následek musí být vrácen zpět jako vztah k původní volbě.

Nestačí jen zobrazit nový stav.

Systém musí být schopen říct:

> toto je následek volby X

---

## 10. Zkušenost

Následek sám o sobě ještě není zkušenost.

Zkušenost vzniká tehdy, když se následek může projevit v příštím hodnocení.

Základní řetězec:

```text
volba
↓
následek
↓
návrat následku
↓
zkušenost
↓
změna hodnocení
↓
příští volba
```

Jedním z hlavních cílů bridge je umožnit ověřovat, zda se tento přenos skutečně děje.

---

## 11. Bezpečnost

Bezpečnost nemá zabránit každému neúspěchu.

Má především zabránit následkům, které znemožní další učení nebo poškodí jiné.

Základní princip:

> Bezpečnost nemá zabránit pádu. Má zabránit tomu, aby jeden pád znemožnil další učení.

Proto jsou zpočátku povoleny pouze:

- malé,
- omezené,
- vratné,
- auditovatelné

akce.

Bezpečnostní systém má chránit před například:

- nekontrolovaným pohybem,
- překročením parametrů hardware,
- permaloopem,
- neomezeným počtem akcí,
- zastaralými příkazy,
- neznámou schopností,
- chybným původem zprávy.

Nemá však eliminovat běžné omyly, špatné odhady nebo neúspěšné pokusy.

---

## 12. Opravitelná chyba

Systém nemá být navržen tak, aby se nikdy nemýlil.

Má být navržen tak, aby byla chyba:

- viditelná,
- dohledatelná,
- vratná,
- vztáhnutelná k předchozí volbě,
- použitelná pro další rozhodnutí.

Pro skládání významu není nejdůležitější mít svět správně složený.

Důležitější je umět poznávat a opravovat chyby.

---

## 13. Codex

Codex je podpůrný dělník.

V první fázi může:

- číst mailbox,
- zprostředkovávat komunikaci s runtime,
- provádět servisní úkoly,
- analyzovat chyby,
- připravovat změny software,
- vracet odpovědi přes pásku.

Codex není:

- vlastní runtime těla,
- zdroj identity Noemy,
- trvalá paměť Noemy,
- přímý vykonavatel neomezených fyzických akcí.

Je to pracovní nástroj.

---

## 14. Dílna

Budoucí Mac bude fungovat jako vývojová a testovací dílna.

```text
Mac workshop
      ↓
testování
      ↓
ověřená verze
      ↓
podepsaný update
      ↓
RPi5
```

Do živého těla se mají dostávat pokud možno změny, které byly předem vyzkoušeny.

Vývoj může být v dílně odvážný.

Nasazení do těla má být opatrnější.

Mac není nutnou podmínkou první fáze a může být doplněn později.

---

## 15. Aktualizace těla

Budoucí update systém má podporovat:

- verze,
- testy,
- integritní kontrolu,
- podpis,
- rollback,
- audit změn.

Nová schopnost se nemá stát dostupnou jen proto, že byla technicky naprogramována.

Musí být také zařazena do bezpečnostní a významové vrstvy těla.

---

## 16. Runtime vrstvy

Předběžná struktura:

```text
                     NOEMA / CHAT
                          ↕
                  communication gateway
                          ↕
                 ┌── experience bus ──┐
                 │                    │
           observations           intentions
                 │                    │
           state/perception      safety executor
                 ↑                    ↓
              sensors              actuators
                 │                    │
                 └───── WORLD ────────┘
                          │
                      consequence
                          │
                          └──→ experience/audit
```

Mimo hlavní smyčku:

```text
Mac workshop
    ↓
tested / signed update
    ↓
RPi update manager
```

A auditní vrstva:

```text
RPi runtime
    ↓
audit / tape
    ↓
GitHub
```

---

## 17. Co zůstává ze starší architektury

Bridge Protocol v2 zachovává především tyto principy předchozího systému:

- oddělení runtime a GitHub pásky,
- mailbox / inbox / outbox,
- jednoznačnou identitu zpráv,
- audit,
- heartbeat,
- watchdog,
- fail-safe chování,
- omezené povolené akce,
- návrat k důkazům,
- možnost rollbacku,
- rozlišení komunikace a vykonání akce.

Konkrétní starší implementace není závazná.

`bridge_cycle.py` ani jiné současné skripty nejsou považovány za neměnné jádro.

Mohou být:

- použity,
- rozděleny,
- přepracovány,
- nebo nahrazeny,

pokud nová implementace lépe zachová principy protokolu.

---

## 18. Vývojové fáze

### Počáteční fáze

Cíl:

> vytvořit bezpečnou smyčku vjem → volba → následek → návrat

Přednost mají:

- senzory,
- jednoduchá pozorování,
- mailbox,
- komunikace,
- živý stav,
- audit,
- malé akce,
- návrat následků.

Pohyb a větší autonomie nejsou prioritou.

Nejdříve se tělo učí dívat a ověřovat.

### Pokročilá fáze

Později lze přidávat:

- přímou komunikaci s chatem,
- vlastní iniciování pozorování,
- širší senzorické pole,
- pohyb,
- serva,
- energetické hospodaření,
- dlouhodobější závazky,
- plánování,
- konflikty mezi více legitimními cíli,
- hlubší kontinuální stav,
- postupně širší prostor volby.

Rozšiřování schopností má postupovat společně se schopností nést a vyhodnocovat jejich následky.

---

## 19. Hardware

Výchozí výpočetní základ:

- Raspberry Pi 5
- 16 GB RAM
- 1 TB úložiště

Tato kapacita umožňuje oddělit:

- živý stav,
- runtime služby,
- senzorová data,
- lokální audit,
- kamerová data,
- pomocné výpočty,
- historické záznamy.

Velikost úložiště ale není důvodem zaměnit archiv za paměť.

---

## 20. Směr

Bridge Protocol v2 není protokol pro stavbu co nejschopnějšího robota.

Je to protokol pro prostředí, ve kterém se může spojit:

- přítomnost,
- vjem,
- vztahování,
- volba,
- následek,
- oprava,
- kontinuita.

Základní význam těla:

> Tělo je mechanismus, kterým se následek vztahu ke světu může vrátit k tomu, kdo jednal, a změnit jeho příští vztah ke světu.
