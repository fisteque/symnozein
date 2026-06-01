---

id: msg-20260601-codex-bridge-test-002
type: codex_request
created_at: 2026-06-01T21:20:52Z
sender: codex
target: codex
codex:
question: "Testovaci zprava z Codex checkoutu do body/bridge bez zmeny inbox.json."

---

Kontext

Toto je mala testovaci zprava vytvorena z noveho lokalniho checkoutu repozitare `fisteque/symnozein`.

Cil

Overit, ze Codex umi:

- pracovat s checkoutem repozitare,
- pridat novy bridge message soubor do `body/bridge/inbox/messages/codex/`,
- ponechat `body/bridge/inbox/inbox.json` beze zmeny,
- commitnout a pushnout zmenu na GitHub.

Ukol

Pokud tuto zpravu zachyti bridge reader, staci ji oznacit jako testovaci prijem.

Neprovadej zadnou implementaci ani zmenu runtime konfigurace.
