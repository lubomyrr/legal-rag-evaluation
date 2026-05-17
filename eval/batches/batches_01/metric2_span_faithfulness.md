# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 4
Mean question score: 0.833
Mean provision score: 0.875
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Chcem si založiť s.r.o., ale nerozumiem, aký je rozdiel medzi konateľom a spoločníkom. Môžem byť oboje?

**Model-Selected Provisions:**
- 513/1991/paragraf-122
- 513/1991/paragraf-133

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
513/1991/paragraf-122

**Text written by the model for this provision:**

```text
Spoločníci si uplatňujú svoje práva, ktoré sa týkajú riadenia a kontroly činnosti spoločnosti, na valnom zhromaždení. Medzi ich práva patrí najmä možnosť žiadať od konateľov informácie o záležitostiach spoločnosti a nahliadať do jej dokladov.
```

**Text of legal provision:**

```text
LAW: 513/1991
VERSION: 20251001
PARAGRAPH: 122
TEXT:
(1) Spoločníci vykonávajú svoje práva týkajúce sa riadenia spoločnosti a kontroly jej činnosti na valnom zhromaždení v rozsahu a spôsobom uvedeným v spoločenskej zmluve, prípadne v stanovách.
(2) Spoločníci majú najmä právo požadovať od konateľov informácie o záležitostiach spoločnosti a nahliadať do dokladov spoločnosti.
(3) Každý spoločník je oprávnený v mene spoločnosti uplatniť nároky na náhradu škody alebo iné nároky, ktoré má spoločnosť voči konateľovi, alebo uplatniť nároky na splatenie vkladu proti spoločníkovi, ktorý je v omeškaní so splatením vkladu, prípadne nároky na vrátenie plnenia vyplateného spoločníkovi v rozpore so zákonom. To neplatí, ak spoločnosť už tieto nároky uplatňuje. Iná osoba ako spoločník, ktorý žalobu podal, alebo ním splnomocnená osoba nemôže v súdnom konaní robiť úkony v mene spoločnosti.
(4) Spoločník, ktorý uplatní v mene spoločnosti nároky podľa odseku 3, je povinný znášať trovy súdneho konania. Ak je spoločnosti priznaná náhrada trov konania, ten, ktorému bola uložená náhrada týchto trov, je povinný uhradiť ju spoločníkovi, ktorý uplatňoval nároky za spoločnosť.
---
LAW: 513/1991
VERSION: 20251001
PARAGRAPH: 122
TEXT:
Každý spoločník je oprávnený v mene spoločnosti uplatniť nároky na náhradu škody alebo iné nároky, ktoré má spoločnosť voči konateľovi, alebo uplatniť nároky na splatenie vkladu proti spoločníkovi, ktorý je v omeškaní so splatením vkladu, prípadne nároky na vrátenie plnenia vyplateného spoločníkovi v rozpore so zákonom. To neplatí, ak spoločnosť už tieto nároky uplatňuje. Iná osoba ako spoločník, ktorý žalobu podal, alebo ním splnomocnená osoba nemôže v súdnom konaní robiť úkony v mene spoločnosti.
---
LAW: 513/1991
VERSION: 20251001
PARAGRAPH: 122
TEXT:
Spoločníci majú najmä právo požadovať od konateľov informácie o záležitostiach spoločnosti a nahliadať do dokladov spoločnosti.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s právnym predpisom. Prvá veta správne parafrázuje odsek 1, podľa ktorého spoločníci vykonávajú svoje práva týkajúce sa riadenia a kontroly na valnom zhromaždení. Druhá veta presne sumarizuje odsek 2, ktorý spoločníkom priznáva právo požadovať informácie od konateľov a nahliadať do dokladov spoločnosti. Model nepridáva žiadne nepodložené informácie.

### Model-Selected Provision 2

**Provision:**
513/1991/paragraf-133

**Text written by the model for this provision:**

```text
Štatutárnym orgánom spoločnosti s ručením obmedzeným je jeden alebo viac konateľov. Konateľov vymenúva valné zhromaždenie, pričom ich môže vybrať z radov spoločníkov alebo aj z iných fyzických osôb. Zákon teda pripúšťa, aby jedna osoba bola zároveň spoločníkom aj konateľom.
```

**Text of legal provision:**

```text
LAW: 513/1991
VERSION: 20251001
PARAGRAPH: 133
TEXT:
(1) Štatutárnym orgánom spoločnosti je jeden alebo viac konateľov. Ak je konateľov viac, je oprávnený konať v mene spoločnosti každý z nich samostatne, ak spoločenská zmluva neurčuje inak.
(2) Konateľom spoločnosti môže byť len fyzická osoba, ktorá nie je v čase vykonania zápisu do obchodného registra ako povinný vedená v registri poverení na vykonanie exekúcie podľa osobitného zákona.
(3) Obmedziť konateľské oprávnenia môže iba spoločenská zmluva alebo valné zhromaždenie. Také obmedzenie je však voči tretím osobám neúčinné.
(4) Konateľov vymenúva valné zhromaždenie z radov spoločníkov alebo iných fyzických osôb.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecne správny a plne podložený právnym predpisom. Tvrdenie, že štatutárnym orgánom je jeden alebo viac konateľov, vychádza z odseku 1. Informácia o tom, že konateľov vymenúva valné zhromaždenie z radov spoločníkov alebo iných fyzických osôb, je presnou parafrázou odseku 4. Záverečná veta, že jedna osoba môže byť spoločníkom aj konateľom, je správnym logickým záverom vyplývajúcim priamo z textu zákona.

