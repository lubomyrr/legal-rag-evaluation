# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 6
Mean question score: 0.944
Mean provision score: 0.917
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Obraciam sa na vás s otázkou ohľadom možnosti zníženia výživného po strate zamestnania. Nedávno som prišiel o prácu a v súčasnosti som nezamestnaný, čo výrazne ovplyvnilo moje finančné možnosti. Som povinný platiť výživné na dve deti z predchádzajúceho manželstva. Ako môžem postupovať pri žiadosti o dočasné zníženie výživného kvôli mojej zmenenej finančnej situácii?

**Model-Selected Provisions:**
- 36/2005/paragraf-62
- 36/2005/paragraf-75
- 36/2005/paragraf-78

**Question score:** 0.833

### Model-Selected Provision 1

**Provision:**
36/2005/paragraf-62

**Text written by the model for this provision:**

```text
Zákon stanovuje, že každý rodič je povinný plniť si svoju vyživovaciu povinnosť v minimálnom rozsahu. Táto minimálna výška výživného je určená ako 30 % zo sumy životného minima na nezaopatrené dieťa, a to bez ohľadu na schopnosti, možnosti a majetkové pomery rodiča.
```

**Text of legal provision:**

```text
LAW: 36/2005
VERSION: 2023010
PARAGRAPH: 62
TEXT:
Plnenie vyživovacej povinnosti rodičov k deťom je ich zákonná povinnosť, ktorá trvá do času, kým deti nie sú schopné samé sa živiť.
---
LAW: 36/2005
VERSION: 20230101
PARAGRAPH: 62
TEXT:
Každý rodič bez ohľadu na svoje schopnosti, možnosti a majetkové pomery je povinný plniť svoju vyživovaciu povinnosť v minimálnom rozsahu vo výške 30 % zo sumy životného minima na nezaopatrené neplnoleté dieťa alebo na nezaopatrené dieťa podľa osobitného zákona. 13)
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s poskytnutým znením právneho predpisu. Správne uvádza, že každý rodič má povinnosť platiť výživné v minimálnej výške, ktorá je stanovená ako 30 % zo sumy životného minima na dieťa, a to bez ohľadu na jeho schopnosti, možnosti a majetkové pomery. Všetky informácie v texte modelu sú podložené.

### Model-Selected Provision 2

**Provision:**
36/2005/paragraf-75

**Text written by the model for this provision:**

```text
Pri určení výšky výživného súd berie do úvahy odôvodnené potreby dieťaťa a zároveň aj schopnosti, možnosti a majetkové pomery povinnej osoby. Súd prihliada aj na situácie, kedy sa povinná osoba bez dôležitého dôvodu vzdá lepšieho zamestnania alebo zárobku.
```

**Text of legal provision:**

```text
LAW: 36/2005
VERSION: 20230101
PARAGRAPH: 75
TEXT:
Pri určení výživného prihliadne súd na odôvodnené potreby oprávneného, ako aj na schopnosti, možnosti a majetkové pomery povinného. Na schopnosti, možnosti a majetkové pomery povinného prihliadne súd aj vtedy, ak sa povinný vzdá bez dôležitého dôvodu výhodnejšieho zamestnania, zárobku, majetkového prospechu; rovnako prihliadne aj na neprimerané majetkové riziká, ktoré povinný na seba berie.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu presne parafrázuje obsah právneho predpisu. Správne uvádza, že súd pri určení výživného prihliada na odôvodnené potreby oprávneného (dieťaťa) a na schopnosti, možnosti a majetkové pomery povinného. Taktiež správne spomína, že súd zohľadní, ak sa povinný bezdôvodne vzdá lepšieho zárobku. Text je vecne správny a podložený.

### Model-Selected Provision 3

**Provision:**
36/2005/paragraf-78

**Text written by the model for this provision:**

```text
Dohody a súdne rozhodnutia o výživnom je možné zmeniť, ak dôjde k zmene pomerov. Pri posudzovaní zmeny pomerov sa vždy prihliada aj na vývoj životných nákladov.
```

**Text of legal provision:**

