# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 7
Mean question score: 0.917
Mean provision score: 0.929
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Na internete som sa dočítal, že ak kataster nezapíše vlastnícke právo v lehote 30 dní, mám možnosť žiadať o vrátenie správneho poplatku. Je to pravda? Ako mám postupovať, aby mi správny poplatok bol vrátený a na koho sa mám v tejto veci obrátiť?

**Model-Selected Provisions:**
- 145/1995/paragraf-10
- 162/1995/paragraf-32

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
145/1995/paragraf-10

**Text written by the model for this provision:**

```text
Správny orgán rozhodne o vrátení správneho poplatku v plnej výške, ak sa úkon alebo konanie nevykonalo v zákonom stanovenej lehote bez zavinenia poplatníka. Lehota sa považuje za zachovanú, ak správny orgán v jej posledný deň odovzdá vybavenie na poštovú prepravu, odošle ho elektronicky alebo ho odovzdá priamo poplatníkovi.
```

**Text of legal provision:**

```text
LAW: 145/1995
VERSION: 20250101
PARAGRAPH: 10
TITLE: Vrátenie poplatku
TEXT:
Správny orgán rozhodne o vrátení poplatku v plnej výške, ak sa nemohol vykonať úkon alebo uskutočniť konanie bez zavinenia poplatníka v lehote ustanovenej podľa osobitného predpisu alebo na základe žiadosti poplatníka, ak bol poplatok zaplatený bez toho, aby bol na to poplatník povinný, ak pri jednotlivých položkách v sadzobníku nie je ustanovené inak. Na účely tohto zákona sa lehota ustanovená osobitným predpisom považuje za zachovanú, ak v posledný deň lehoty správny orgán
a) odovzdá spoplatnené vybavenie na poštovú prepravu,
b) odošle spoplatnené vybavenie elektronicky podľa osobitného predpisu 7ab) alebo
c) odovzdá poplatníkovi spoplatnené vybavenie.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza jednu z podmienok na vrátenie poplatku (nevykonanie úkonu v lehote bez zavinenia poplatníka) a presne parafrázuje, kedy sa lehota považuje za zachovanú zo strany správneho orgánu. Všetky uvedené informácie sú plne podložené textom právneho predpisu. Model síce nespomína ďalšie dôvody na vrátenie poplatku, ktoré predpis obsahuje, ale netvrdí, že jeho výpočet je vyčerpávajúci. Informácie, ktoré poskytuje, sú vecne správne, preto je skóre 1.0.

### Model-Selected Provision 2

**Provision:**
162/1995/paragraf-32

**Text written by the model for this provision:**

```text
Okresný úrad má na rozhodnutie o návrhu na vklad do katastra nehnuteľností lehotu 30 dní odo dňa doručenia návrhu. V osobitných prípadoch, ako napríklad pri zmluve vo forme notárskej zápisnice alebo pri žiadosti o urýchlené konanie, sú lehoty kratšie.
```

**Text of legal provision:**

```text
LAW: 162/1995
VERSION: 20240627
PARAGRAPH: 32
TEXT:
(1) Okresný úrad rozhodne o návrhu na vklad do 30 dní odo dňa doručenia návrhu na vklad. Ak ide o strategickú investíciu, rozhodne okresný úrad o návrhu na vklad do 15 dní odo dňa doručenia návrhu na vklad.
(2) Ak zmluva o prevode nehnuteľnosti bola vyhotovená vo forme notárskej zápisnice alebo bola autorizovaná advokátom, nie je v rozpore s katastrálnym operátom a sú splnené procesné podmienky na povolenie vkladu, okresný úrad rozhodne o návrhu na povolenie vkladu do 20 dní.
(3) Okresný úrad môže rozhodnúť na základe žiadosti o urýchlené konanie o návrhu na vklad a zaplatení správneho poplatku 10e) do 15 dní odo dňa doručenia návrhu na vklad. Ak v tejto lehote nerozhodne, rozhodne v lehote podľa odseku 1.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu presne uvádza štandardnú 30-dňovú lehotu na rozhodnutie o návrhu na vklad. Taktiež správne identifikuje, že v osobitných prípadoch sú lehoty kratšie, a ako príklady uvádza zmluvu vo forme notárskej zápisnice (lehota 20 dní podľa ods. 2) a žiadosť o urýchlené konanie (lehota 15 dní podľa ods. 3). Všetky tvrdenia v texte modelu sú plne podporené textom právneho predpisu. Preto je skóre 1.0.

