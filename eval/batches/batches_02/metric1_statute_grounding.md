# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 3
False positives: 0
False negatives: 0
Precision: 1.000
Recall: 1.000
F1: 1.000

## ID 0 | Status: OK

**Question:** Dobrý deň, otec ma vydedil v závete s odôvodnením, že sme spolu roky nekomunikovali. Mám napriek tomu nárok na nejakú časť dedičstva ako neopomenuteľný dedič?

**Expected Provisions:**
- 40/1964/paragraf-469a

**Model-Selected Provisions:**
- 40/1964/paragraf-469a

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-469a",
    "odpoved_vygenerovana": "Zákon umožňuje poručiteľovi vydediť svojho potomka z presne stanovených dôvodov. Jedným z týchto dôvodov je, ak potomok o poručiteľa trvalo neprejavuje opravdivý záujem, ktorý by ako potomok mal prejavovať. V listine o vydedení musí byť dôvod vydedenia uvedený."
  }
]
```

**True positives:** ["40/1964/paragraf-469a"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: OK

**Question:** Dobrý deň. Mám problém s prenajímateľom, ktorý mi nechce vrátiť kauciu s odôvodnením, že v byte zostali drobné poškodenia. Má na to právo, ak ide o bežné opotrebovanie?

**Expected Provisions:**
- 40/1964/paragraf-682

**Model-Selected Provisions:**
- 40/1964/paragraf-682

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-682",
    "odpoved_vygenerovana": "Po skončení nájmu je nájomca povinný vrátiť prenajatú vec v stave, v akom ju prevzal, pričom sa prihliada na obvyklé opotrebenie. Toto ustanovenie znamená, že zákon rozlišuje medzi poškodením veci a jej bežným opotrebovaním, ktoré vzniká pri riadnom užívaní."
  }
]
```

**True positives:** ["40/1964/paragraf-682"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 2 | Status: COMPOSE_FAILED

**Question:** Dobrý deň. Už rok a pól riešim pred súdom vyporiadanie podielového a bezpodielového spoluvlastníctva s bývalou manželkou. V marci minulého roku sa dobrovoľne odsťahovala z domu, ktorý je na liste vlastníctva v podielovom spoluvlastníctve v pomere 1/2 môj a 1/2 jej. Ona teraz začala do domu chodiť vtedy, keď som tam ja neni a berie odtiaľ veci. Náklady okolo domu, čo sa týka vody, elektriny, plynu si platím sám, odkedy sa odsťahovala. Čítal som, že existuje zákon, že pokiaľ v tom dome nebýva a dobrovoľne sa odsťahovala (čo mi potvrdila správou), tak že nemôže zasahovať do môjho obydlia. Viete mi poradiť, či je momentálne v poriadku, že by som vymenil zámok a ak bude niečo chcieť, ja jej odomknem nech si zoberie, len nech mi do domu nechodí vtedy, keď som tam ja neni?

**Expected Provisions:**
- 300/2005/paragraf-194

**Model-Selected Provisions:**
- 300/2005/paragraf-194

**Structured output:**

```json
[
  {
    "zakon": "300/2005/paragraf-194",
    "odpoved_vygenerovana": "Trestný zákon definuje trestný čin porušovania domovej slobody, ktorého sa dopustí ten, kto neoprávnene vnikne do obydlia iného alebo sa v ňom neoprávnene zdržiava. Podmienkou trestnosti je teda neoprávnenosť takéhoto konania. Páchateľovi tohto trestného činu hrozí trest odňatia slobody, ktorého výška závisí od okolností spáchania."
  }
]
```

**True positives:** ["300/2005/paragraf-194"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---
