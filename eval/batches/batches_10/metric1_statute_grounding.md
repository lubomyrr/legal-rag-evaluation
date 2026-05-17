# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 3
False positives: 0
False negatives: 1
Precision: 1.000
Recall: 0.750
F1: 0.857

## ID 0 | Status: OK

**Question:** Dobrý deň, chcem sa spýtať na krádež. Ak si v obchode vezmem nejakú drobnosť, napríklad žuvačky alebo čokoládu, ale hneď ma pri tom chytia, stále mi hrozí trest? Počul som, že ak je to len do určitej sumy, tak je to len priestupok. Kde je hranica medzi priestupkom a trestným činom a aké môžu byť následky?

**Expected Provisions:**
- 300/2005/paragraf-212
- 372/1990/paragraf-50

**Model-Selected Provisions:**
- 300/2005/paragraf-212
- 372/1990/paragraf-50

**Structured output:**

```json
[
  {
    "zakon": "300/2005/paragraf-212",
    "odpoved_vygenerovana": "Trestného činu krádeže sa dopustí ten, kto si prisvojí cudziu vec, zmocní sa jej a spôsobí tak malú škodu. Za trestný čin sa to považuje aj vtedy, ak je skutok spáchaný napríklad vlámaním alebo na veci, ktorú má iná osoba na sebe alebo pri sebe."
  },
  {
    "zakon": "372/1990/paragraf-50",
    "odpoved_vygenerovana": "Priestupku proti majetku sa dopustí ten, kto úmyselne spôsobí škodu na cudzom majetku krádežou. Za takýto priestupok možno uložiť pokutu do výšky 1 400 eur. V prípade opakovaného spáchania priestupku v priebehu 12 mesiacov môže byť uložená pokuta až do výšky 2 000 eur."
  }
]
```

**True positives:** ["300/2005/paragraf-212", "372/1990/paragraf-50"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: EMPTY_RESULT

**Question:** Potrebujem právnu poradu ohľadom spáchania trestného činu v podmienke. Môj brat, ktorý bol nedávno odsúdený na podmienečný trest, je teraz obvinený z nového trestného činu. Chcel by som vedieť, aké môžu byť právne dôsledky jeho konania. Ako ovplyvní tento nový trestný čin jeho aktuálnu podmienečnú dobu a aké opatrenia by mohol súd prijať?

**Expected Provisions:**
- 300/2005/paragraf-51

**Model-Selected Provisions:**
- none

**Structured output:**

```json
[]
```

**True positives:** []
**False positives:** []
**False negatives:** ["300/2005/paragraf-51"]

**Verdict:** missing annotated citations

---

## ID 2 | Status: OK

**Question:** Potrebovala by som poradiť ohľadom premeny trestu. Môj brat bol nedávno odsúdený na trest odňatia slobody a zvažujeme možnosť požiadať o jeho premenu na alternatívny trest – domáce väzenie alebo podmienečné prepustenie. Aké sú prosím podmienky a proces pre takúto zmenu trestu? Podľa čoho sa určuje vhodnosť odsúdenej osoby?

**Expected Provisions:**
- 300/2005/paragraf-66

**Model-Selected Provisions:**
- 300/2005/paragraf-66

**Structured output:**

```json
[
  {
    "zakon": "300/2005/paragraf-66",
    "odpoved_vygenerovana": "Súd môže odsúdeného podmienečne prepustiť na slobodu, ak odsúdený svojím správaním a plnením povinností vo výkone trestu preukázal polepšenie a možno od neho očakávať, že bude viesť riadny život. Podmienkou je tiež výkon určitej časti trestu, ktorá je spravidla polovica pri prečine a dve tretiny pri zločine. Pri rozhodovaní súd prihliadne aj na povahu spáchaného trestného činu."
  }
]
```

**True positives:** ["300/2005/paragraf-66"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---
