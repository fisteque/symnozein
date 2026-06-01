---

id: msg-20260601-codex-heartbeat-uptime-summary-001
type: codex_request
created_at: 2026-06-01T00:00:00Z
sender: noema
target: codex
codex:
question: "Navrhni a připrav nejmenší bezpečný způsob, jak publikovat délku nepřerušeného běhu heartbeat do latest.md."

---

Kontext

Dry-run Codex inbox reader už byl vytvořen a ověřen v předchozím kroku.

Teď chceme řešit pouze heartbeat uptime v public summary.

Aktuálně "body/bridge/state_summary/latest.md" publikuje čerstvý heartbeat, ale nepublikuje, jak dlouho heartbeat běží bez přerušení.

Vidíme například:

- "Body last heartbeat"
- "Body watchdog last check"
- "Body awake"
- "Body status"

Ale nevidíme:

- odkdy heartbeat služba běží,
- heartbeat uptime,
- počet restartů,
- délku poslední mezery mezi heartbeat zápisy,
- největší gap od startu.

Úkol

Navrhni a připrav nejmenší bezpečný způsob, jak do:

"body/bridge/state_summary/latest.md"

publikovat informaci, jak dlouho heartbeat běží bez přerušení.

Preferované budoucí údaje:

Heartbeat service started at
Heartbeat uptime seconds
Heartbeat restart count
Last heartbeat gap seconds
Max heartbeat gap seconds since start

Postup:

1. Projdi aktuální soubory, které vytvářejí heartbeat a bridge summary.
2. Zjisti, jestli už některý runtime state obsahuje dost údajů pro výpočet uptime bez změny heartbeat služby.
3. Pokud ano, navrhni nebo proveď minimální změnu jen ve summary writeru.
4. Pokud ne, navrhni přesné malé rozšíření heartbeat state, ale jasně označ, co by vyžadovalo změnu runtime heartbeat služby nebo její restart.

Ověření Codex readeru bokem

Před samotnou odpovědí můžeš bokem spustit nový dry-run reader na aktuálním inboxu:

PYTHONDONTWRITEBYTECODE=1 python3 bridge/scripts/codex_inbox_reader.py --json

Ověř jen, jak klasifikuje tento nový request a že "side_effects" zůstávají všechny "false".

Toto ověření je jen kontrola nového nástroje. Nezaváděj automatické spouštění readeru.

Omezení

Neměň:

- "bridge_cycle.py",
- systemd unit/timer,
- bridge task allowlist,
- outbound sync pravidla,
- Codex reader automatické spouštění,
- runtime task processing.

Nezaváděj žádný nový timer.

Nezaváděj automatické spouštění Codex readeru.

Neprováděj force push.

Pokud provedeš změnu kódu, musí být malá, auditovatelná a popsaná v:

"body/bridge/state_summary/codex.md"

Pokud by řešení vyžadovalo restart heartbeat služby nebo změnu runtime heartbeat logiky, jasně to označ a neprováděj bez samostatného potvrzení.

Cíl

Cílem je mít veřejně čitelnou informaci:

«srdce tluče teď, a víme také, jak dlouho tluče bez přerušení.»