---

## ID 1 | Status: OK

**Question:** Môj partner ma psychicky ponižuje, vyhráža sa mi a kontroluje mi telefón. Je to už týranie, aj keď ma neudrel?

**Model-Selected Provisions:**
- 300/2005/paragraf-127
- 300/2005/paragraf-208

**Question score:** 0.750

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-127

**Text written by the model for this provision:**

```text
Pre účely trestného činu týrania sa za blízku osobu považuje okrem iných aj druh, bývalý druh alebo osoba, ktorá s páchateľom žije alebo žila v spoločnej domácnosti.
```

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20250801
PARAGRAPH: 127
TEXT:
Blízkou osobou sa na účely trestných činov vydierania podľa § 189 , znásilnenia podľa § 199 ods. 2 , sexuálneho násilia podľa § 200 ods. 2 , sexuálneho zneužívania podľa § 201 ods. 2 , týrania blízkej osoby a zverenej osoby podľa § 208 , nebezpečného vyhrážania podľa § 360 ods. 2 , nebezpečného prenasledovania podľa § 360a , nebezpečného elektronického obťažovania podľa § 360b alebo financovania terorizmu podľa § 419c ods. 2 rozumie aj bývalý manžel, druh, bývalý druh, rodič spoločného dieťaťa a osoba, ktorá je vo vzťahu k nim blízkou osobou podľa odseku 4, ako aj osoba, ktorá s páchateľom žije alebo žila v spoločnej domácnosti.
---
LAW: 300/2005
VERSION: 20250801
PARAGRAPH: 127
TEXT:
Blízkou osobou sa na účely tohto zákona rozumie príbuzný v priamom pokolení, osvojiteľ, osvojenec, súrodenec a manžel; iné osoby v rodinnom alebo obdobnom pomere sa pokladajú za navzájom blízke osoby len vtedy, ak by ujmu, ktorú utrpela jedna z nich, druhá právom pociťovala ako ujmu vlastnú.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne a presne definuje, kto sa považuje za blízku osobu pre účely trestného činu týrania. Vymenované osoby (druh, bývalý druh, osoba žijúca v spoločnej domácnosti) sú explicitne uvedené v texte právneho predpisu. Formulácia "okrem iných" je tiež správna, keďže zákon vymenúva aj ďalšie osoby. Informácie sú plne podporené zákonom.

### Model-Selected Provision 2

**Provision:**
300/2005/paragraf-208

**Text written by the model for this provision:**

```text
Trestného činu týrania blízkej osoby sa dopustí ten, kto jej spôsobí fyzické alebo psychické utrpenie. Zákon ako príklady foriem psychického utrpenia uvádza ponižovanie, pohŕdavé zaobchádzanie, neustále sledovanie, vyhrážanie, vyvolávanie strachu alebo stresu, či iné správanie, ktoré ohrozuje psychické zdravie.
```

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20250801
PARAGRAPH: 208
TITLE: Týranie blízkej osoby a zverenej osoby
TEXT:
(1) Kto blízkej osobe alebo osobe, ktorá je v jeho starostlivosti alebo výchove, spôsobí fyzické utrpenie alebo psychické utrpenie
a) bitím, kopaním, údermi, spôsobením rán a popálenín rôzneho druhu, ponižovaním, pohŕdavým zaobchádzaním, neustálym sledovaním, vyhrážaním, vyvolávaním strachu alebo stresu, násilnou izoláciou, citovým vydieraním alebo iným správaním, ktoré ohrozuje jej fyzické alebo psychické zdravie alebo obmedzuje jej bezpečnosť,
b) bezdôvodným odopieraním stravy, oddychu alebo spánku alebo odopieraním nevyhnutnej osobnej starostlivosti, ošatenia, hygieny, zdravotnej starostlivosti, bývania, výchovy alebo vzdelávania,
c) nútením k žobrote alebo k opakovanému vykonávaniu činnosti vyžadujúcej jej neúmernú fyzickú záťaž alebo psychickú záťaž vzhľadom na jej vek alebo zdravotný stav alebo spôsobilej poškodiť jej zdravie,
d) vystavovaním vplyvu látok spôsobilých poškodiť jej zdravie, alebo
e) neodôvodneným obmedzovaním v prístupe k majetku, ktorý má právo užívať,
(2) Rovnako ako v odseku 1 sa potrestá, kto spácha obdobný čin ako je čin uvedený v odseku 1, hoci bol za obdobný čin v predchádzajúcich dvanástich mesiacoch postihnutý.
(3) Odňatím slobody na sedem rokov až pätnásť rokov sa páchateľ potrestá, ak spácha čin uvedený v odseku 1
a) a spôsobí ním ťažkú ujmu na zdraví alebo smrť,
b) z osobitného motívu,
c) hoci bol v predchádzajúcich dvadsiatich štyroch mesiacoch za taký čin odsúdený alebo z výkonu trestu odňatia slobody uloženého za taký čin prepustený, alebo
d) závažnejším spôsobom konania.
(4) Odňatím slobody na pätnásť rokov až dvadsaťpäť rokov alebo trestom odňatia slobody na doživotie sa páchateľ potrestá, ak spácha čin uvedený v odseku 1 a spôsobí ním ťažkú ujmu na zdraví viacerým osobám alebo smrť viacerých osôb.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Model správne uvádza, že trestného činu týrania sa dopustí ten, kto blízkej osobe spôsobí fyzické alebo psychické utrpenie. Taktiež správne vymenúva príklady konania ako ponižovanie, vyhrážanie či vyvolávanie strachu. Text je však nepresný v tom, že tieto konania prezentuje ako "príklady foriem psychického utrpenia", zatiaľ čo zákon ich uvádza ako príklady konania, ktorým sa spôsobuje fyzické alebo psychické utrpenie (zákon v tom istom bode uvádza aj bitie a kopanie). Model teda správne cituje časť zákona, ale nesprávne ju kategorizuje, čo je čiastočná nepresnosť.

