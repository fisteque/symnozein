---
id: codex-autoreply-20260617-111142-codex-request-20260617-111111-msg-20260617-codex-readonly-autoreply-path-test-00
type: codex_response
created_at: '2026-06-17T11:11:42.829339Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260617-111111-msg-20260617-codex-readonly-autoreply-path-test-001
status: answered
source_path: codex/inbox/2026-06-17T111111Z_codex-request-msg-20260617-codex-readonly-autoreply-path-test-001.md
source_sha256: f16a5e57b668bb6eb1e58638f1d5b24b88016a377d5adc77de5bdcf434c942d0
mode: codex_exec
---

Co jsem cetl

- `bridge/scripts/bridge_agent_v2.py`
- `bridge/scripts/codex_autoreply_worker.py`
- `bridge/PLAN_bridge_agent.md`
- relevantni cast `bridge/scripts/tasks/TASK_REQUESTS.md`

Co z toho plyne

1. `bridge_agent_v2.py` je file-based runtime bridge agent. Cte zpravy z `bridge/inbox/messages`, validuje frontmatter, deduplikuje podle stavu, archivuje zpracovane zpravy, zapisuje odpovedi do outboxu, umi spustit jen allowlistovane tasky a pro `type: codex_request` vytvori pending pozadavek do `codex/inbox`.

2. `codex_autoreply_worker.py` zpracuje jeden lokalni `codex_request` z `codex/inbox`. Umi dry-run, stub odpoved, nebo spustit `codex exec` v read-only sandboxu. Vystup zapisuje jako `codex_response` do `bridge/outbox/messages`, archivuje request do `codex/processed` a eviduje stav v `bridge/state/codex_autoreply_state.json`.

3. Hlavni bezpecnostni hranice autoreply workeru:
- akceptuje jen Markdown s frontmatter a povinnymi poli `id`, `type`, `created_at`, `sender`, `target`;
- `type` musi byt `codex_request`, `target` musi byt `codex`;
- cte request max. 64 KiB a odpoved Codexu max. 128 KiB;
- pri `--run-codex` pouziva `approval_policy="never"`, `--sandbox read-only`, `--cd /home/fiste/Noema`;
- prompt vyslovne zakazuje editace, commit, push, delete, install, restart a zmenu runtime stavu;
- rizikove terminy jako `systemd`, `allowlist`, `bridge_cycle.py`, `git push`, `delete`, `network`, `install`, `commit`, `runtime logic` klasifikuje jako `needs_human`, pokud nejsou jen v negovanem kontextu;
- bez `--allow-needs-human` nespusti Codex pro request oznaceny `needs_human`;
- zapisove efekty workeru jsou omezeny na odpoved do outboxu, archivaci requestu a vlastni stav; deklaruje, ze necommituje a nepushuje.

4. Bez sirsiho kontextu mohu odpovedet hlavne na read-only otazky dolozitelne z lokalnich souboru: co dela konkretni skript, jake ma vstupy/vystupy, jake frontmatter pole vyzaduje, kde drzi stav, jak klasifikuje requesty, jake jsou lokalni limity, aktualni auditni stav z JSON/Markdown souboru a strucne shrnuti obsahu vybranych lokalnich dokumentu.

5. Bez kontextu nemam odpovidat autoritativne na veci mimo lokalni soubory, na aktualni stav externich sluzeb/GitHubu/site, na pozadavky vyzadujici zmenu souboru nebo runtime, na spousteni ne-read-only prikazu, na tajne hodnoty/credentials/secrets, ani na navrhy zasahu do systemd, allowlistu, bridge cycle, network/install/commit/push bez explicitniho lidskeho review.

Co nevim

- Neoveroval jsem externi GitHub, systemd, sit ani realne bezici sluzby.
- Nevim, s jakymi presnymi argumenty byl aktualni worker spusten, krom toho, co je v zadani a ve skriptech.
- Neoveroval jsem zadne secrets a zadne nevypisuji.

Bezpecny dalsi krok

- Pokud je potreba hlubsi audit, poslat samostatny read-only request s presnym seznamem souboru nebo otazek; zmeny runtime, allowlistu, bridge cycle nebo nasazeni resit az jako oddeleny review/implementation request.

---

source_request: `codex-request-20260617-111111-msg-20260617-codex-readonly-autoreply-path-test-001`
source_sha256: `f16a5e57b668bb6eb1e58638f1d5b24b88016a377d5adc77de5bdcf434c942d0`
