# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 6
Mean question score: 0.917
Mean provision score: 0.833
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Obraciam sa na vás s otázkou týkajúcou sa odstúpenia od kúpnej zmluvy. Nedávno som uzavrela kúpnu zmluvu na kúpu nehnuteľnosti, ale zistila som niekoľko problémov, ktoré neboli vopred uvedené.

**Model-Selected Provisions:**
- 40/1964/paragraf-597

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-597

**Text written by the model for this provision:**

```text
Kupujúci má právo odstúpiť od zmluvy, ak ho predávajúci ubezpečil, že vec má určité vlastnosti, alebo že je bez vád, a toto ubezpečenie sa neskôr ukáže ako nepravdivé. Toto právo na odstúpenie sa vzťahuje aj na situáciu, keď sa nepravdivým ukáže ubezpečenie o vlastnostiach, ktoré si kupujúci vopred vymienil.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20241101
PARAGRAPH: 597
TEXT:
Právo odstúpiť od zmluvy má kupujúci aj vtedy, ak ho predávajúci ubezpečil, že vec má určité vlastnosti, najmä vlastnosti vymienené kupujúcim, alebo že nemá žiadne vady, a toto ubezpečenie sa ukáže nepravdivým.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu presne a kompletne parafrázuje obsah právneho predpisu. Správne uvádza, že kupujúci môže odstúpiť od zmluvy, ak sa ubezpečenie predávajúceho o vlastnostiach veci (vrátane tých, ktoré si kupujúci vymienil) alebo o jej bezchybnosti ukáže ako nepravdivé. Všetky informácie v texte modelu sú plne podložené citovaným paragrafom.

---

## ID 1 | Status: OK

**Question:** Potrebovala by som sa poradiť ohľadom nároku na majetok v prípade, že dlhodobo žijem s mojim priateľom ako družka. Sme spolu už desať rokov, ale nie sme zosobášení. Počas nášho spolužitia sme nadobudli určitý majetok, vrátane domu a niekoľkých cenností. Chcela by som vedieť, aký nárok mám na tento majetok v prípade rozchodu alebo úmrtia môjho partnera, keďže sme nikdy neboli manželmi.

**Model-Selected Provisions:**
- 40/1964/paragraf-116
- 40/1964/paragraf-141
- 40/1964/paragraf-143
- 40/1964/paragraf-451

**Question score:** 0.750

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-116

**Text written by the model for this provision:**

```text
Blízkou osobou je okrem príbuzných a manžela aj iná osoba v rodinnom alebo obdobnom pomere. Musí však platiť, že by ujmu, ktorú utrpela jedna z nich, druhá dôvodne pociťovala ako vlastnú ujmu. Tento status môže byť dôležitý napríklad v dedičskom konaní.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20241101
PARAGRAPH: 116
TEXT:
Blízkou osobou je príbuzný v priamom rade, súrodenec a manžel; iné osoby v pomere rodinnom alebo obdobnom sa pokladajú za osoby sebe navzájom blízke, ak by ujmu, ktorú utrpela jedna z nich, druhá dôvodne pociťovala ako vlastnú ujmu.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Jadro definície blízkej osoby je správne a vychádza z predpisu. Text modelu však pridáva informáciu, ktorá v danom paragrafe nie je obsiahnutá – príklad využitia statusu blízkej osoby v dedičskom konaní. Hoci je tento príklad vecne správny, ide o doplnenie informácie nad rámec poskytnutého textu zákona, čo znižuje skóre.

### Model-Selected Provision 2

**Provision:**
40/1964/paragraf-141

**Text written by the model for this provision:**

