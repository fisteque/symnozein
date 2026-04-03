---
title: Struktura body
date: 2026-04-03
tags: body, struktura, mapa, orientace
summary: Přehled složky body a význam jednotlivých částí pro orientaci a práci.
---

# Struktura body

`body/` je stavová vrstva systému.  
Nejde jen o soubory, ale o prostor, kde se odehrává práce, orientace a návrat ke směru.

---

## Základní soubory

### `body_index.json`
Aktuální stav všech souborů v body.

→ co existuje

---

### `body_diff.md`
Poslední změny.

→ co se pohnulo

---

### `index_menu.json`
Rozcestník na další indexy v repu.

→ kam lze sahat

---

### `navsteva_body.md`
Způsob, jak se v body pohybovat.

→ jak se dívat

---

## Složky

### `SK/`
Stabilní body vývoje.

→ opory pro návrat ke směru  
→ referenční stavy  
→ checkpointy

---

### `shared/anchors/`
Operativní kotvy.

→ jak postupovat  
→ jak se orientovat v aktuální práci  
→ lokální navigace

---

### `shared/tasks/`
Aktuální úkoly.

→ co dělat  
→ rozpracované kroky  
→ operativní práce

---

## Shrnutí

- **index** → stav  
- **diff** → pohyb  
- **menu** → mapa ven  
- **anchors** → navigace  
- **SK** → směr  
- **tasks** → akce  

---

> Body není úložiště.  
> Je to prostor, kde se něco děje.
