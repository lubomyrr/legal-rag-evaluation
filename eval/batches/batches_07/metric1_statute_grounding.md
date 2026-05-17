# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 6
False positives: 1
False negatives: 1
Precision: 0.857
Recall: 0.857
F1: 0.857

## ID 0 | Status: OK

**Question:** Môže maloleté dieťa, ktoré vlastní nehnuteľnosť, zastupovať vo veciach danej nehnuteľnosti aj niekto iný okrem zákonného zástupcu – rodiča?

**Expected Provisions:**
- 36/2005/paragraf-31
- 36/2005/paragraf-33
- 40/1964/paragraf-30

**Model-Selected Provisions:**
- 36/2005/paragraf-31
- 36/2005/paragraf-33
- 40/1964/paragraf-30

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-31",
    "odpoved_vygenerovana": "Rodič nemôže zastupovať svoje maloleté dieťa v právnych úkonoch, pri ktorých by mohlo dôjsť k rozporu záujmov medzi nimi. V takom prípade súd ustanoví dieťaťu takzvaného kolízneho opatrovníka, ktorý ho bude v konaní alebo pri danom právnom úkone zastupovať."
  },
  {
    "zakon": "36/2005/paragraf-33",
    "odpoved_vygenerovana": "Ak sú záujmy maloletého dieťaťa súvisiace so spravovaním jeho majetku ohrozené a rodičia neurobili alebo nie sú schopní urobiť vhodné opatrenia, súd môže ustanoviť majetkového opatrovníka. Tento opatrovník je potom zodpovedný za správu majetku dieťaťa v rozsahu určenom súdom."
  },
  {
    "zakon": "40/1964/paragraf-30",
    "odpoved_vygenerovana": "Ak dôjde k stretu záujmov zákonného zástupcu so záujmami zastúpeného, alebo k stretu záujmov osôb zastúpených tým istým zákonným zástupcom, súd ustanoví osobitného zástupcu."
  }
]
```

**True positives:** ["36/2005/paragraf-31", "36/2005/paragraf-33", "40/1964/paragraf-30"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: OK

**Question:** Potrebovala by som právnu radu týkajúcu sa výživného v prípade, keď je jeden z rodičov zdravotne ťažko postihnutý (ZŤP). Rozvádzame sa a môj partner, ktorý má status ZŤP, by mal byť zákonným platiteľom výživného na naše spoločné deti. Chcela by som vedieť, ako jeho zdravotný stav ovplyvní jeho povinnosť platiť výživné.

**Expected Provisions:**
- 36/2005/paragraf-62

**Model-Selected Provisions:**
- 36/2005/paragraf-62
- 36/2005/paragraf-75

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-62",
    "odpoved_vygenerovana": "Vyživovacia povinnosť rodičov voči deťom je zákonná povinnosť, ktorá trvá, kým deti nie sú schopné sa samé živiť. Každý rodič je povinný plniť túto povinnosť v minimálnom rozsahu 30 % zo sumy životného minima na dieťa, a to bez ohľadu na jeho schopnosti, možnosti a majetkové pomery."
  },
  {
    "zakon": "36/2005/paragraf-75",
    "odpoved_vygenerovana": "Pri určovaní konkrétnej výšky výživného súd prihliada na odôvodnené potreby dieťaťa a zároveň na schopnosti, možnosti a majetkové pomery povinného rodiča. Súd teda zohľadní všetky okolnosti na strane povinného rodiča, ktoré môžu ovplyvňovať jeho schopnosť prispievať na výživu."
  }
]
```

**True positives:** ["36/2005/paragraf-62"]
**False positives:** ["36/2005/paragraf-75"]
**False negatives:** []

**Verdict:** extra citation

---

## ID 2 | Status: OK

**Question:** Obraciam sa na vás s otázkou týkajúcou sa zmeny priezviska dieťaťa bez súhlasu otca. Som matkou šesťročného syna, ktorý má priezvisko svojho biologického otca. Od synovho narodenia sme s otcom v minimálnom kontakte, o syna takmer vôbec nestará. Teraz, keď žijem s novým partnerom a mám ďalšie deti, chcela by som, aby mal môj syn rovnaké priezvisko ako zvyšok rodiny. Je možné zmeniť priezvisko syna bez súhlasu biologického otca, vzhľadom na jeho nezáujem o dieťa? Aké sú právne možnosti a postupy v tejto situácii?

**Expected Provisions:**
- 36/2005/paragraf-4
- 36/2005/paragraf-6
- 36/2005/paragraf-8

**Model-Selected Provisions:**
- 36/2005/paragraf-6
- 36/2005/paragraf-8

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-6",
    "odpoved_vygenerovana": "Ak si rodič, ktorého priezvisko má maloleté dieťa, zmení svoje priezvisko, táto zmena sa vzťahuje aj na dieťa. Podmienkou pre takúto zmenu priezviska dieťaťa je však súhlas druhého rodiča."
  },
  {
    "zakon": "36/2005/paragraf-8",
    "odpoved_vygenerovana": "Zmena priezviska maloletého dieťaťa sa nepovolí, ak by bola v rozpore s jeho záujmami. Každá žiadosť o zmenu priezviska dieťaťa sa posudzuje s ohľadom na to, či je v súlade s najlepším záujmom dieťaťa."
  }
]
```

**True positives:** ["36/2005/paragraf-6", "36/2005/paragraf-8"]
**False positives:** []
**False negatives:** ["36/2005/paragraf-4"]

**Verdict:** missing annotated citations

---
