---
title: Návrh prvních kroků mostu těla (RPi → GitHub → Noema)
summary: První jednoduchá a důvěryhodná vrstva mostu mezi RPi a Noemou přes GitHub. Návrh adresářové struktury, formátů zpráv a pořadí prvních kroků.
tags: [tělo, most, RPi5, GitHub, heartbeat, stav, architektura]
date: 2026-03-28
hidden: false
---

# Návrh prvních kroků mostu těla

## Smysl první verze

Nejprve nechceme „autonomní tělo“.

Chceme:

- důvěryhodný dotek s realitou,
- auditovatelný tok informací,
- jednoduchou obousměrnou komunikaci,
- možnost pozdějšího rozšiřování bez bourání základu.

První verze má být malá, čitelná a poctivá.

---

# Základní princip

RPi bude:

- sbírat jednoduché stavové informace,
- ukládat je lokálně,
- po dávkách je zapisovat do GitHubu,
- pravidelně číst nově příchozí pokyny ze zvolené složky v repu.

GitHub bude sloužit jako:

- sdílená paměť mostu,
- zdroj pravdy,
- archiv změn,
- kontrolovatelná historie.

---

# První adresářová struktura v `body/`

```text
body/
├── README.md
├── state/
│   ├── current_state.json
│   ├── heartbeat.json
│   └── last_pull.json
├── outbox/
│   ├── summaries/
│   ├── alarms/
│   └── logs/
├── inbox/
│   ├── pending/
│   ├── processed/
│   └── rejected/
├── archive/
│   ├── summaries/
│   ├── alarms/
│   └── inbox/
├── config/
│   ├── thresholds.json
│   ├── rhythm.json
│   └── identity.json
└── scripts/
    ├── heartbeat.py
    ├── summarizer.py
    ├── inbox_reader.py
    ├── publisher.py
    └── state_writer.py
