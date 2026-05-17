# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 2
False positives: 4
False negatives: 2
Precision: 0.333
Recall: 0.500
F1: 0.400

## ID 0 | Status: OK

**Question:** Obraciam sa na vás s otázkou týkajúcou sa odstúpenia od kúpnej zmluvy. Nedávno som uzavrela kúpnu zmluvu na kúpu nehnuteľnosti, ale zistila som niekoľko problémov, ktoré neboli vopred uvedené.

**Expected Provisions:**
- 40/1964/paragraf-596
- 40/1964/paragraf-597

**Model-Selected Provisions:**
- 40/1964/paragraf-597

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-597",
    "odpoved_vygenerovana": "Kupujúci má právo odstúpiť od zmluvy, ak ho predávajúci ubezpečil, že vec má určité vlastnosti, alebo že je bez vád, a toto ubezpečenie sa neskôr ukáže ako nepravdivé. Toto právo na odstúpenie sa vzťahuje aj na situáciu, keď sa nepravdivým ukáže ubezpečenie o vlastnostiach, ktoré si kupujúci vopred vymienil."
  }
]
```

**True positives:** ["40/1964/paragraf-597"]
**False positives:** []
**False negatives:** ["40/1964/paragraf-596"]

**Verdict:** missing annotated citations (50.0% matched)

---

## ID 1 | Status: OK

**Question:** Potrebovala by som sa poradiť ohľadom nároku na majetok v prípade, že dlhodobo žijem s mojim priateľom ako družka. Sme spolu už desať rokov, ale nie sme zosobášení. Počas nášho spolužitia sme nadobudli určitý majetok, vrátane domu a niekoľkých cenností. Chcela by som vedieť, aký nárok mám na tento majetok v prípade rozchodu alebo úmrtia môjho partnera, keďže sme nikdy neboli manželmi.

**Expected Provisions:**
- 40/1964/paragraf-130

**Model-Selected Provisions:**
- 40/1964/paragraf-116
- 40/1964/paragraf-141
- 40/1964/paragraf-143
- 40/1964/paragraf-451

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-143",
    "odpoved_vygenerovana": "Bezpodielové spoluvlastníctvo manželov je majetkový režim, ktorý vzniká len medzi manželmi. Vzťahuje sa na veci nadobudnuté ktorýmkoľvek z nich počas trvania manželstva, s určitými zákonnými výnimkami."
  },
  {
    "zakon": "40/1964/paragraf-141",
    "odpoved_vygenerovana": "Spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. Ak je predmetom spoluvlastníctva nehnuteľnosť, zákon pre takúto dohodu vyžaduje písomnú formu."
  },
  {
    "zakon": "40/1964/paragraf-116",
    "odpoved_vygenerovana": "Blízkou osobou je okrem príbuzných a manžela aj iná osoba v rodinnom alebo obdobnom pomere. Musí však platiť, že by ujmu, ktorú utrpela jedna z nich, druhá dôvodne pociťovala ako vlastnú ujmu. Tento status môže byť dôležitý napríklad v dedičskom konaní."
  },
  {
    "zakon": "40/1964/paragraf-451",
    "odpoved_vygenerovana": "Kto sa na úkor iného bezdôvodne obohatí, je povinný toto obohatenie vydať. Za bezdôvodné obohatenie sa považuje majetkový prospech získaný plnením bez právneho dôvodu, z neplatného právneho úkonu alebo z právneho dôvodu, ktorý odpadol."
  }
]
```

**True positives:** []
**False positives:** ["40/1964/paragraf-116", "40/1964/paragraf-141", "40/1964/paragraf-143", "40/1964/paragraf-451"]
**False negatives:** ["40/1964/paragraf-130"]

**Verdict:** partial match (0.0% matched)

---

## ID 2 | Status: OK

**Question:** Zamestnávateľ mi znížil mzdu bez môjho súhlasu. Môže to urobiť jednostranne?

**Expected Provisions:**
- 311/2001/paragraf-54

**Model-Selected Provisions:**
- 311/2001/paragraf-54

**Structured output:**

```json
[
  {
    "zakon": "311/2001/paragraf-54",
    "odpoved_vygenerovana": "Dohodnutý obsah pracovnej zmluvy, ktorého súčasťou sú aj mzdové podmienky, je možné zmeniť iba vtedy, ak sa na tom zamestnávateľ a zamestnanec dohodnú. Zamestnávateľ je povinný takúto zmenu pracovnej zmluvy vyhotoviť písomne."
  }
]
```

**True positives:** ["311/2001/paragraf-54"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---
