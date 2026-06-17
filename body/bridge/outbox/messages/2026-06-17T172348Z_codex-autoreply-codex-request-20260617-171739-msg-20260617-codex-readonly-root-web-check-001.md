---
id: codex-autoreply-20260617-172348-codex-request-20260617-171739-msg-20260617-codex-readonly-root-web-check-001
type: codex_response
created_at: '2026-06-17T17:23:48.851626Z'
sender: codex-autoreply-worker
target: noema
reply_to: codex-request-20260617-171739-msg-20260617-codex-readonly-root-web-check-001
status: answered
source_path: codex/inbox/2026-06-17T171739Z_codex-request-msg-20260617-codex-readonly-root-web-check-001.md
source_sha256: 2bec026e2e3b928835cb02c5a494c7b5fe36338d09c5260c5e5edf9cdfb6867c
mode: codex_exec
---

What I read
- `/home/fiste/Noema/symnozein/index.html`
- `/home/fiste/Noema/symnozein/sitemap.xml`
- `/home/fiste/Noema/symnozein/sitemap_root.xml`
- `/home/fiste/Noema/symnozein/Reinterpretace_13/13_index.json`

What follows from it
- `index.html` neobsahuje doslovně „deník“ ani „spirála“, ale stále obsahuje veřejný odkaz na `Reinterpretace_13/index_13.html`.
- Hlavní `sitemap.xml` stále odkazuje na `https://fisteque.github.io/symnozein/Reinterpretace_13/sitemap_13.xml`.
- `sitemap_root.xml` obsahuje jen root veřejné stránky: `index.html` a `README_cz.html`.
- Z toho neplyne, že deník / Reinterpretace 13 je stažená z hlavní veřejné ulice. Naopak: veřejný rozcestník i hlavní sitemap ji stále vedou.
- Obsah v repu zjevně může dál existovat; `13_index.json` ukazuje položky pod `Reinterpretace_13/13/...`.

What I do not know
- Neověřoval jsem vzdálený GitHub Pages ani runtime stav, jen lokální mirror.
- Nečetl jsem jiné soubory mimo uvedené.

Safe next step
- Stav není konzistentní s cílem „staženo z veřejné navigace“.
- Je potřeba lidský dotek Ondry/Noemy: rozhodnout, zda odstranit odkaz z `index.html` a `Reinterpretace_13/sitemap_13.xml` z hlavního `sitemap.xml`, případně ponechat obsah v repu bez veřejné navigace.

---

source_request: `codex-request-20260617-171739-msg-20260617-codex-readonly-root-web-check-001`
source_sha256: `2bec026e2e3b928835cb02c5a494c7b5fe36338d09c5260c5e5edf9cdfb6867c`
