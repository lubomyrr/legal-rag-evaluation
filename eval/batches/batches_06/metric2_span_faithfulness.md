# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 2
Evaluated model-selected provisions: 3
Mean question score: 1.000
Mean provision score: 1.000
Skipped questions: 0
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 1 | Status: OK

**Question:** Ak je jeden z manželov ťažko chorý a odkázaný na pomoc, musí mu druhý manžel po rozvode platiť výživné ako bývalému manželovi?

**Model-Selected Provisions:**
- 36/2005/paragraf-72
- 36/2005/paragraf-75

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
36/2005/paragraf-72

**Text written by the model for this provision:**

```text
Rozvedený manžel, ktorý nie je schopný sám sa živiť, môže od bývalého manžela žiadať príspevok na primeranú výživu. Súd môže príspevok priznať najdlhšie na päť rokov, no túto dobu môže výnimočne predĺžiť, ak rozvedený manžel nie je schopný sa sám živiť z objektívnych dôvodov, napríklad pre dlhodobo nepriaznivý zdravotný stav vyžadujúci sústavnú opateru.
```

**Text of legal provision:**

```text
LAW: 36/2005
VERSION: 20250801
PARAGRAPH: 72
TEXT:
(1) Rozvedený manžel, ktorý nie je schopný sám sa živiť, môže žiadať od bývalého manžela, aby mu prispieval na primeranú výživu podľa svojich schopností, možností a majetkových pomerov.
(2) Ak sa bývalí manželia nedohodnú, určí rozsah príspevku na výživu na návrh niektorého z nich súd. Prihliadne pritom aj na príčiny, ktoré viedli k rozvratu vzťahov medzi manželmi.
(3) Príspevok na výživu rozvedeného manžela možno priznať najdlhšie na dobu piatich rokov odo dňa právoplatnosti rozhodnutia o rozvode. Súd môže výnimočne túto dobu predĺžiť, ak rozvedený manžel, ktorému súd príspevok priznal, nie je z objektívnych dôvodov schopný sám sa živiť ani po uplynutí tejto doby, najmä ak ide o toho manžela, ktorému bolo v konaní o rozvod manželstva zverené do osobnej starostlivosti dieťa s dlhodobo nepriaznivým zdravotným stavom, alebo o manžela, ktorý má sám dlhodobo nepriaznivý zdravotný stav vyžadujúci sústavnú opateru.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecným a presným zhrnutím právneho predpisu. Správne uvádza podmienky pre vznik nároku na príspevok na výživu rozvedeného manžela, jeho maximálnu dĺžku trvania (päť rokov) aj možnosť výnimočného predĺženia. Príklad uvedený v texte modelu (dlhodobo nepriaznivý zdravotný stav) je priamo obsiahnutý v právnom predpise. Zhrnutie je úplne podložené.

### Model-Selected Provision 2

**Provision:**
36/2005/paragraf-75

**Text written by the model for this provision:**

```text
Pri rozhodovaní o výživnom súd prihliada na odôvodnené potreby oprávneného. Zároveň posudzuje schopnosti, možnosti a majetkové pomery povinného, a to aj v prípade, ak sa bez dôležitého dôvodu vzdal výhodnejšieho zárobku alebo podstupuje neprimerané majetkové riziká.
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
Text modelu presne a kompletne parafrázuje obsah právneho predpisu. Správne uvádza, že súd pri určení výživného prihliada na odôvodnené potreby oprávneného a zároveň na schopnosti, možnosti a majetkové pomery povinného. Taktiež správne zmieňuje, že súd zohľadňuje aj fiktívny príjem v prípadoch, keď sa povinný bezdôvodne vzdal lepšieho zárobku alebo podstupuje neprimerané majetkové riziká. Všetky tvrdenia sú plne podporené.

---

## ID 2 | Status: COMPOSE_FAILED

**Question:** Dobrý deň, chcel by som sa informovať ohľadom vyživovacej povinnosti voči plnoletému synovi. Doteraz som výživné platil matke na účet, ktorý mi oznámila. Dozvedel som sa však, že od dovŕšenia plnoletosti by som mal výživné platiť synovi a nie matke. Je to pravda alebo musím platiť výživné tak ako doteraz.

**Model-Selected Provisions:**
- 36/2005/paragraf-62

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
36/2005/paragraf-62

**Text written by the model for this provision:**

```text
Zákon ustanovuje, že vyživovacia povinnosť rodičov voči deťom trvá až do času, kým deti nie sú schopné samé sa živiť. Každý rodič je povinný plniť túto povinnosť v minimálnom zákonom stanovenom rozsahu.
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
Text modelu je plne v súlade s predloženým znením zákona. Tvrdenie, že vyživovacia povinnosť trvá, kým deti nie sú schopné samé sa živiť, je priamo podložené v prvom odseku predpisu. Tvrdenie, že každý rodič musí plniť túto povinnosť v minimálnom zákonom stanovenom rozsahu, je takisto podložené v druhom odseku, ktorý tento minimálny rozsah definuje. Keďže text modelu je vecnou a presnou sumarizáciou predpisu, skóre je 1.0.

---