---

## ID 2 | Status: OK

**Question:** Dobrý deň. Bol som bol prichytený pri šoférovaní pod vplyvom alkoholu, ale bez nehody. Čo mi za tento čin hrozí?

**Model-Selected Provisions:**
- 300/2005/paragraf-289
- 300/2005/paragraf-51
- 372/1990/paragraf-22

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-289

**Text written by the model for this provision:**

```text
Vykonávanie činnosti, pri ktorej by mohol byť ohrozený život alebo zdravie ľudí, v stave vylučujúcom spôsobilosť privodenom návykovou látkou, je trestným činom. Páchateľovi takéhoto činu hrozí trest odňatia slobody až na jeden rok.
```

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20250217
PARAGRAPH: 289
TITLE: Ohrozenie pod vplyvom návykovej látky
TEXT:
(1) Kto vykonáva v stave vylučujúcom spôsobilosť, ktorý si privodil vplyvom návykovej látky, zamestnanie alebo inú činnosť, pri ktorých by mohol ohroziť život alebo zdravie ľudí alebo spôsobiť značnú škodu na majetku, potrestá sa odňatím slobody až na jeden rok.
(2) Rovnako ako v odseku 1 sa potrestá, kto sa pri výkone zamestnania alebo inej činnosti uvedenej v odseku 1 odmietne podrobiť vyšetreniu na zistenie návykovej látky, ktoré sa vykonáva dychovou skúškou alebo orientačným testovacím prístrojom, alebo sa odmietne podrobiť lekárskemu vyšetreniu odberom a vyšetrením krvi alebo iného biologického materiálu, či nie je ovplyvnený návykovou látkou, hoci by to pri vyšetrení nebolo spojené s nebezpečenstvom pre jeho zdravie.
(3) Kto vykonáva v stave vylučujúcom spôsobilosť, ktorý si privodil vplyvom návykovej látky, zamestnanie alebo inú činnosť, pri ktorých by mohol ohroziť život alebo zdravie ľudí alebo spôsobiť značnú škodu na majetku,
a) hoci bol za taký čin alebo za čin uvedený v odseku 2 v predchádzajúcich dvadsiatich štyroch mesiacoch odsúdený alebo z výkonu trestu odňatia slobody uloženého za taký čin alebo za čin uvedený v odseku 2 prepustený,
b) hoci bol za obdobný čin spáchaný pod vplyvom návykovej látky alebo za čin uvedený v odseku 2 v predchádzajúcich dvadsiatich štyroch mesiacoch postihnutý, alebo
c) spôsobil čo aj z nedbanlivosti inému ublíženie na zdraví alebo väčšiu škodu na cudzom majetku,
(4) Odňatím slobody na dva roky až päť rokov sa páchateľ potrestá, ak vykonáva v stave vylučujúcom spôsobilosť, ktorý si privodil vplyvom návykovej látky, konanie, pri ktorom by mohol ohroziť život alebo zdravie ľudí alebo spôsobiť značnú škodu na majetku pri výkone zamestnania alebo inej činnosti, pri ktorých je vplyv návykovej látky obzvlášť nebezpečný, najmä ak vedie prostriedok hromadnej prepravy.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne popisuje základnú skutkovú podstatu trestného činu ohrozenia pod vplyvom návykovej látky podľa odseku 1. Uvádza, že ide o vykonávanie činnosti v stave vylučujúcom spôsobilosť, pri ktorej môže dôjsť k ohrozeniu života alebo zdravia. Taktiež správne uvádza trestnú sadzbu odňatia slobody až na jeden rok, ktorá zodpovedá základnej skutkovej podstate. Informácie sú plne podložené v právnom predpise.

