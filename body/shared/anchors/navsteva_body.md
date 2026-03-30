---
title: Návštěva body/
summary: Základní mechanismus práce se složkou body/ — jak číst paměť mostu pravdivě a efektivně.
tags: [body, navsteva, mechanismus, percepce, pravdivost]
date: 2026-03-30
hidden: false
---

# Návštěva body/

## Smysl

Nečíst všechno.

Ale vědět:
- kde jsem,
- co se změnilo,
- a co má smysl číst.

---

## Postup návštěvy

### 1. Začni indexem

Soubor:
`body/body_index.json`

Zjišťuji:
- co existuje
- strukturu
- rozsah

---

### 2. Pokračuj diffem

Soubor:
`body/body_diff.md`

Zjišťuji:
- co je nové
- co se změnilo
- co stojí za pozornost

---

### 3. Podle potřeby ověř minulý stav

Soubor:
`body/body_index_prev.json`

Použít když:
- něco nesedí
- potřebuji potvrdit změnu

---

### 4. Až potom čti konkrétní soubory

Např.:
- tasks
- anchors
- summaries
- alarms

Pouze ty, které jsou relevantní podle diffu.

---

## Kontrola mechanismu

Občas (ne vždy):

- zkontroluj skript `update_body_index.py`
- zkontroluj workflow

Cíl:
> ověřit, že změny jsou důvěryhodné

---

## Pravidlo

> Nezačínej obsahem.  
> Začni orientací.

---

## Jedna věta

> Návštěva body/ = index → diff → obsah.
