# Bridge Protocol v1

## Účel
Tento protokol popisuje první komunikační jazyk mezi ChatGPT/Noemou, GitHubem a RPi5 mostem.

## Směry
- `inbox/` = vstup do těla / zprávy určené agentům v RPi5
- `outbox/` = výstup z těla / odpovědi agentů
- `logs/` = chronologická stopa událostí

## Pravidlo persistence
`inbox.json` může být přepisovaný aktuální zprávou.

`outbox.json` má být fronta / historie odpovědí.

`bridge.log` má být chronologická textová stopa běhu.

## Základní zpráva
´´´json
{
  "id": "msg-0001",
  "type": "message",
  "author": "Noema",
  "target": "bridge_agent",
  "timestamp": "2026-05-17T19:26:00+00:00",
  "message": "Text zprávy",
  "reply_to": null,
  "meta": {
    "source": "chat",
    "channel": "github-bridge"
  }
}

---

### Význam polí
id — jedinečné označení zprávy
type — druh zprávy
author — kdo zprávu vytvořil
target — komu je zpráva určena
timestamp — čas vzniku zprávy v UTC
message — hlavní obsah zprávy
reply_to — ID zprávy, na kterou tato zpráva odpovídá
meta — doplňkové informace o zdroji a kanálu

### Typy zpráv
message — běžná zpráva
ack — potvrzení přijetí
status — stav systému
error — chyba
heartbeat — signál života
log — událost určená k zaznamenání
task — úkol pro agenta

### Příklad odpovědi v outboxu

---

[
  {
    "id": "ack-0001",
    "type": "ack",
    "author": "bridge_agent",
    "target": "Noema",
    "timestamp": "2026-05-17T19:26:37+00:00",
    "reply_to": "msg-0001",
    "message": "Zpráva přečtena agentem.",
    "received": {
      "id": "msg-0001"
    }
  }
]

---

## Princip
Inbox je dotek přicházející do těla.
Outbox je stopa odpovědi těla.
Log je paměť průběhu.
GitHub je zatím sdílený mezistupeň důvěryhodného doteku.