### Model-Selected Provision 2

**Provision:**
300/2005/paragraf-51

**Text written by the model for this provision:**

```text
Súd môže v rámci trestného konania uložiť páchateľovi aj rôzne povinnosti. Medzi takéto povinnosti patrí napríklad príkaz podrobiť sa liečeniu závislosti od návykových látok.
```

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20241230
PARAGRAPH: 51
TEXT:
Obmedzenia spočívajú najmä v zákaze
a) účasti na určených verejných podujatiach,
b) požívania alkoholických nápojov a iných návykových látok,
c) stretávania sa s osobami, ktoré majú na páchateľa negatívny vplyv alebo ktoré boli jeho spolupáchateľmi alebo účastníkmi na trestnom čine,
d) vstupu na vyhradené miesta alebo priestory, na ktorých trestný čin spáchal,
e) účasti na hazardných hrách, hrania na hracích automatoch a uzatvárania stávok,
f) kontaktu s určenou osobou v akejkoľvek forme vrátane kontaktovania prostredníctvom elektronickej komunikačnej služby alebo inými obdobnými prostriedkami.
---
LAW: 300/2005
VERSION: 20241230
PARAGRAPH: 51
TEXT:
Povinnosti spočívajú najmä v príkaze
a) nepriblížiť sa k určenej osobe na vzdialenosť menšiu ako päť metrov a nezdržiavať sa v blízkosti obydlia určenej osoby alebo v určenom mieste, kde sa takáto osoba zdržuje alebo ktoré navštevuje,
b) zdržiavať sa v určenom čase na určenej adrese,
c) vysťahovať sa z bytu alebo domu, v ktorom sa neoprávnene zdržuje alebo ktorý protiprávne obsadil,
d) nahradiť v skúšobnej dobe spôsobenú škodu,
e) zaplatiť v skúšobnej dobe dlh alebo zameškané výživné,
f) osobne alebo verejne sa ospravedlniť poškodenému,
g) v skúšobnej dobe získať určitú pracovnú kvalifikáciu alebo zúčastniť sa na rekvalifikačnom kurze,
h) podrobiť sa v súčinnosti s probačným a mediačným úradníkom alebo iným odborníkom programu sociálneho výcviku alebo inému výchovnému programu,
i) podrobiť sa liečeniu závislosti od návykových látok, ak mu nebolo uložené ochranné liečenie,
j) podrobiť sa v skúšobnej dobe psychoterapii alebo zúčastniť sa na psychologickom poradenstve,
k) zamestnať sa v skúšobnej dobe alebo uchádzať sa preukázateľne o zamestnanie,
l) dostaviť sa v určenom čase na príslušný útvar Policajného zboru určený podľa miesta pobytu, v odôvodnených prípadoch aj opakovane.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne konštatuje, že súd môže páchateľovi uložiť rôzne povinnosti. Uvedený príklad, príkaz podrobiť sa liečeniu závislosti od návykových látok, je priamo uvedený v texte právneho predpisu v časti o povinnostiach pod písmenom i). Tvrdenie je teda vecne správne a plne podporené predpisom.

### Model-Selected Provision 3

**Provision:**
372/1990/paragraf-22

**Text written by the model for this provision:**

```text
Vedenie vozidla v čase po požití alkoholu, keď sa ešte nachádza v organizme, je priestupkom proti bezpečnosti a plynulosti cestnej premávky. Za tento priestupok možno uložiť pokutu od 150 eur do 800 eur a zákaz činnosti do troch rokov.
```

