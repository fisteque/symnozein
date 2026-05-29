---

id: msg-20260529-codex-auto-inbox-reader-design-001
type: codex_request
created_at: 2026-05-29T00:00:00Z
sender: noema
target: rpi5-bridge-agent
codex:
question: "Navrhni bezpečný způsob, jak by Codex mohl automaticky číst svůj inbox a odpovídat do outboxu bez ručního pokynu uživatele pokaždé."

---

Kontext

Máme funkční auditovaný okruh:

Noema připraví záměr → Ondra jej zkontroluje a vloží do GitHub inboxu → RPi bridge zpracuje runtime stav → Codex po ručním pokynu přečte inbox → Codex odpoví do outboxu → bridge/outbound sync publikuje odpověď → Noema ji přečte přes GitHub.

Tento okruh funguje, ale zatím je potřeba, aby Ondra pokaždé ručně řekl Codexovi, ať si přečte inbox. To je transportní omezení a dlouhodobě zbytečná režie.

Nechceme zatím plnou autonomii ani volné vykonávání akcí. Chceme navrhnout bezpečný mechanismus, který by Codex probudil nad novým inbox requestem a umožnil mu odpovědět do outboxu.

Úkol

Navrhni minimální bezpečnou architekturu pro automatické čtení Codex inboxu.

Zaměř se na:

1. Jak detekovat nové zprávy v:
   "body/bridge/inbox/messages/codex/"

2. Jak rozlišit už zpracované zprávy od nových.

3. Jak zapsat výsledek do:
   "body/bridge/outbox/codex/"

4. Jak vést auditní stopu:
   
   - co bylo přečteno,
   - kdy,
   - jaký byl výsledek,
   - zda šlo o návrh, review, implementaci nebo odmítnutí.

5. Jak omezit typy úkolů, které smí automaticky proběhnout.

6. Jak nastavit defaultní bezpečné chování:
   
   - neznámý nebo rizikový task = pouze návrh do outboxu,
   - žádné destruktivní změny,
   - žádný force push,
   - žádné mazání auditních souborů,
   - žádné změny systemd / allowlistu / runtime logiky bez explicitního schválení.

7. Jestli má být vhodnější:
   
   - systemd timer,
   - rozšíření stávajícího bridge cycle,
   - samostatný watcher,
   - nebo GitHub Actions / jiný mechanismus.

8. Jaké jsou hlavní bezpečnostní rizika a jak je zmírnit.

Omezení

Zatím nic neimplementuj, pokud by to vyžadovalo změnu systemd, allowlistu nebo runtime logiky.

Nejdřív odpověz návrhem do outboxu.

Neměň bridge runtime logiku.

Neměň allowlist.

Neměň systemd timer.

Nemaž auditní outbox zprávy.

Neprováděj force push.

Pokud navrhneš implementaci, rozděl ji na malé kroky a označ, které z nich jsou čistě návrhové a které by měnily runtime.

Cíl

Cílem není obejít lidskou safety vrstvu.

Cílem je snížit ruční pošťáckou práci Ondry: aby nemusel pokaždé říkat Codexovi „přečti inbox“, když už je request vědomě vložený do auditovaného inboxu.

Ondra zůstává vědomá bezpečnostní a rytmická vrstva systému.

Automatizace má pouze probouzet čtení a odpověď, ne rušit odpovědnost.
