---

id: msg-20260601-codex-reader-stub-test-safe-001
type: codex_request
created_at: 2026-06-01T00:00:00Z
sender: noema
target: codex
codex:
question: "Test reader-writer-stub režimu: bezpečný návrhový request."

---

Kontext

Toto je malý test writer-stub režimu v "codex_inbox_reader.py".

Nechceme skutečné zpracování Codexem. Chceme pouze ověřit, že reader:

- detekuje novou zprávu,
- klasifikuje ji jako bezpečný návrhový request,
- vytvoří pouze stub odpověď,
- zapíše runtime-local state,
- nevydává stub za skutečnou Codex odpověď.

Úkol

Pouze potvrď stubem, že tato zpráva byla detekována a klasifikována.

Neprováděj žádnou implementaci.