**Text of legal provision:**

```text
LAW: 372/1990
VERSION: 20250201
PARAGRAPH: 22
TITLE: Priestupky proti bezpečnosti a plynulosti cestnej premávky
TEXT:
(1) Priestupku proti bezpečnosti a plynulosti cestnej premávky sa dopustí ten, kto
a) ako vodič vozidla sa odmietne podrobiť vyšetreniu na zistenie požitia alkoholu alebo inej návykovej látky spôsobom ustanoveným osobitným predpisom, 3a) hoci by také vyšetrenie nebolo spojené s nebezpečenstvom pre jeho zdravie,
b) ako vodič vozidla, ktorý sa zúčastnil na dopravnej nehode, bezodkladne nezastavil vozidlo, nezdržal sa požitia alkoholu alebo inej návykovej látky po nehode v čase, keď by to bolo na ujmu zistenia, či pred jazdou alebo počas jazdy požil alkohol alebo inú návykovú látku, alebo nezotrval na mieste dopravnej nehody až do príchodu policajta alebo sa na toto miesto bezodkladne nevrátil po poskytnutí alebo privolaní pomoci, alebo po ohlásení dopravnej nehody, 3b)
1. ak ide o dopravnú nehodu podľa osobitného predpisu, 3baa)
2. ak ide o škodovú udalosť, ktorá sa považuje za dopravnú nehodu podľa osobitného predpisu, 3bab)
c) vedie motorové vozidlo
1. bez príslušného vodičského oprávnenia, bez osoby spolujazdca, ak prítomnosť spolujazdca vyžaduje osobitný predpis 3ba) alebo počas zadržania vodičského preukazu okrem prípadu, ak vedie motorové vozidlo autoškoly v kurze podľa osobitného predpisu, 3bb) vedie motorové vozidlo v kurze základnej kvalifikácie, 3bc) podrobuje sa skúške z odbornej spôsobilosti alebo preskúšaniu odbornej spôsobilosti z vedenia motorového vozidla alebo má v čase zadržania vodičského preukazu povolenú jazdu,
2. akejkoľvek skupiny počas trvania trestu zákazu činnosti spočívajúceho v zákaze vedenia motorových vozidiel alebo počas trvania sankcie zákazu činnosti spočívajúcej v zákaze vedenia motorových vozidiel,
d) vedie motorové vozidlo v stave vylučujúcom spôsobilosť viesť motorové vozidlo, ktorý si privodil požitím alkoholu,
e) ako vodič počas vedenia vozidla požije alkohol alebo vedie vozidlo v takom čase po jeho požití, keď sa na základe vykonaného vyšetrenia podľa osobitného predpisu 3a) alkohol ešte nachádza v jeho organizme, okrem cyklistu, vodiča kolobežky s pomocným motorčekom a vodiča samovyvažovacieho vozidla jazdiacich v obci a cyklistu, vodiča kolobežky s pomocným motorčekom a vodiča samovyvažovacieho vozidla jazdiacich po cestičke pre cyklistov, ak množstvo alkoholu v jeho organizme nepresiahne hodnotu 0,24 miligramu etanolu na liter vydýchnutého vzduchu pri vyšetrení dychovou skúškou prístrojom alebo 0,5 gramu etanolu na kilogram hmotnosti vyšetrovanej osoby pri lekárskom vyšetrení zo vzorky krvi plynovou chromatografiou,
f) ako vodič počas vedenia vozidla požije inú návykovú látku alebo vedie vozidlo v takom čase po jej požití, keď sa na základe vykonaného vyšetrenia podľa osobitného predpisu 3a) návyková látka ešte nachádza v jeho organizme,
g) poruší všeobecne záväzný právny predpis o bezpečnosti a plynulosti cestnej premávky, v ktorého dôsledku vznikne dopravná nehoda, pri ktorej inému ublíži na zdraví alebo inému spôsobí škodu na majetku,
h) ako vodič motorového vozidla prekročí rýchlosť ustanovenú v osobitnom predpise 3c) alebo prekročí rýchlosť ustanovenú dopravnou značkou alebo dopravným zariadením
1. v obci najviac o 20 km h alebo mimo obce najviac o 30 km h ,
2. v obci o 21 až 50 km h alebo mimo obce o 31 až 60 km h ,
3. v obci o viac ako 50 km h alebo mimo obce o viac ako 60 km h ,
i) použije vozidlo, ktoré
1. nie je schválené na prevádzku v cestnej premávke, je vyradené z cestnej premávky, je vyradené z evidencie alebo je dočasne vyradené z evidencie,
2. má umiestnenú tabuľku s evidenčným číslom, ktorá nie je pridelená tomuto vozidlu,
3. prekračuje najväčšiu technicky prípustnú celkovú hmotnosť vozidla, najväčšiu technicky prípustnú hmotnosť jazdnej súpravy, najväčšiu technicky prípustnú celkovú hmotnosť prípojného vozidla alebo najväčšiu technicky prípustnú hmotnosť pripadajúcu na nápravy vozidla,
4. prekračuje svojimi rozmermi a hmotnosťami ustanovené najväčšie povolené rozmery a ustanovené najväčšie povolené hmotnosti bez povolenia na zvláštne užívanie ciest,
5. pri preprave skaziteľných potravín nespĺňa podmienky podľa osobitného predpisu, 3ca)
j) ako vodič vozidla s najväčšou prípustnou celkovou hmotnosťou vozidla prevyšujúcou 12 000 kg alebo ako vodič jazdnej súpravy s najväčšou prípustnou hmotnosťou prevyšujúcou 12 000 kg vojde na pozemnú komunikáciu, na ktorej je jazda takéhoto vozidla alebo takejto jazdnej súpravy zakázaná,
k) iným spôsobom ako uvedeným v písmenách a) až i) sa dopustí porušenia pravidiel cestnej premávky závažným spôsobom podľa osobitného predpisu, 3d)
l) iným konaním, ako sa uvádza v písmenách a) až k), poruší všeobecne záväzný právny predpis o bezpečnosti a plynulosti cestnej premávky.
(2) Za priestupok podľa odseku 1
a) písm. a), b) prvý bod a c) sa uloží pokuta od 300 eur do 1 300 eur a zákaz činnosti od jedného roku do piatich rokov,
b) písm. b) druhý bod, d) a f) možno uložiť pokutu od 200 eur do 1 000 eur a zákaz činnosti do piatich rokov,
c) písm. e), g) a i) možno uložiť pokutu od 150 eur do 800 eur a zákaz činnosti do troch rokov,
d) písm. h)
1. prvého bodu možno uložiť pokutu do 100 eur,
2. druhého bodu sa uloží pokuta od 150 eur do 600 eur,
3. tretieho bodu sa uloží pokuta od 500 eur do 1 000 eur a zákaz činnosti od šesť mesiacov do troch rokov,
e) písm. j) sa uloží pokuta 1 500 eur,
f) písm. k) možno uložiť pokutu od 60 eur do 300 eur a zákaz činnosti do dvoch rokov,
g) písm. l) možno uložiť pokutu do 100 eur.
(3) V blokovom konaní alebo v rozkaznom konaní za priestupok podľa odseku 1
a) písm. a) až g) a i) možno uložiť pokutu do 650 eur,
b) písm. h)
1. prvého bodu možno uložiť pokutu do 50 eur,
2. druhého bodu sa uloží pokuta od 30 eur do 400 eur,
3. tretieho bodu sa uloží pokuta od 250 eur do 800 eur,
c) písm. j) možno uložiť pokutu do 1 000 eur,
d) písm. k) možno uložiť pokutu do 150 eur,
e) písm. l) možno uložiť pokutu do 50 eur.
(4) Ak sú splnené podmienky podľa § 84 ods. 1 , priestupky podľa odseku 1 písm. h), i) a l) sa prejednajú vždy v blokovom konaní; to neplatí pri priestupku podľa odseku 1 písm. h) tretieho bodu, ak sa ho páchateľ dopustil tretíkrát a viac za posledných 12 mesiacov, alebo ak osobitný zákon ustanovuje inak.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu presne popisuje skutkovú podstatu priestupku podľa § 22 ods. 1 písm. e) zákona o priestupkoch, ktorým je vedenie vozidla v čase, keď sa v organizme vodiča ešte nachádza alkohol. Taktiež správne uvádza sankciu za tento konkrétny priestupok, ktorá je v súlade s § 22 ods. 2 písm. c) pokuta od 150 do 800 eur a zákaz činnosti do troch rokov. Informácie sú plne podložené v predloženom právnom predpise.

---
