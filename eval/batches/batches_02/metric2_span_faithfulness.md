# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 3
Mean question score: 0.833
Mean provision score: 0.833
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Dobrý deň, otec ma vydedil v závete s odôvodnením, že sme spolu roky nekomunikovali. Mám napriek tomu nárok na nejakú časť dedičstva ako neopomenuteľný dedič?

**Model-Selected Provisions:**
- 40/1964/paragraf-469a

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-469a

**Text written by the model for this provision:**

```text
Zákon umožňuje poručiteľovi vydediť svojho potomka z presne stanovených dôvodov. Jedným z týchto dôvodov je, ak potomok o poručiteľa trvalo neprejavuje opravdivý záujem, ktorý by ako potomok mal prejavovať. V listine o vydedení musí byť dôvod vydedenia uvedený.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20241101
PARAGRAPH: 469a
TEXT:
(1) Poručiteľ môže vydediť potomka, ak
a) v rozpore s dobrými mravmi neposkytol poručiteľovi potrebnú pomoc v chorobe, v starobe alebo v iných závažných prípadoch,
b) o poručiteľa trvalo neprejavuje opravdivý záujem, ktorý by ako potomok mal prejavovať,
c) bol odsúdený pre úmyselný trestný čin na trest odňatia slobody v trvaní najmenej jedného roka,
d) trvalo vedie neusporiadaný život.
(2) Pokiaľ to poručiteľ v listine o vydedení výslovne určí, vzťahujú sa dôsledky vydedenia aj na osoby uvedené v § 473 ods. 2 .
(3) O náležitostiach listiny o vydedení a o jej zrušení platia obdobne ustanovenia § 476 a 480 ; v listine však musí byť uvedený dôvod vydedenia.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza, že poručiteľ môže vydediť potomka len z presne stanovených dôvodov. Ako príklad jedného z dôvodov správne cituje trvalé neprejavovanie opravdivého záujmu, čo je v súlade s § 469a ods. 1 písm. b). Taktiež správne konštatuje, že dôvod vydedenia musí byť uvedený v listine o vydedení, čo vyplýva z § 469a ods. 3. Všetky informácie v texte modelu sú vecne podložené právnym predpisom.

---

## ID 1 | Status: OK

**Question:** Dobrý deň. Mám problém s prenajímateľom, ktorý mi nechce vrátiť kauciu s odôvodnením, že v byte zostali drobné poškodenia. Má na to právo, ak ide o bežné opotrebovanie?

**Model-Selected Provisions:**
- 40/1964/paragraf-682

**Question score:** 0.500

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-682

**Text written by the model for this provision:**

```text
Po skončení nájmu je nájomca povinný vrátiť prenajatú vec v stave, v akom ju prevzal, pričom sa prihliada na obvyklé opotrebenie. Toto ustanovenie znamená, že zákon rozlišuje medzi poškodením veci a jej bežným opotrebovaním, ktoré vzniká pri riadnom užívaní.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20241101
PARAGRAPH: 682
TEXT:
Ak sa nájom skončí, je nájomca povinný vrátiť prenajatú vec v stave zodpovedajúcom dojednanému spôsobu užívania veci; ak sa spôsob užívania výslovne nedohodol, v stave, v akom ju prevzal, s prihliadnutím na obvyklé opotrebenie.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza povinnosť nájomcu vrátiť po skončení nájmu prenajatú vec s prihliadnutím na obvyklé opotrebenie. Taktiež správne interpretuje, že zákon týmto rozlišuje medzi bežným opotrebovaním a poškodením. Text je však nepresný, pretože zjednodušuje a vynecháva kľúčovú časť ustanovenia. Zákon primárne stanovuje, že vec sa má vrátiť v stave zodpovedajúcom dojednanému spôsobu užívania. Až ak sa spôsob užívania nedohodol, platí to, čo uvádza model – že sa vec vracia v stave, v akom ju nájomca prevzal. Keďže model prezentuje iba túto subsidiárnu podmienku ako všeobecné pravidlo, je jeho tvrdenie iba čiastočne podporené.

---

## ID 2 | Status: COMPOSE_FAILED

**Question:** Dobrý deň. Už rok a pól riešim pred súdom vyporiadanie podielového a bezpodielového spoluvlastníctva s bývalou manželkou. V marci minulého roku sa dobrovoľne odsťahovala z domu, ktorý je na liste vlastníctva v podielovom spoluvlastníctve v pomere 1/2 môj a 1/2 jej. Ona teraz začala do domu chodiť vtedy, keď som tam ja neni a berie odtiaľ veci. Náklady okolo domu, čo sa týka vody, elektriny, plynu si platím sám, odkedy sa odsťahovala. Čítal som, že existuje zákon, že pokiaľ v tom dome nebýva a dobrovoľne sa odsťahovala (čo mi potvrdila správou), tak že nemôže zasahovať do môjho obydlia. Viete mi poradiť, či je momentálne v poriadku, že by som vymenil zámok a ak bude niečo chcieť, ja jej odomknem nech si zoberie, len nech mi do domu nechodí vtedy, keď som tam ja neni?

**Model-Selected Provisions:**
- 300/2005/paragraf-194

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-194

**Text written by the model for this provision:**

```text
Trestný zákon definuje trestný čin porušovania domovej slobody, ktorého sa dopustí ten, kto neoprávnene vnikne do obydlia iného alebo sa v ňom neoprávnene zdržiava. Podmienkou trestnosti je teda neoprávnenosť takéhoto konania. Páchateľovi tohto trestného činu hrozí trest odňatia slobody, ktorého výška závisí od okolností spáchania.
```

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20250217
PARAGRAPH: 194
TITLE: Porušovanie domovej slobody
TEXT:
(1) Kto neoprávnene vnikne do obydlia iného alebo tam neoprávnene zotrvá, potrestá sa odňatím slobody až na dva roky.
(2) Odňatím slobody na jeden rok až päť rokov sa páchateľ potrestá, ak spácha čin uvedený v odseku 1
a) závažnejším spôsobom konania,
b) prekonaním prekážky, ktorej účelom je zabrániť vniknutiu,
c) najmenej s dvoma osobami, alebo
d) z osobitného motívu.
(3) Odňatím slobody na tri roky až osem rokov sa páchateľ potrestá, ak spácha čin uvedený v odseku 1 alebo 2
a) voči chránenej osobe, alebo
b) ako člen nebezpečného zoskupenia.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je v plnom súlade s právnym predpisom. Správne definuje skutkovú podstatu trestného činu porušovania domovej slobody ako neoprávnené vniknutie do obydlia iného alebo neoprávnené zotrvanie v ňom. Taktiež správne uvádza, že páchateľovi hrozí trest odňatia slobody, pričom jeho výška závisí od okolností spáchania, čo je presné zhrnutie kvalifikovaných skutkových podstát uvedených v odsekoch 2 a 3. Text nepridáva žiadne nepodložené informácie.

---
