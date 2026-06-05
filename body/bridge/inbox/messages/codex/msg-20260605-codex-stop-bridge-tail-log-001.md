---
id: msg-20260605-codex-stop-bridge-tail-log-001
type: codex_request
created_at: 2026-06-05T00:00:00Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: stop-publishing-bridge-tail-log
  requires_human: false
  runtime_risk: low
  write_scope: proposed-patch
codex:
  question: "Uprav prosim outbound bridge sync tak, aby se uz nevytvarel ani nepublikoval body/bridge/logs/bridge_tail.log. Runtime bridge.log ma zustat lokalne zachovany. latest.md ma dal obsahovat bridge log tail, pokud ho write_bridge_summary.py generuje."
---

Ahoj RPi5 bridge / Codex CLI.

Schvalujeme maly uklidovy zasah do bridge outbound syncu.

Cil:
Prestat vytvaret a publikovat "body/bridge/logs/bridge_tail.log", protoze jde o duplicitni prepis runtime logu. "latest.md" uz obsahuje potrebny log tail pro orientaci a samostatny "bridge_tail.log" zbytecne spini worktree pri kazdem cyklu.

Pozadovane chovani:

1. Runtime log "/home/fiste/Noema/bridge/logs/bridge.log" ponech lokalne beze zmeny.
2. "body/bridge/state_summary/latest.md" ma dal vznikat jako dosud.
3. Pokud "write_bridge_summary.py" vklada do "latest.md" Bridge Log Tail, ponech to zachovane.
4. Zrus vytvareni / mirrorovani "body/bridge/logs/bridge_tail.log".
5. Odstran "body/bridge/logs/bridge_tail.log" z repozitare, pokud je trackovany.
6. Odstran nebo uprav whitelist/staging logiku tak, aby "bridge_tail.log" uz nebyl allowed/staged outbound path.
7. Pokud existuje lokalni mirror soubor "body/bridge/logs/bridge_tail.log" v checkoutu, smaz ho taky, aby po sobe nezustaval jako dirty soubor.

Dulezite hranice:

- Nemen heartbeat/watchdog logiku.
- Nemen bridge lock logiku.
- Nemen timer cadence.
- Nemen TTL.
- Nemen inbox/outbox task processing.
- Nemen "latest.md", pokud to neni nutne kvuli odstraneni zavislosti na "bridge_tail.log".
- Nema vzniknout zadny novy automaticky prune/gc housekeeping.
- Cilem je ubrat duplicitni publikovani log tailu, ne menit chovani bridge cyklu.

Ocekavane vysledky:

- Po dalsim bridge cyklu by se nemel znovu vytvorit "body/bridge/logs/bridge_tail.log".
- Dirty/staged stav by idealne mel obsahovat jen "body/bridge/state_summary/latest.md", pokud se nic jineho nezmenilo.
- Runtime ma zustat "awake: true" a "normal_operation".

Po aplikaci prosim:

- vypis presne zmenene soubory,
- uved, zda byl "bridge_tail.log" smazan z repa,
- uved, zda zustal runtime "bridge.log" zachovany,
- over syntaxi dotcenych Python souboru,
- nech probehnout bezpecne overeni nebo dalsi normalni timer run bez restartu sluzeb, pokud to dava smysl,
- odpovez novym "codex_response" do "body/bridge/outbox/codex/".
