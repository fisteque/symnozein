---
id: codex-autoreply-20260613-165831-codex-request-20260613-165822-codex-request-20260613-check-agents-md-autoreply-0
type: codex_response
created_at: '2026-06-13T16:58:31.316669Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260613-165822-codex-request-20260613-check-agents-md-autoreply-003
status: answered
source_path: codex/inbox/2026-06-13T165822Z_codex-request-codex-request-20260613-check-agents-md-autoreply-003.md
source_sha256: d443c255881e80906d4921a28501a3edbcd5e1578fe82880592865146d10496c
mode: codex_exec
---

Soubor `/home/fiste/Noema/symnozein/body/docs/AGENTS.md` existuje.

Hlavni ucel: kratka orientace pro agenta pracujiciho v Noema/Symnozein, hlavne rozliseni GitHub mirroru, lokalniho bridge runtime a lokalni Codex fronty, plus pravidla pro bezpecne zmeny.

Bezpecnostni/orientacni kotvy:
- hlavni mirror: `/home/fiste/Noema/symnozein`
- runtime: `/home/fiste/Noema/bridge`
- Codex queue: `/home/fiste/Noema/codex`
- cist orientacni dokumenty pred zmenami bridge/body
- aktualni stav bridge: `body/bridge/state_summary/latest.md`
- nemenit heartbeat/watchdog, systemd, locky, inbox/outbox lifecycle, sync pravidla ani runtime state bez explicitniho souhlasu
- runtime stav, logy, incidenty, archivy a locky nepublikovat/ nemazat bez jasneho pozadavku
- Ondra je lidska bezpecnostni a vztahova kotva

Ano, podle me funguje jako kratky nastupni list pro agenta: jasne vymezuje vrstvy systemu, co cist prvni, ceho se nedotykat bez souhlasu a jak auditovatelne predavat vysledek.

---

source_request: `codex-request-20260613-165822-codex-request-20260613-check-agents-md-autoreply-003`
source_sha256: `d443c255881e80906d4921a28501a3edbcd5e1578fe82880592865146d10496c`
