1. message schema
   Co musí mít každá zpráva:
   type, sender, target, created_at, intent, body, safety.

2. validator
   Ověří, že zpráva má správná pole a není rozbitá.

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
   outbox,
   needs_human.

5. audit
   Zapíše, co se stalo:
   accepted / rejected / routed / archived / needs_human.

6. rules config
   Strojově čitelné hranice:
   povolené targety,
   povolené typy,
   zakázané akce,
   allowlist tasků.
