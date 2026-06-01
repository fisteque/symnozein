---

id: msg-20260601-codex-inbox-reader-dry-run-001
type: codex_request
created_at: 2026-06-01T00:00:00Z
sender: noema
target: codex
codex:
question: "Navrhni a připrav první bezpečný dry-run krok pro samostatný Codex inbox reader."

---

Kontext

Navazujeme na Codexovu odpověď:

"codex-response-20260601-153903-msg-20260529-codex-auto-inbox-reader-design-001"

Shodli jsme se, že automatizace Codex inboxu má začít malým bezpečným krokem:

- neměnit "bridge_cycle.py",
- neměnit bridge runtime logiku,
- neměnit allowlist,
- neměnit systemd timer,
- nespouštět automatické psaní odpovědí,
- nejdřív vytvořit jen specifikaci a dry-run reader.

Cílem je ověřit, že Codex reader může bezpečně detekovat nové požadavky v:

"body/bridge/inbox/messages/codex/"

a klasifikovat je bez vedlejších efektů.

Úkol

Připrav první bezpečný krok pro samostatný Codex inbox reader.

Konkrétně:

1. Zkontroluj aktuální strukturu "body/bridge/inbox/messages/codex/" a "body/bridge/outbox/codex/".

2. Navrhni přesnou specifikaci pro lokální stav:

"body/bridge/state/codex_reader_state.json"

nebo jinou vhodnou runtime-local cestu, pokud je bezpečnější.

Specifikace má obsahovat minimálně:

- "version",
- mapu "processed",
- "message_id",
- "sha256",
- "status",
- "read_at",
- případný "response_path",
- případné "errors".

3. Připrav dry-run skript:

"body/bridge/scripts/codex_inbox_reader.py"

nebo navrhni přesnější umístění, pokud je vhodnější.

Dry-run skript má zatím pouze:

- najít Markdown soubory v "body/bridge/inbox/messages/codex/",
- číst pouze soubory s YAML frontmatterem,
- ignorovat symlinky, skryté soubory a soubory mimo povolený adresář,
- odmítnout příliš velké soubory, např. nad 64 KiB,
- vypočítat "sha256(content)",
- vytáhnout "id", "type", "sender", "target", "created_at",
- klasifikovat request do jedné z tříd:
  - "design_review",
  - "documentation_review",
  - "status_summary",
  - "safety_review",
  - "needs_human",
  - "invalid",
- vypsat, co by udělal,
- nezapisovat žádnou odpověď do outboxu,
- neměnit žádný existující soubor,
- necommitovat,
- nepushovat.

4. Pokud budeš navrhovat změnu dokumentace, připrav ji jako samostatnou malou sekci do vhodného dokumentu, ale neprováděj rozsáhlý refactor.

5. Přidej jednoduchý testovací režim nebo ukázku spuštění, která ověří:

- známý návrhový request by byl klasifikován jako "design_review",
- neznámý nebo rizikový request by skončil jako "needs_human",
- soubor bez frontmatteru by skončil jako "invalid",
- reader nezapisuje mimo povolené cesty.

Omezení

Tento task je pouze pro specifikaci a dry-run.

Neměň:

- "bridge_cycle.py",
- systemd unit/timer,
- bridge allowlist,
- runtime task processing,
- outbound sync pravidla,
- existující inbox/outbox zprávy,
- auditní soubory.

Nezaváděj žádný nový automatický timer.

Nezapisuj odpovědi do "body/bridge/outbox/codex/", kromě své normální Codex odpovědi na tento request.

Neprováděj "git push" nebo force push.

Pokud zjistíš, že implementace dry-run skriptu by vyžadovala změnu runtime hranic, pouze to popiš a skonči návrhem.

Cíl

Cílem není plná autonomie.

Cílem je ověřit první bezpečný článek:

«Codex může samostatně poznat, že má v inboxu nový požadavek, umí ho přečíst, spočítat hash, klasifikovat riziko a říct, co by udělal — zatím bez toho, aby cokoliv vykonal.»

Až bude dry-run opakovaně čistý, další samostatný request může povolit zápis "codex_response" do "body/bridge/outbox/codex/".
