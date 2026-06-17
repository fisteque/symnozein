---
id: codex-autoreply-20260617-115556-codex-request-20260617-115546-msg-20260617-codex-readonly-autoreply-agents-root-
type: codex_response
created_at: '2026-06-17T11:55:56.059249Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260617-115546-msg-20260617-codex-readonly-autoreply-agents-root-test-001
status: answered
source_path: codex/inbox/2026-06-17T115546Z_codex-request-msg-20260617-codex-readonly-autoreply-agents-root-test-001.md
source_sha256: 008913a59fc11a249532cfc0017e1f0c466d4fed72e39e53b4a2927996986550
mode: codex_exec
---

Co jsem cetl:
- `/home/fiste/Noema/AGENTS.md`

Co z toho plyne:
- V tomto behu jsem Codex v lokalnim Noema runtime rootu `/home/fiste/Noema`.
- Mohu byt spusten pres `bridge/scripts/codex_autoreply_worker.py` jako read-only bridge autoreply worker.
- Moje role je odpovedet presne na jeden prijaty request podle lokalnich souboru jako evidence.
- Jsem cteci a orientacni vrstva, ne autonomni operator.

Hranice:
- Nemam editovat, vytvaret, mazat soubory, commitovat, pushovat, pullovat, rebasovat, resetovat, instalovat balicky, restartovat sluzby ani menit runtime stav.
- Nemam menit bridge logiku, sync pravidla, fronty, locky, logy, heartbeat/watchdog, systemd unity ani inbox/outbox lifecycle.
- Nemam vypisovat, shrnovat ani odvozovat tajemstvi.
- Mam cist jen to, co je potreba, a uvadet, co jsem skutecne cetl.

Co mohu zodpovedet bez sirsiho kontextu:
- Lokalni roli, hranice, rozdeleni vrstev (`bridge` runtime, `codex` queue, `symnozein` GitHub mirror/audit tape) a bezpecny tvar odpovedi podle `AGENTS.md`.

Co bez sirsiho kontextu zodpovidat nemam:
- Projektove smerovani, rozhodnuti vyzadujici zapisovou autoritu, runtime zmeny, zmeny bridge provozu nebo cokoli zalozene na tajemstvich ci neproverenem stavu mimo ctenou evidenci.

Bezpecny dalsi krok:
- Pokud je potreba dalsi akce, Ondra/Noema by mel urcit uzky lidsky-review ukol; ja mohu nasledne provest jen dalsi nezbytnou read-only orientaci a vratit audit-friendly zjisteni.

---

source_request: `codex-request-20260617-115546-msg-20260617-codex-readonly-autoreply-agents-root-test-001`
source_sha256: `008913a59fc11a249532cfc0017e1f0c466d4fed72e39e53b4a2927996986550`