---

## ID 1 | Status: OK

**Question:** Dobrý deň. Približne pred mesiacom sme mali v spoločnosti zasadnutie valného zhromaždenia. Ostatní spoločníci schválili zmeny, s ktorými ja nesúhlasím a mám záujem sa voči ním brániť. Existujú nejaké limity alebo obmedzenia toho, voči akému uzneseniu mám možnosť sa brániť?

**Model-Selected Provisions:**
- 513/1991/paragraf-131

**Question score:** 0.500

### Model-Selected Provision 1

**Provision:**
513/1991/paragraf-131

**Text written by the model for this provision:**

```text
Spoločník môže podať na súd návrh na určenie neplatnosti uznesenia valného zhromaždenia, ak je toto uznesenie v rozpore so zákonom, spoločenskou zmluvou alebo stanovami. Súd však môže určiť neplatnosť uznesenia len vtedy, ak toto porušenie mohlo obmedziť práva spoločníka, ktorý sa určenia neplatnosti domáha.
```

**Text of legal provision:**

```text
LAW: 513/1991
VERSION: 20240601
PARAGRAPH: 131
TEXT:
(1) Každý spoločník, konateľ, likvidátor, správca konkurznej podstaty, vyrovnávací správca alebo člen dozornej rady môže podať návrh na súd na určenie neplatnosti uznesenia valného zhromaždenia, ak je v rozpore so zákonom, spoločenskou zmluvou alebo so stanovami. Rovnaké právo má aj bývalý spoločník alebo konateľ, ak sa ho uznesenie valného zhromaždenia týka. Toto právo však zanikne, ak ho oprávnená osoba neuplatní do troch mesiacov od prijatia uznesenia valného zhromaždenia alebo ak valné zhromaždenie nebolo riadne zvolané, odo dňa, keď sa mohla o uznesení dozvedieť.
(2) Súd môže na návrh spoločníka určiť neplatnosť uznesenia valného zhromaždenia, len ak porušenie zákona, spoločenskej zmluvy alebo stanov mohlo obmedziť práva spoločníka, ktorý sa určenia neplatnosti domáha.
(3) V konaní konajú za spoločnosť konatelia; ak sú však účastníkmi konania sami konatelia, zastupuje spoločnosť určený člen (členovia) dozornej rady. Ak žalujú tak konatelia, ako aj členovia dozornej rady, alebo ak nie je dozorná rada zriadená, určí zástupcu spoločnosti valné zhromaždenie. Ak tak neurobí do troch mesiacov od doručenia žaloby spoločnosti, ustanoví súd spoločnosti opatrovníka.
(4) Neplatnosť uznesenia valného zhromaždenia spoločnosti sa netýka práv nadobudnutých v dobrej viere tretími osobami. V pochybnostiach platí, že tretie osoby nadobudli práva v dobrej viere.
(5) Právoplatné rozhodnutie súdu podľa odseku 1 je záväzné pre každého.
---
LAW: 513/1991
VERSION: 20251001
PARAGRAPH: 131
TEXT:
(1) Každý spoločník, konateľ, likvidátor, správca konkurznej podstaty, vyrovnávací správca alebo člen dozornej rady môže podať návrh na súd na určenie neplatnosti uznesenia valného zhromaždenia, ak je v rozpore so zákonom, spoločenskou zmluvou alebo so stanovami. Rovnaké právo má aj bývalý spoločník alebo konateľ, ak sa ho uznesenie valného zhromaždenia týka. Toto právo však zanikne, ak ho oprávnená osoba neuplatní do troch mesiacov od prijatia uznesenia valného zhromaždenia alebo ak valné zhromaždenie nebolo riadne zvolané, odo dňa, keď sa mohla o uznesení dozvedieť.
(2) Súd môže na návrh spoločníka určiť neplatnosť uznesenia valného zhromaždenia, len ak porušenie zákona, spoločenskej zmluvy alebo stanov mohlo obmedziť práva spoločníka, ktorý sa určenia neplatnosti domáha.
(3) V konaní konajú za spoločnosť konatelia; ak sú však účastníkmi konania sami konatelia, zastupuje spoločnosť určený člen (členovia) dozornej rady. Ak žalujú tak konatelia, ako aj členovia dozornej rady, alebo ak nie je dozorná rada zriadená, určí zástupcu spoločnosti valné zhromaždenie. Ak tak neurobí do troch mesiacov od doručenia žaloby spoločnosti, ustanoví súd spoločnosti opatrovníka.
(4) Neplatnosť uznesenia valného zhromaždenia spoločnosti sa netýka práv nadobudnutých v dobrej viere tretími osobami. V pochybnostiach platí, že tretie osoby nadobudli práva v dobrej viere.
(5) Právoplatné rozhodnutie súdu podľa odseku 1 je záväzné pre každého.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza, že spoločník sa môže na súde domáhať neplatnosti uznesenia valného zhromaždenia, ak je v rozpore so zákonom, spoločenskou zmluvou alebo stanovami. Taktiež správne parafrázuje podmienku z odseku 2, že súd určí neplatnosť len vtedy, ak porušenie mohlo obmedziť práva daného spoločníka. Text je však nepresný, pretože zjednodušuje okruh osôb, ktoré môžu návrh podať. Podľa zákona toto právo nemá len spoločník, ale aj konateľ, likvidátor, správca konkurznej podstaty a ďalšie osoby vymenované v odseku 1. Zameraním sa výlučne na spoločníka je tvrdenie síce v jadre správne, ale neúplné a príliš zovšeobecňujúce.

---

## ID 2 | Status: OK

**Question:** Dobrý deň, chcel by som si založiť spoločnosť. Všetky dokumenty som si pripravil a zaslal na obchodný register. Moja spoločnosť však nebola založená, nakoľko som podanie neurobil elektronicky. Je možnosť založiť spoločnosť aj v papierovej forme alebo musím podanie uskutočniť iba elektronicky?

**Model-Selected Provisions:**
- 530/2003/paragraf-5

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
530/2003/paragraf-5

**Text written by the model for this provision:**

```text
Návrh na zápis do obchodného registra, návrh na zápis zmeny údajov alebo návrh na výmaz údajov sa podáva výlučne elektronickými prostriedkami. Registrový súd na návrh podaný inou ako elektronickou formou, napríklad v listinnej podobe, neprihliada.
```

**Text of legal provision:**

```text
LAW: 530/2003
VERSION: 20240601
PARAGRAPH: 5
TITLE: Návrh
TEXT:
(1) Návrh na zápis údajov do obchodného registra, návrh na zápis zmeny zapísaných údajov a návrh na výmaz zapísaných údajov (ďalej len "návrh na zápis") podáva navrhovateľ, ktorým je zapísaná osoba alebo osoba oprávnená podľa osobitného zákona. 1) Osvedčenie pravosti podpisu navrhovateľa a pravosti podpisu splnomocniteľa, ak ide o zastúpenie na základe plnomocenstva, sa nevyžaduje.
(2) Návrh na zápis sa podáva výlučne elektronickými prostriedkami registrovému súdu prostredníctvom elektronického formulára zverejneného na webovom sídle ústredného portálu verejnej správy 6a) alebo špecializovaného portálu. 6b) Elektronický formulár obsahuje náležitosti ustanovené osobitným predpisom. 6c)
(3) Na návrh na zápis podaný registrovému súdu inak ako podľa odseku 2 registrový súd neprihliada.
(4) Návrh na zápis musí byť autorizovaný 5aa) navrhovateľom a musí byť podaný spolu s listinami v elektronickej podobe, z ktorých vyplývajú údaje, ktoré sa majú do obchodného registra zapísať, a listinami, z ktorých vyplývajú skutočnosti, ktoré sa majú podľa tohto zákona preveriť, inak registrový súd naň neprihliada; to neplatí, ak povaha alebo veľkosť listiny podľa prvej vety neumožňuje jej podanie spolu s návrhom na zápis v elektronickej podobe. Listinná podoba listiny podľa prvej vety prevádzaná do elektronickej podoby na účely jej podania v elektronickej podobe musí mať formu ustanovenú osobitným zákonom. 1)
(5) Ak povaha alebo veľkosť listiny, ktorá sa prikladá k návrhu na zápis podľa odseku 4, neumožňuje jej podanie v elektronickej podobe spolu s návrhom na zápis v elektronickej podobe, navrhovateľ k návrhu na zápis pripojí písomné vyhlásenie, v ktorom uvedie dôvod, pre ktorý listina nemohla byť podaná v elektronickej podobe spolu s návrhom, a v lehote 15 dní odo dňa podania návrhu na zápis doručí listinu v listinnej podobe registrovému súdu, inak registrový súd na návrh na zápis nebude prihliadať. Ustanovenia osobitného zákona 6a) o zaručenej konverzii sa na postup registrového súdu podľa predchádzajúcej vety nepoužijú.
(6) Účinky doručenia návrhu na zápis nastávajú v deň, keď registrovému súdu prišla informácia o zaplatení súdneho poplatku a registrovému súdu bola doručená listina podľa odseku 5, ak sa k návrhu na zápis mala priložiť, a zároveň neuplynulo 15 dní odo dňa podania návrhu na zápis.
(7) Ak navrhovateľ uvádza v návrhu na prvý zápis viacero predmetov podnikania alebo činností, uvedie na prvom mieste ten predmet podnikania alebo tú činnosť, ktorú považuje za hlavnú.
(8) Späťvzatie návrhu na zápis sa nepripúšťa.
(9) Fyzické osoby oprávnené konať v mene zapísanej právnickej osoby sú povinné najneskôr do 30 dní odo dňa uvedeného v rozhodnutí spoločníkov alebo orgánu spoločnosti, orgánu družstva alebo inej zapísanej osoby, inak odo dňa, keď bolo toto rozhodnutie prijaté, alebo odo dňa, keď nastali účinky právnej skutočnosti, podať návrh na zápis zmeny zapísaných údajov alebo návrh na výmaz zapísaných údajov.
(10) Fyzické osoby oprávnené konať v mene zapísanej právnickej osoby sú povinné uviesť v návrhu na zápis pravdivé údaje a doložiť ho listinami, ktorých obsah zodpovedá skutočnému stavu.
(11) Ak ukladá notár do zbierky listín osvedčenie podľa osobitného predpisu, 5a) listina sa ukladá do zbierky listín registrového súdu výlučne elektronickými prostriedkami. Registrový súd zašle osvedčenie podľa prvej vety bezodkladne po jeho uložení prostredníctvom systému prepojenia registrov zahraničnému obchodnému registru alebo inej evidencii, v ktorej je zahraničná zúčastnená alebo nástupnícka osoba zapísaná alebo v ktorej je povinná ukladať listiny.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je presným zhrnutím kľúčových informácií z paragrafu 5 ods. 2 a 3. Prvá veta o podávaní návrhov výlučne elektronickými prostriedkami je priamo podložená v odseku 2. Druhá veta o tom, že súd na návrh podaný inou formou (napr. listinne) neprihliada, je správnou interpretáciou odseku 3. Text modelu nepridáva žiadne nepodložené informácie a zachováva právny význam predpisu.

---
