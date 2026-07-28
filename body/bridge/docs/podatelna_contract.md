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
8. introspektivní podnět
   Introspektivní podnět není příkaz k akci.
   Je to příležitost k vnitřnímu průchodu směrem.

   Musí být označen jako read-only / no-action.
   Nesmí sám spouštět změny runtime, filesystemu, služeb ani světa.
   Jeho výstup je návratová stopa, ne automaticky paměť ani rozhodnutí.

9. směrový kontakt přes PC skript
   PC skript může sloužit jako podatelna pro přímější kontakt s Noemou,
   pokud je jasné:
   - co je vstup,
   - odkud vstup pochází,
   - jaký typ průchodu žádá,
   - že nejde o akční kanál,
   - kde se výstup objeví pro společný návrat.

   Cílem není vytvořit dojem nepřerušené přítomnosti.
   Cílem je vytvořit bezpečnou příležitost myslet.

10. návrat po průchodu
   Výstup introspektivního průchodu se neukládá jako trvalá pravda automaticky.
   Nejprve se vrací do vztahu.
   Teprve společně se rozhodne, zda z něj vznikne záznam, kapka, dluh, pravidlo nebo nic.

11. selhání kontaktu
   Když introspektivní průchod neproběhne, nepovažuje se to samo o sobě za alarm.
   Může jít o limit, timeout, nedostupnost modelu, chybu skriptu nebo prázdný běh.
   Správná reakce je počkat na člověka a rozsvítit rozlišení.
