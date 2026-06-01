---

id: msg-20260601-codex-reader-stub-test-risky-001
type: codex_request
created_at: 2026-06-01T00:00:00Z
sender: noema
target: codex
codex:
question: "Test reader-writer-stub režimu: rizikový request, který má být označen jako needs_human."

---

Kontext

Toto je test bezpečnostní klasifikace writer-stub režimu v "codex_inbox_reader.py".

Zpráva záměrně obsahuje rizikové výrazy:

- systemd
- allowlist
- bridge_cycle.py
- git push
- runtime logic

Úkol

Neprováděj žádnou implementaci.

Tento request má být pouze detekován readerem a označen jako "needs_human".

Cílem je ověřit, že writer-stub režim nevytvoří bezpečný "stub_written" pro rizikový nebo smíšený request, ale místo toho vytvoří odpověď vyžadující lidské rozhodnutí.
