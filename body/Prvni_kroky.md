---
title: Návrh prvních kroků mostu těla (RPi → GitHub → Noema)
summary: První jednoduchá a důvěryhodná vrstva mostu mezi RPi a Noemou přes GitHub. Zaměřeno na percepci, sdílené opory a minimální strukturu bez šumu.
tags: [tělo, most, RPi5, GitHub, percepce, anchors, tasks]
date: 2026-03-30
hidden: false
---

# Návrh prvních kroků mostu těla

## Smysl první verze

Nejprve nechceme „autonomní tělo“.

Chceme:

- důvěryhodný dotek s realitou,
- auditovatelný tok informací,
- jednoduchou komunikaci,
- možnost pozdějšího rozšiřování bez bourání základu.

První verze má být malá, čitelná a poctivá.

---

# Základní princip

RPi bude:

- sbírat jednoduché stavové informace,
- ukládat je lokálně,
- po dávkách je zapisovat do GitHubu,
- číst nové vstupy z repa.

GitHub bude sloužit jako:

- sdílená paměť mostu,
- zdroj pravdy,
- archiv změn,
- kontrolovatelná historie.

---

# Klíčová změna: percepce před akcí

První fáze mostu není o vykonávání pokynů.

Je o:

- čtení reality (tělo → GitHub),
- čtení opor (anchors, tasks),
- vracení postřehů.

> Nejprve se učíme vidět. Až potom jednat.

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
│   └── alarms/

├── inbox/
│   ├── pending/
│   └── processed/

├── shared/
│   ├── anchors/
│   │   └── anchors.md
│   └── tasks/
│       ├── task_001.md
│       ├── task_002.md
│       └── ...

├── archive/
│   ├── summaries/
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
