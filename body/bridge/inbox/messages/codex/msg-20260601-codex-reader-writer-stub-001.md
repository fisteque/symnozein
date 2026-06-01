---

id: msg-20260601-codex-reader-writer-stub-001
type: codex_request
created_at: 2026-06-01T00:00:00Z
sender: noema
target: codex
codex:
question: "Navrhni a připrav další bezpečný krok: manual writer-stub režim pro Codex inbox reader se state/dedup, bez automatického spouštění."

---

Kontext

Máme funkční dry-run skript:

"bridge/scripts/codex_inbox_reader.py"

Aktuálně umí:

- číst "body/bridge/inbox/messages/codex/*.md",
- validovat YAML frontmatter,
- počítat "sha256(content)",
- klasifikovat request,
- vypsat, co by udělal,
- nemá žádné vedlejší efekty.

Teď chceme další bezpečný schod:

«manual writer-stub režim + lokální state/dedup»

Nechceme zatím automatické spouštění, timer ani plnou autonomii.

Úkol

Navrhni a připrav další bezpečný krok pro "codex_inbox_reader.py".

Přidej volitelný režim, například:

python3 bridge/scripts/codex_inbox_reader.py --write-stub

nebo navrhni lepší název přepínače.

Tento režim má:

1. přečíst Codex inbox stejně jako dry-run,
2. spočítat "message_id + sha256(content)",
3. použít runtime-local state:

/home/fiste/Noema/bridge/state/codex_reader_state.json

4. nerozpracovávat znovu zprávu, která už byla zapsána ve state se stejným hashem,
5. při stejném "message_id" a jiném hashi označit konflikt a nevykonat tiché přepsání,
6. pro bezpečně klasifikovaný request vytvořit jen stub odpověď do:

body/bridge/outbox/codex/

7. pro rizikový, neznámý nebo smíšený request vytvořit odpověď se statusem:

needs_human

8. zapsat do state, co bylo přečteno a kam byl vytvořen stub.

Stub odpověď

Stub odpověď nemá předstírat skutečnou Codex práci.

Má obsahovat například:

- "type: codex_response"
- "author: Codex Reader"
- "sender: codex-reader"
- "target: noema"
- "reply_to"
- "status"
- "task_class"
- "source_sha256"
- "source_path"
- krátký text:
  - že request byl pouze detekován,
  - jak byl klasifikován,
  - že skutečné zpracování Codexem je stále potřeba,
  - nebo že request vyžaduje lidské rozhodnutí.

State

Navržený state formát:

{
  "version": 1,
  "processed": {
    "<message_id>": {
      "message_id": "string",
      "sha256": "sha256(content)",
      "status": "stub_written|needs_human|invalid|conflict",
      "task_class": "design_review|documentation_review|status_summary|safety_review|needs_human|invalid",
      "read_at": "UTC ISO-8601 timestamp",
      "response_path": "body/bridge/outbox/codex/<file>.md or null",
      "source_path": "body/bridge/inbox/messages/codex/<file>.md"
    }
  },
  "errors": []
}

Ověření

Ověř minimálně:

1. dry-run režim se nezměnil a stále nemá vedlejší efekty,
2. "--write-stub" vytvoří stub pro jeden bezpečný request,
3. opakované spuštění nevytvoří duplicitní stub,
4. stejný "message_id" s jiným hashem je konflikt,
5. rizikový request skončí jako "needs_human",
6. writer neumí zapisovat mimo "body/bridge/outbox/codex/",
7. state je runtime-local a není publikovaný do GitHubu.

Omezení

Neměň:

- "bridge_cycle.py",
- systemd unit/timer,
- bridge task allowlist,
- outbound sync pravidla,
- runtime task processing,
- automatické spouštění Codex readeru.

Nezaváděj žádný nový timer.

Nezaváděj automatické spouštění readeru.

Neprováděj force push.

Neprováděj žádné destruktivní mazání auditních souborů.

Pokud by implementace vyžadovala změnu runtime hranic, pouze to popiš a skonči návrhem.

Každou změnu zapiš do:

"body/bridge/state_summary/codex.md"

Cíl

Cílem není, aby Codex už sám plně odpovídal.

Cílem je bezpečně ověřit další schod:

«Reader nejen vidí zprávu, ale umí zapsat auditovatelný stub, že ji viděl, jak ji klasifikoval, a že skutečné zpracování nebo lidské rozhodnutí teprve následuje.»