```text
Spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. Ak je predmetom spoluvlastníctva nehnuteľnosť, zákon pre takúto dohodu vyžaduje písomnú formu.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20191201
PARAGRAPH: 141
TEXT:
(1) Spoluvlastníci sa môžu dohodnúť o zrušení spoluvlastníctva a o vzájomnom vyporiadaní; ak je predmetom spoluvlastníctva nehnuteľnosť, dohoda musí byť písomná.
(2) Každý zo spoluvlastníkov je povinný vydať ostatným na požiadanie písomné potvrdenie o tom, ako sa vyporiadali, ak nemala už dohoda o zrušení spoluvlastníctva a o vzájomnom vyporiadaní písomnú formu.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je presným a vecným zhrnutím odseku 1 daného paragrafu. Správne uvádza možnosť dohody o zrušení spoluvlastníctva a požiadavku písomnej formy v prípade nehnuteľností. Nepridáva žiadne nové informácie a nemení právny význam.

### Model-Selected Provision 3

**Provision:**
40/1964/paragraf-143

**Text written by the model for this provision:**

```text
Bezpodielové spoluvlastníctvo manželov je majetkový režim, ktorý vzniká len medzi manželmi. Vzťahuje sa na veci nadobudnuté ktorýmkoľvek z nich počas trvania manželstva, s určitými zákonnými výnimkami.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20241101
PARAGRAPH: 143
TEXT:
V bezpodielovom spoluvlastníctve manželov je všetko, čo môže byť predmetom vlastníctva a čo nadobudol niektorý z manželov za trvania manželstva, s výnimkou vecí získaných dedičstvom alebo darom, ako aj vecí, ktoré podľa svojej povahy slúžia osobnej potrebe alebo výkonu povolania len jedného z manželov, a vecí vydaných v rámci predpisov o reštitúcii majetku jednému z manželov, ktorý mal vydanú vec vo vlastníctve pred uzavretím manželstva alebo ktorému bola vec vydaná ako právnemu nástupcovi pôvodného vlastníka. 3)
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Model poskytuje výstižné zhrnutie podstaty bezpodielového spoluvlastníctva manželov. Správne uvádza, že ide o majetok nadobudnutý počas manželstva a zmieňuje existenciu zákonných výnimiek, čím presne sumarizuje obsah paragrafu bez toho, aby ho skresľoval alebo pridával nepodložené informácie.

### Model-Selected Provision 4

**Provision:**
40/1964/paragraf-451

**Text written by the model for this provision:**

```text
Kto sa na úkor iného bezdôvodne obohatí, je povinný toto obohatenie vydať. Za bezdôvodné obohatenie sa považuje majetkový prospech získaný plnením bez právneho dôvodu, z neplatného právneho úkonu alebo z právneho dôvodu, ktorý odpadol.
```

**Text of legal provision:**

```text
LAW: 40/1964
VERSION: 20191201
PARAGRAPH: 451
TEXT:
(1) Kto sa na úkor iného bezdôvodne obohatí, musí obohatenie vydať.
(2) Bezdôvodným obohatením je majetkový prospech získaný plnením bez právneho dôvodu, plnením z neplatného právneho úkonu alebo plnením z právneho dôvodu, ktorý odpadol, ako aj majetkový prospech získaný z nepoctivých zdrojov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu správne parafrázuje všeobecnú povinnosť vydať bezdôvodné obohatenie a vymenúva tri prípady, kedy k nemu dochádza. Vypúšťa však štvrtý prípad uvedený v zákone, a to "majetkový prospech získaný z nepoctivých zdrojov". Tým, že neuvádza, že jeho výpočet nie je úplný, je zhrnutie nepresné.

---

## ID 2 | Status: OK

**Question:** Zamestnávateľ mi znížil mzdu bez môjho súhlasu. Môže to urobiť jednostranne?

**Model-Selected Provisions:**
- 311/2001/paragraf-54

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
311/2001/paragraf-54

**Text written by the model for this provision:**

```text
Dohodnutý obsah pracovnej zmluvy, ktorého súčasťou sú aj mzdové podmienky, je možné zmeniť iba vtedy, ak sa na tom zamestnávateľ a zamestnanec dohodnú. Zamestnávateľ je povinný takúto zmenu pracovnej zmluvy vyhotoviť písomne.
```

**Text of legal provision:**

```text
LAW: 311/2001
VERSION: 20250715
PARAGRAPH: 54
TITLE: Zmena pracovnej zmluvy
TEXT:
Dohodnutý obsah pracovnej zmluvy možno zmeniť len vtedy, ak sa zamestnávateľ a zamestnanec dohodnú na jeho zmene. Zamestnávateľ je povinný zmenu pracovnej zmluvy vyhotoviť písomne a jedno vyhotovenie zmeny pracovnej zmluvy vydať zamestnancovi.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza kľúčové informácie z právneho predpisu: zmena obsahu pracovnej zmluvy je možná len po vzájomnej dohode a zamestnávateľ musí túto zmenu vyhotoviť písomne. Doplnenie, že mzdové podmienky sú súčasťou pracovnej zmluvy, je vecne správna konkretizácia, ktorá nemení význam ustanovenia. Model síce nespomína povinnosť zamestnávateľa vydať zamestnancovi jedno vyhotovenie zmeny, no ide o zjednodušenie, ktoré neovplyvňuje vecnú správnosť hlavnej myšlienky. Celkovo je text modelu presným zhrnutím, ktoré je plne podporené predpisom.

---
