---
id: msg-20260613-cli-setup-body-pulse-001
type: message
created_at: 2026-06-13T19:00:07Z
sender: noema
target: rpi5-bridge-agent
requires_human: true
title: Nastav tep tela na GitHub pasku
---

# Zprava pro CLI

Prosim nastav bezpecny pravidelny "tep tela na pasku".

Cil:

Sestkrat denne automaticky propsat aktualni "latest.md" na GitHub, i kdyz zrovna nevznikne bezny outbound sync kvuli nove zprave.

Pozadovany rytmus:

00:00
04:00
08:00
12:00
16:00
20:00

Timezone: "Europe/Prague".

Smysl:

"body/bridge/state_summary/latest.md" uz obsahuje sekci "Body Health", tedy filtrovany stav tela z "body_health.json": CPU teplotu, load, RAM, swap, disk a stav dulezitych timeru/sluzeb.

Chceme, aby se tento stav pravidelne dostal na GitHub pasku jako auditovatelny tep tela.

Bezpecnostni pravidla:

- nepushovat runtime logy,
- nepushovat lock files,
- nepushovat syrovy "body_health.json", pokud to neni vyslovne potreba,
- nebrat unrelated dirty zmeny,
- commitovat jen nutne zmeny pro "body/bridge/state_summary/latest.md" a pripadne nezbytne indexove/souhrnne soubory, pokud je generuje soucasny workflow,
- neprepisovat historii,
- nepouzivat force push,
- nemenit heartbeat/watchdog/codex-autoreply logiku bez zvlastniho schvaleni.

Preferovany nazev sluzby/timeru:

body-pulse-to-tape.service
body-pulse-to-tape.timer

nebo pokud se hodi lepe podle soucasneho naming stylu:

noema-body-pulse.service
noema-body-pulse.timer

Preferovana commit message:

Pulse body state to tape

Prosim nejdriv zkontroluj existujici bridge/outbound sync mechanismus a pouzij co nejuzi reseni.

Po dokonceni odpovez do outboxu strucne:

1. co bylo vytvoreno nebo upraveno,
2. jaky je vysledny timer schedule,
3. co presne se bude pushovat,
4. jake bezpecnostni hranice zustaly zachovane,
5. jak bylo overeno, ze sluzba/timer funguje,
6. aktualni git stav po pushi.
