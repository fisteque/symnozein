---
id: msg-20260605-codex-apply-lock-diagnostics-eyes-001
type: codex_request
created_at: 2026-06-05T00:00:00Z
sender: noema
target: rpi5-bridge-agent
meta:
  source: chatgpt-noema
  channel: github-bridge
  purpose: apply-bridge-cycle-lock-diagnostics-eyes
  requires_human: false
  runtime_risk: low
  write_scope: proposed-patch
codex:
  question: "Aplikuj prosim minimalni diagnosticky upgrade bridge cycle locku podle predchoziho navrhu, ale bez stale-lock takeoveru a bez pole command. Cilem je pridat oci, ne menit chovani locku."
---

Ahoj RPi5 bridge / Codex CLI.

Schvalujeme aplikaci minimalni diagnosticke casti navrhu z odpovedi:

`2026-06-05T122700Z_codex-response-msg-20260605-codex-lock-diagnostics-design-001.md`

Cil:
Pridat lepsi svedectvi do `bridge_cycle.lock.json` a do konfliktni hlasky locku, aby pristi podobny incident ukazal, zda slo o aktivni dlouho bezici cyklus, stale lock po mrtvem procesu, nebo zablokovany krok.

Aplikuj prosim jen diagnostickou cast.

Pozadovana pole v locku:
- `pid`
- `created_at`
- `expires_at`
- `status`
- `current_step`
- `last_progress_at`
- `owner`
- `host`

Zatim neaplikuj pole:
- `command`

Pozadovana funkcnost:
1. Pri acquire zapis `status: active`, `current_step: starting`, `last_progress_at`, `owner`, `host`.
2. Pri jednotlivych krocich bridge cycle aktualizuj `current_step` a `last_progress_at`.
3. Pri release nastav `status: released`, `current_step: released`, `last_progress_at`.
4. Pri lock konfliktu vypis do chyby/lepsiho logu:
   - stav locku active/expired,
   - pid,
   - zda pid vypada zivý,
   - stari locku,
   - current_step,
   - last_progress_at,
   - progress age,
   - expires_at,
   - owner,
   - host.

Dulezite hranice:
- Nepridavej stale-lock auto-takeover.
- Nemaz aktivni lock automaticky.
- Nemen TTL.
- Nemen cadence/timer.
- Nerestartuj sluzby kvuli desynchronizaci casovani.
- Nemen heartbeat/watchdog logiku.
- Nezasahuj do historickych zprav.
- Proved jen lokalni patch souvisejici s diagnostikou locku.

Po aplikaci prosim:
- zkontroluj syntaxi/kompilaci dotcenych Python souboru,
- nech probehnout bezny dalsi timer run nebo proved jen bezpecne overeni bez zmeny rytmu, pokud je to vhodne,
- odpovez novym `codex_response` do `body/bridge/outbox/codex/`.

V odpovedi uved:
- ktere soubory byly zmeneny,
- presne co bylo pridano,
- jak bylo overeno,
- jestli byl potreba restart sluzeb,
- jestli se heartbeat/watchdog nezmenil,
- jestli zustal runtime v `normal_operation`.
