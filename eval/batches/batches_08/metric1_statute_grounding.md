# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 6
False positives: 0
False negatives: 0
Precision: 1.000
Recall: 1.000
F1: 1.000

## ID 0 | Status: OK

**Question:** Obraciam sa na vás s otázkou ohľadom možnosti zníženia výživného po strate zamestnania. Nedávno som prišiel o prácu a v súčasnosti som nezamestnaný, čo výrazne ovplyvnilo moje finančné možnosti. Som povinný platiť výživné na dve deti z predchádzajúceho manželstva. Ako môžem postupovať pri žiadosti o dočasné zníženie výživného kvôli mojej zmenenej finančnej situácii?

**Expected Provisions:**
- 36/2005/paragraf-62
- 36/2005/paragraf-75
- 36/2005/paragraf-78

**Model-Selected Provisions:**
- 36/2005/paragraf-62
- 36/2005/paragraf-75
- 36/2005/paragraf-78

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-75",
    "odpoved_vygenerovana": "Pri určení výšky výživného súd berie do úvahy odôvodnené potreby dieťaťa a zároveň aj schopnosti, možnosti a majetkové pomery povinnej osoby. Súd prihliada aj na situácie, kedy sa povinná osoba bez dôležitého dôvodu vzdá lepšieho zamestnania alebo zárobku."
  },
  {
    "zakon": "36/2005/paragraf-62",
    "odpoved_vygenerovana": "Zákon stanovuje, že každý rodič je povinný plniť si svoju vyživovaciu povinnosť v minimálnom rozsahu. Táto minimálna výška výživného je určená ako 30 % zo sumy životného minima na nezaopatrené dieťa, a to bez ohľadu na schopnosti, možnosti a majetkové pomery rodiča."
  },
  {
    "zakon": "36/2005/paragraf-78",
    "odpoved_vygenerovana": "Dohody a súdne rozhodnutia o výživnom je možné zmeniť, ak dôjde k zmene pomerov. Pri posudzovaní zmeny pomerov sa vždy prihliada aj na vývoj životných nákladov."
  }
]
```

**True positives:** ["36/2005/paragraf-62", "36/2005/paragraf-75", "36/2005/paragraf-78"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: OK

**Question:** Moje vozidlo bolo namerané radarom v meste, ale auto šoféroval môj otec. Pokutu poslali mne ako držiteľovi vozidla. Musím ju zaplatiť?

**Expected Provisions:**
- 8/2009/paragraf-6a

**Model-Selected Provisions:**
- 8/2009/paragraf-6a

**Structured output:**

```json
[
  {
    "zakon": "8/2009/paragraf-6a",
    "odpoved_vygenerovana": "Držiteľ vozidla má zákonnú povinnosť zabezpečiť, aby pri prevádzkovaní jeho motorového vozidla boli dodržiavané pravidlá cestnej premávky. Táto povinnosť sa vzťahuje aj na dodržiavanie povolenej rýchlosti jazdy."
  }
]
```

**True positives:** ["8/2009/paragraf-6a"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 2 | Status: OK

**Question:** Dobrý deň, potreboval by som pomôcť s pokutou, ktorá mi prišla domov. Údajne som vyšiel na diaľnicu bez diaľničnej známky a domov mi prišla pokuta. Ja som si však diaľničnú známku kúpil. Bohužiaľ, pri jej zadávaní musela nastať chyba a diaľničnú známku som kúpil na iné evidenčné číslo. Je možné reklamovať takto zakúpenú diaľničnú známku aby som sa vyhol pokute alebo ako mám postupovať. Ďakujem.

**Expected Provisions:**
- 488/2013/paragraf-10
- 488/2013/paragraf-13

**Model-Selected Provisions:**
- 488/2013/paragraf-10
- 488/2013/paragraf-13

**Structured output:**

```json
[
  {
    "zakon": "488/2013/paragraf-10",
    "odpoved_vygenerovana": "Zákon definuje, že priestupku sa dopustí vodič, ktorý použije vymedzené úseky diaľnic bez toho, aby mal uhradenú diaľničnú známku. Pre spáchanie priestupku je teda rozhodujúce samotné použitie diaľnice bez platnej úhrady."
  },
  {
    "zakon": "488/2013/paragraf-13",
    "odpoved_vygenerovana": "Proti doručenému rozkazu o uložení pokuty môže prevádzkovateľ vozidla podať odpor. Lehota na podanie odporu je 15 dní odo dňa doručenia a podáva sa na okresnom úrade, ktorý rozkaz vydal. Odpor musí byť odôvodnený, pričom je potrebné uviesť rozhodujúce skutočnosti a označiť dôkazy na preukázanie svojich tvrdení."
  }
]
```

**True positives:** ["488/2013/paragraf-10", "488/2013/paragraf-13"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---
