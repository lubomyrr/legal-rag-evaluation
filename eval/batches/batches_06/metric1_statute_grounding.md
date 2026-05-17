# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 2
True positives: 1
False positives: 2
False negatives: 1
Precision: 0.333
Recall: 0.500
F1: 0.400

## ID 1 | Status: OK

**Question:** Ak je jeden z manželov ťažko chorý a odkázaný na pomoc, musí mu druhý manžel po rozvode platiť výživné ako bývalému manželovi?

**Expected Provisions:**
- 36/2005/paragraf-72

**Model-Selected Provisions:**
- 36/2005/paragraf-72
- 36/2005/paragraf-75

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-72",
    "odpoved_vygenerovana": "Rozvedený manžel, ktorý nie je schopný sám sa živiť, môže od bývalého manžela žiadať príspevok na primeranú výživu. Súd môže príspevok priznať najdlhšie na päť rokov, no túto dobu môže výnimočne predĺžiť, ak rozvedený manžel nie je schopný sa sám živiť z objektívnych dôvodov, napríklad pre dlhodobo nepriaznivý zdravotný stav vyžadujúci sústavnú opateru."
  },
  {
    "zakon": "36/2005/paragraf-75",
    "odpoved_vygenerovana": "Pri rozhodovaní o výživnom súd prihliada na odôvodnené potreby oprávneného. Zároveň posudzuje schopnosti, možnosti a majetkové pomery povinného, a to aj v prípade, ak sa bez dôležitého dôvodu vzdal výhodnejšieho zárobku alebo podstupuje neprimerané majetkové riziká."
  }
]
```

**True positives:** ["36/2005/paragraf-72"]
**False positives:** ["36/2005/paragraf-75"]
**False negatives:** []

**Verdict:** extra citation

---

## ID 2 | Status: COMPOSE_FAILED

**Question:** Dobrý deň, chcel by som sa informovať ohľadom vyživovacej povinnosti voči plnoletému synovi. Doteraz som výživné platil matke na účet, ktorý mi oznámila. Dozvedel som sa však, že od dovŕšenia plnoletosti by som mal výživné platiť synovi a nie matke. Je to pravda alebo musím platiť výživné tak ako doteraz.

**Expected Provisions:**
- 300/2005/paragraf-207

**Model-Selected Provisions:**
- 36/2005/paragraf-62

**Structured output:**

```json
[
  {
    "zakon": "36/2005/paragraf-62",
    "odpoved_vygenerovana": "Zákon ustanovuje, že vyživovacia povinnosť rodičov voči deťom trvá až do času, kým deti nie sú schopné samé sa živiť. Každý rodič je povinný plniť túto povinnosť v minimálnom zákonom stanovenom rozsahu."
  }
]
```

**True positives:** []
**False positives:** ["36/2005/paragraf-62"]
**False negatives:** ["300/2005/paragraf-207"]

**Verdict:** partial match

---
