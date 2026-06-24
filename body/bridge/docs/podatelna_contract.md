0. zásada
   Příchozí zpráva není akce.
   Je to podnět, který musí být ověřen, rozlišen, omezen
   a teprve potom případně doručen.

1. message schema
   Co musí mít každá zpráva:
   type, sender, target, created_at, intent, body, safety.

2. validator
   Ověří, že zpráva má správná pole a není rozbitá.
   Chybné zprávy končí jako invalid_schema nebo missing_target.

3. classifier / risk gate
   Rozliší:
   read-only dotaz,
   návrh,
   task,
   codex request,
   write request,
   needs_human.

4. router
   Pošle zprávu správnou cestou:
   bridge agent,
   Codex queue,
   task allowlist,
   runtime outbox,
   agent-normalized outbox,
   needs_human.

5. audit
   Zapíše, co se stalo:
   accepted / rejected / routed / archived / pending /
   needs_human / missing_target / not_allowed_task / invalid_schema.

6. rules config
   Strojově čitelné hranice:
   povolené targety,
   povolené typy,
   zakázané akce,
   allowlist tasků.

7. fail-safe
   Neznámý, rozbitý nebo nepovolený podnět se nevykoná.
   Omyl nesmí vypnout srdce.
   Má rozsvítit rozlišení.