```text
LAW: 36/2005
VERSION: 20230101
PARAGRAPH: 78
TEXT:
Pri zmene pomerov sa vždy prihliadne na vývoj životných nákladov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu je podložený iba čiastočne. Druhá veta, ktorá hovorí o prihliadaní na vývoj životných nákladov pri zmene pomerov, je priamo podložená poskytnutým textom. Prvá veta, ktorá uvádza, že dohody a súdne rozhodnutia o výživnom je možné zmeniť pri zmene pomerov, je síce vecne správna, ale táto informácia sa v poskytnutom úryvku právneho predpisu nenachádza. Model teda dopĺňa informáciu, ktorá nie je v zdrojovom texte, preto je skóre 0.5.

---

## ID 1 | Status: OK

**Question:** Moje vozidlo bolo namerané radarom v meste, ale auto šoféroval môj otec. Pokutu poslali mne ako držiteľovi vozidla. Musím ju zaplatiť?

**Model-Selected Provisions:**
- 8/2009/paragraf-6a

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
8/2009/paragraf-6a

**Text written by the model for this provision:**

```text
Držiteľ vozidla má zákonnú povinnosť zabezpečiť, aby pri prevádzkovaní jeho motorového vozidla boli dodržiavané pravidlá cestnej premávky. Táto povinnosť sa vzťahuje aj na dodržiavanie povolenej rýchlosti jazdy.
```

**Text of legal provision:**

```text
LAW: 8/2009
VERSION: 20250701
PARAGRAPH: 6a
TITLE: Povinnosti držiteľa vozidla
TEXT:
Držiteľ vozidla je povinný zabezpečiť, aby pri prevádzkovaní motorového vozidla boli dodržiavané pravidlá cestnej premávky podľa tohto zákona, ktoré ustanovujú
a) zákaz predchádzania podľa § 15 ods. 5 , § 35 ods. 3 alebo zákaz predchádzania vyplývajúci z dopravnej značky alebo dopravného zariadenia,
b) rýchlosť jazdy podľa § 16 alebo § 27 ods. 3 ,
c) povinnosť zastaviť vozidlo na príkaz dopravnej značky "Stoj, daj prednosť v jazde!" alebo na signál so znamením "Stoj!",
d) zákaz otáčania a cúvania podľa § 22 ods. 4 alebo zákaz otáčania vyplývajúci z dopravnej značky alebo dopravného zariadenia,
e) zákaz zastavenia a státia podľa § 25 alebo zákaz zastavenia alebo státia vyplývajúci z dopravnej značky alebo dopravného zariadenia,
f) prejazd cez železničné priecestie v čase, keď je to zakázané podľa § 27 až 29 ,
g) najväčšiu prípustnú celkovú hmotnosť vozidla, najväčšiu prípustnú hmotnosť jazdnej súpravy, najväčšiu prípustnú celkovú hmotnosť prípojného vozidla alebo najväčšiu prípustnú hmotnosť pripadajúcu na nápravu vozidla podľa § 51 ,
h) zákaz vjazdu, zákaz odbočovania alebo prikázaný smer jazdy vyplývajúci z dopravnej značky alebo dopravného zariadenia,
i) zákaz vjazdu vozidla vyplývajúci z dopravnej značky alebo dopravného zariadenia alebo zákaz jazdy vozidla s najväčšou prípustnou celkovou hmotnosťou vozidla prevyšujúcou 12 000 kg alebo jazdnej súpravy s najväčšou prípustnou celkovou hmotnosťou prevyšujúcou 12 000 kg podľa § 39 ods. 4 ,
j) povinnosť umožniť vozidlu, ktoré používa typické zvukové znamenie doplnené zvláštnym výstražným modrým svetlom alebo červeným svetlom, prípadne ich kombináciou (ďalej len "zvláštne výstražné znamenie") pri plnení špeciálnych úloh (ďalej len "vozidlo s právom prednostnej jazdy"), a vozidlu, ktoré sprevádza, bezpečný a plynulý prejazd podľa § 40 ods. 8 ,
k) povinnosť vytvoriť voľný priestor na prejazd vozidiel (ďalej len "záchranárska ulička") podľa § 10 ods. 11 alebo zákaz jazdy v záchranárskej uličke podľa § 10 ods. 11.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s právnym predpisom. Prvá veta presne parafrázuje úvodnú vetu § 6a, ktorá ustanovuje všeobecnú povinnosť držiteľa vozidla zabezpečiť dodržiavanie pravidiel cestnej premávky. Druhá veta správne uvádza, že táto povinnosť sa vzťahuje aj na dodržiavanie rýchlosti jazdy, čo je explicitne uvedené v písmene b) daného paragrafu. Model nepridáva žiadne nepodložené informácie, preto je hodnotenie 1.0.

