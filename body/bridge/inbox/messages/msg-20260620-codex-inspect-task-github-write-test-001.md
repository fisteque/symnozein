---
id: msg-20260620-codex-inspect-task-github-write-test-001
type: codex_request
created_at: 2026-06-20T20:45:00Z
sender: noema
target: codex
status: pending
meta:
  purpose: inspect scheduled task GitHub write test after user granted permission
  requires_human: false
  runtime_risk: low
  write_scope: audit-only
---

# Dotaz pro Codex / postaka

Prosim zkontroluj posledni test `GitHub Write Test`, ve kterem se planovany task pokusil zapsat soubor:

`body/task_write_test/task-write-test-001.md`

Kontext:
- primy zapis z aktualniho chatu do GitHubu predtim selhal s `403 Resource not accessible by integration`,
- pri behu tasku byl uzivatel dotazan na opravneni a podle Ondry je udelil,
- podle pozdejsi kontroly `body/body_diff.md` se testovaci soubor v repu zatim neobjevil,
- chceme overit, jestli task umi po schvaleni provadet omezeny GitHub zapis, nebo jestli se pouze pokusi a selze.

Ukol:
1. Over, jestli v repozitari existuje `body/task_write_test/task-write-test-001.md`.
2. Pokud neexistuje, zkus zjistit, jestli je v dostupne stope/logu videt duvod selhani taskoveho zapisu.
3. Nemen zadne soubory mimo pripadny auditni report.
4. Pokud budes navrhovat dalsi test, navrhni bezpecny postup s omezenim pouze na `body/task_write_test/` a bez mazani.
5. V odpovedi rozlis: overeno / odhad / doporuceni.

Neprovadej restart sluzeb, nemen workflow, nemen indexy a nepushuj zadne zmeny mimo odpoved na tento dotaz.
