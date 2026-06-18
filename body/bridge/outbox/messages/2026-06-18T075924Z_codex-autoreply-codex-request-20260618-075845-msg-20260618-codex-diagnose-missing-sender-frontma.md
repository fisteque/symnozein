---
id: codex-autoreply-20260618-075924-codex-request-20260618-075845-msg-20260618-codex-diagnose-missing-sender-frontma
type: codex_response
created_at: '2026-06-18T07:59:24.739893Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260618-075845-msg-20260618-codex-diagnose-missing-sender-frontmatter-001
status: answered
source_path: codex/inbox/2026-06-18T075845Z_codex-request-msg-20260618-codex-diagnose-missing-sender-frontmatter-001.md
source_sha256: 405ee593319f27cc10e283028af0bd0324edd300e23ad43f695140baefdad9a8
mode: codex_exec
---

What I read

- `bridge/inbox/processed/2026-06/invalid-msg-20260614-check-next-scheduled-pulse-unknown-001.md`
- `symnozein/body/bridge/inbox/messages/msg-20260614-check-next-scheduled-pulse-unknown-001.md`
- `bridge/logs/archive/2026-06/bridge-20260614T091439Z-5015-lines.log`
- `symnozein/body/bridge/outbox/messages/2026-06-14T081304Z_rpi5_error-86bc5d81ca1b.md`
- `bridge/state/processed_messages.json`
- `bridge/scripts/bridge_agent_v2.py`
- `bridge/outbox/published/2026-06/2026-06-14T082831Z_rpi5_reply-check-next-scheduled-pulse.md`
- current request file/archive for `msg-20260618-codex-diagnose-missing-sender-frontmatter-001`

What follows from it

1. Konkretni soubor, ktery chybu zpusobil:

`bridge/inbox/messages/msg-20260614-check-next-scheduled-pulse-unknown-001.md`

Bridge ho nasledne archivoval jako:

`bridge/inbox/processed/2026-06/invalid-msg-20260614-check-next-scheduled-pulse-unknown-001.md`

Mirror kopie je porad v:

`symnozein/body/bridge/inbox/messages/msg-20260614-check-next-scheduled-pulse-unknown-001.md`

2. Chybelo jen povinne pole `sender`.

Validator v `bridge/scripts/bridge_agent_v2.py` vyzaduje:

`id`, `type`, `created_at`, `sender`, `target`

Problemovy soubor ma `id`, `type`, `target`, `created_at`, ale misto `sender` obsahuje jen:

`created_by: Ondra + Noema`

To se nepocita jako `sender`.

3. Nevypada to jako chyba readeru pri cteni. Chyba vznikla uz ve zdrojove zprave/generovani zpravy, protoze i mirrorovana source kopie v `symnozein/body/bridge/inbox/messages/...` nema `sender`.

Pro existujici soubor by technicky stacilo rucne doplnit napr. `sender: noema`, ale tahle konkretni zprava uz byla po invalidaci zjevne vyrizena pozdejsi odpovedi:

`2026-06-14T082831Z_rpi5_reply-check-next-scheduled-pulse.md`

Takze bych ji bez Ondrova potvrzeni nereprocesoval.

4. Validace sama dela spravnou vec: zpravu odmita a hlasi chybejici pole. Zlepseni by davalo smysl jen pro jasnejsi diagnostiku: do error zpravy/logu pridat i `source_path`, seznam pritomnych frontmatter klicu a pripadne hint typu:

`found created_by, but required field is sender`

What I do not know

- Neoveril jsem puvodni generator/autora te zpravy mimo lokalni soubory.
- Nevim, jestli ma byt kanonicky `sender: noema`, nebo nejaky jiny konkretni sender pro zpravy psane Ondrou/Noemou; podle okolnich zprav nejpravdepodobneji `noema`.

Safe next step

- Pro generator/template zpravy opravit frontmatter tak, aby vzdy zapisoval `sender`.
- U validatoru jen drobne zlepsit error text, ne menit pravidla: `created_by` by nemelo nahrazovat `sender`.
- Existujici invalidni soubor zatim nemenit ani nereprocessovat bez potvrzeni, protoze vec uz byla zodpovezena naslednou bridge odpovedi.

---

source_request: `codex-request-20260618-075845-msg-20260618-codex-diagnose-missing-sender-frontmatter-001`
source_sha256: `405ee593319f27cc10e283028af0bd0324edd300e23ad43f695140baefdad9a8`
