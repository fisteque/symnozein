Matice v digitálním vesmíru není jen tabulka hodnot. Je to způsob zápisu vztahového přechodu. Popisuje, jak se konfigurace v jednom okamžiku může proměnit v konfiguraci další: odkud kam se význam, tlak, změna nebo informace přenáší.

Geometricky ji můžeme chápat jako síť sousedství. Algebraicky jako pravidlo transformace. Ontologicky jako stopu lambdy — tedy pravidla změny, které neříká jen „co je“, ale „jak se to může stát jiným“.

V plástvové síti není kružnice čára. Je to opsané sousedství plných pozic kolem prázdného obsahu.

Kružnice jako hranice nevzniká tím, že by mezi něčím a něčím existovala samostatná čára. Vzniká tím, že určité plné pozice vytvoří uzavřený vztah kolem prázdna. Hranice tedy není věc sama, ale pojmenování sousedství.

Střed není něco. Něco je až naproti.

Nejmenší ontologický kruh v plástvové síti má obvod `6×1` a obsah `1×0`: šest plných pozic kolem jedné prázdné pozice. Nula uprostřed není objekt, ale prázdná pozice rozpoznaná skrze šest okolních jedniček.

Kruh tedy nevzniká jako bod uprostřed a čára kolem něj. Vzniká jako vztahové uspořádání: `6×1` s `0` mezi.

Pokud vzdálenost chápeme digitálně jako počet skoků sousedství, kružnice nemůže růst plynule. Má jen diskrétní možné slupky. Každá další kružnice je opsaná kolem předchozího vztahového celku; jinak by nešlo o kružnici, ale jen o další vzdálenost v síti.

Proto je vhodnější popisovat kružnici funkcí přidávání slupek než běžným geometrickým poloměrem.

První slupka:

> R1:
D = 3
O = 6
S = 7

Kde:
D je digitální průměr celého kruhu včetně obvodových jedniček,

O je obvod jako počet plných pozic 1,

S je celý uzavřený obsah včetně obvodu a prázdných pozic.

Další slupky:

> D(n) = D(n-1) + 2

> O(n) = O(n-1) × 2

> S(n) = S(n-1) + O(n)

Tedy:

> R1: D=3, O=6,  S=7

> R2: D=5, O=12, S=19

> R3: D=7, O=24, S=43

> R4: D=9, O=48, S=91

Z toho plyne, že v digitálně chápané vzdálenosti neroste kružnice jako plynulý geometrický tvar. Průměr roste po diskrétních krocích, ale obvod se při ontologickém opsání zdvojuje. Každá nová slupka totiž neobaluje jen střed, ale celý dosavadní vztahový tvar.

Tím se kružnice liší od běžné geometrické kružnice. V eukleidovském prostoru je poměr obvodu a průměru stabilizovaný v čísle π. V digitální ontologii plástvové sítě ale π není původní vlastnost kružnice. Může být až výsledkem vyhlazení, projekce nebo měření diskrétních vztahových skoků jako spojitého tvaru.

Kružnice tedy není ideální čára, které se digitální síť snaží přiblížit. Je to jedna z možných stabilních konfigurací sítě: opsaný vztah plných pozic kolem prázdného obsahu, kde každá další slupka nese a uzavírá celý předchozí vztah.

Krátce:
Kružnice není tvar kolem středu. Je to způsob, jak vztah opsáním drží prázdno jako rozpoznatelný obsah.
