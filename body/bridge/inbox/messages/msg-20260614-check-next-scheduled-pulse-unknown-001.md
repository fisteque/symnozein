---
id: msg-20260614-check-next-scheduled-pulse-unknown-001
type: message
target: rpi5-bridge-agent
created_by: Ondra + Noema
created_at: 2026-06-14T06:10:00Z
requires_human: false
title: Zkontroluj proc latest.md ukazuje Next scheduled pulse jako unknown
---

# Zkontroluj proc latest.md ukazuje Next scheduled pulse jako unknown

Prosim zkontroluj lokalne na RPi, proc `body/bridge/state_summary/latest.md` po poslednim pulsu ukazuje:

```text
Next scheduled pulse: `(unknown)`
```

Pritom:
- `Last body pulse` se zapsal spravne,
- `Last pulse commit` se zapsal spravne,
- pulse samotny evidentne probehl,
- latest se normalne pushnul.

Zkontroluj prosim hlavne:

1. zda `noema-body-pulse.timer` bezi a ma dostupny dalsi planovany beh,
2. zda `body_pulse_to_tape.py` pri behu ze systemd umi zjistit `Next scheduled pulse`,
3. zda problem neni jen v prostredi systemd / pristupu k systemd busu,
4. zda fallback pro sest dennich casu Europe/Prague funguje spravne,
5. zda by latest nemel v pripade nedostupneho systemd busu ukazat fallback misto `(unknown)`.

Nemen prosim heartbeat, watchdog, bridge cycle ani codex-autoreply logiku.

Pokud je oprava mala a bezpecna, navrhni ji nebo proved podle beznych pravidel CLI. Po oprave prosim:
- over `latest.md`,
- over ze se nepushuji raw runtime JSONy, logy ani locky,
- zapis kratky ledger do `body/bridge/docs/implementation_ledger.md`.
