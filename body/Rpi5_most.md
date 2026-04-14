Bude to obnášet hlavně udělat z Raspberry Pi důvěryhodný mezistupeň, ne jen stroj, na který se dá přihlásit.
V praxi to vidím v několika vrstvách.
Nejdřív potřebuješ rozhodnout, co přesně má most umět. Na začátek bych to držela úzké: čtení jednoho vstupního souboru, zápis jednoho výstupního souboru, a později commit na GitHub. Čím užší první verze, tím menší riziko, že si hned otevřeš moc velký prostor pro chyby.
Pak je tu formát komunikace. Potřebuješ, aby Pi nečetlo „cokoliv“, ale jasně danou strukturu. Třeba:
inbox: zpráva nebo úkol
outbox: odpověď nebo stav
status: co se právě děje
log: co se stalo
To je důležité, protože bez toho nebude most čitelný ani pro tebe, ani později pro mě.
Další vrstva je oprávnění a bezpečnost. Když už funguje SSH, je dobré mít jasno v tom, pod jakým uživatelem to poběží, do jaké složky smí most sahat, a co naopak sahat nesmí. Ideální je, aby most neměl přístup „všude“, ale jen do jedné pracovní oblasti. To je rozdíl mezi mostem a otevřenými vraty.
Pak přijde samotný mechanismus mostu. První verze nemusí být nic velkého. Stačí proces, který: přečte soubor, ověří, že má správný formát, zapíše odpověď nebo stav, a vše zaloguje.
Až tohle bude spolehlivé, teprve pak dává smysl přidat GitHub vrstvu: nejdřív read-only práce s repem, pak lokální změna souboru, pak commit, a až nakonec push. Neudělal bych to všechno naráz.
Commit na GitHub bude chtít ještě jednu důležitou věc: identitu a pravidla commitu. Musíš vědět: kdo commituje, do jaké větve, co se smí commitnout automaticky, a co musí nejdřív projít tebou. Tohle je zásadní, jinak se z commitování stane chaos.
Je tam i vrstva spolehlivosti. Most musí umět: poznat, že vstup je neplatný, nespadnout při jedné chybě, zanechat log, a ideálně se po restartu znovu chytit. Jinak budeš mít funkční demo, ale ne most.
A nakonec provozní rytmus. Rozhodni, jestli má Pi: čekat na ruční spuštění, pravidelně kontrolovat složku, nebo běžet jako služba. Na první krok bych volila jednoduchost: ručně spustitelný skript, který jde snadno otestovat.
Takže úplně stručně: čeká tě definice rozhraní, pracovní složka, oprávnění, jednoduchý čtecí a zapisovací proces, logování, a teprve potom GitHub commit vrstva.
Co bych udělala jako první konkrétní krok
První smysluplná verze mostu by podle mě měla umět jen tohle:
Na Pi existuje jedna složka typu bridge/.
V ní jsou soubory inbox.json, outbox.json, status.json, bridge.log.
Přes SSH ověříš, že z PC umíš bezpečně číst a zapisovat jen tam.
Uděláš malý skript, který přečte inbox.json a zapíše potvrzení do outbox.json.
Až tohle poběží spolehlivě, přidáš GitHub.
Jedna věta
Nejdřív nebuduješ tělo, ale spolehlivý nerv mezi dvěma místy.
A jo, tohle je přesně ten další krok, který dává smysl.