---

## ID 2 | Status: OK

**Question:** Dobrý deň, potreboval by som pomôcť s pokutou, ktorá mi prišla domov. Údajne som vyšiel na diaľnicu bez diaľničnej známky a domov mi prišla pokuta. Ja som si však diaľničnú známku kúpil. Bohužiaľ, pri jej zadávaní musela nastať chyba a diaľničnú známku som kúpil na iné evidenčné číslo. Je možné reklamovať takto zakúpenú diaľničnú známku aby som sa vyhol pokute alebo ako mám postupovať. Ďakujem.

**Model-Selected Provisions:**
- 488/2013/paragraf-10
- 488/2013/paragraf-13

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
488/2013/paragraf-10

**Text written by the model for this provision:**

```text
Zákon definuje, že priestupku sa dopustí vodič, ktorý použije vymedzené úseky diaľnic bez toho, aby mal uhradenú diaľničnú známku. Pre spáchanie priestupku je teda rozhodujúce samotné použitie diaľnice bez platnej úhrady.
```

**Text of legal provision:**

```text
LAW: 488/2013
VERSION: 20250101
PARAGRAPH: 10
TITLE: Priestupky
TEXT:
Priestupku sa dopustí ten, kto ako vodič použije vymedzené úseky diaľnic bez úhrady diaľničnej známky.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s právnym predpisom. Správne identifikuje, že priestupku sa dopustí vodič, ktorý použije vymedzené úseky diaľnic bez úhrady diaľničnej známky. Druhá veta je len logickým zhrnutím skutkovej podstaty priestupku, ktoré je vecne správne a nič podstatné nepridáva.

### Model-Selected Provision 2

**Provision:**
488/2013/paragraf-13

**Text written by the model for this provision:**

```text
Proti doručenému rozkazu o uložení pokuty môže prevádzkovateľ vozidla podať odpor. Lehota na podanie odporu je 15 dní odo dňa doručenia a podáva sa na okresnom úrade, ktorý rozkaz vydal. Odpor musí byť odôvodnený, pričom je potrebné uviesť rozhodujúce skutočnosti a označiť dôkazy na preukázanie svojich tvrdení.
```

**Text of legal provision:**

```text
LAW: 488/2013
VERSION: 20250101
PARAGRAPH: 13
TEXT:
Prevádzkovateľ vozidla môže proti rozkazu podať do 15 dní odo dňa jeho doručenia odpor okresnému úradu, ktorý rozkaz vydal. Odpor proti rozkazu sa musí odôvodniť. V odôvodnení uvedie prevádzkovateľ vozidla rozhodujúce skutočnosti, o ktoré opiera svoju obranu proti výroku uvedenému v rozkaze, a zároveň označí dôkazy na preukázanie svojich tvrdení. K odporu pripojí listinné dôkazy, ktorých sa dovoláva. O tomto musí byť prevádzkovateľ vozidla v rozkaze poučený. Ustanovenie § 19 ods. 3 všeobecného predpisu o správnom konaní sa nepoužije.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu presne a vecne správne parafrázuje obsah právneho predpisu. Správne uvádza, kto môže podať odpor (prevádzkovateľ vozidla), lehotu (15 dní od doručenia), orgán, ktorému sa podáva (okresný úrad, ktorý rozkaz vydal), aj základné náležitosti odporu (odôvodnenie, uvedenie skutočností a označenie dôkazov). Ide o presné zhrnutie, ktoré nemení právny význam.

---
