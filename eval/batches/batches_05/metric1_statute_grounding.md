# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 5
False positives: 1
False negatives: 0
Precision: 0.833
Recall: 1.000
F1: 0.909

## ID 0 | Status: OK

**Question:** Dobrý deň, zamestnávateľ mi oznámil, že sa ruší moje pracovné miesto. Na čo mám nárok od zamestnávateľa v takejto situácii?

**Expected Provisions:**
- 311/2001/paragraf-63
- 311/2001/paragraf-64
- 311/2001/paragraf-76

**Model-Selected Provisions:**
- 311/2001/paragraf-63
- 311/2001/paragraf-64
- 311/2001/paragraf-76

**Structured output:**

```json
[
  {
    "zakon": "311/2001/paragraf-63",
    "odpoved_vygenerovana": "Zamestnávateľ môže dať zamestnancovi výpoveď, ak sa zamestnanec stane nadbytočným na základe písomného rozhodnutia o organizačných zmenách, napríklad o znížení stavu zamestnancov. Pred podaním výpovede z tohto dôvodu je zamestnávateľ povinný zamestnancovi ponúknuť inú pre neho vhodnú prácu, ak má takúto prácu k dispozícii."
  },
  {
    "zakon": "311/2001/paragraf-76",
    "odpoved_vygenerovana": "Zamestnancovi, s ktorým zamestnávateľ skončí pracovný pomer výpoveďou alebo dohodou z dôvodu nadbytočnosti, patrí odstupné. Výška odstupného závisí od dĺžky trvania pracovného pomeru a pohybuje sa od jedného až po päťnásobok priemerného mesačného zárobku. Odstupné je vyplatené po skončení pracovného pomeru v najbližšom výplatnom termíne, pokiaľ sa zamestnávateľ a zamestnanec nedohodnú inak."
  },
  {
    "zakon": "311/2001/paragraf-64",
    "odpoved_vygenerovana": "Zákonník práce ustanovuje ochranné doby, počas ktorých zamestnávateľ nesmie dať zamestnancovi výpoveď, napríklad počas práceneschopnosti, tehotenstva alebo rodičovskej dovolenky. Tento zákaz výpovede sa však neuplatní, ak sa zamestnávateľ alebo jeho časť zrušuje."
  }
]
```

**True positives:** ["311/2001/paragraf-63", "311/2001/paragraf-64", "311/2001/paragraf-76"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: OK

**Question:** Dobrý deň, zamestnávateľa som požiadal o dovolenku na budúci týždeň, nakoľko by som chcel ísť na výlet s rodinou. Zamestnávateľ mi však odmietol dovolenku poskytnúť. Má na to právo alebo si môže dovolenku vybrať aj napriek tomu?

**Expected Provisions:**
- 311/2001/paragraf-111

**Model-Selected Provisions:**
- 311/2001/paragraf-111

**Structured output:**

```json
[
  {
    "zakon": "311/2001/paragraf-111",
    "odpoved_vygenerovana": "Čerpanie dovolenky určuje zamestnávateľ po prerokovaní so zamestnancom a podľa plánu dovoleniek. Pri rozhodovaní o termíne dovolenky je potrebné prihliadať na úlohy zamestnávateľa, ako aj na oprávnené záujmy zamestnanca. Zamestnávateľ je povinný oznámiť zamestnancovi určené čerpanie dovolenky aspoň 14 dní vopred, ak sa nedohodnú na kratšej dobe."
  }
]
```

**True positives:** ["311/2001/paragraf-111"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 2 | Status: OK

**Question:** Chcel by som sa informovať ohľadom obrany proti výpovedi z práce. Nedávno som dostal výpoveď zo zamestnania, ktorú považujem za neoprávnenú a neodôvodnenú. Zaujíma ma, aké mám možnosti a akým spôsobom sa môžem brániť proti tejto výpovedi.

**Expected Provisions:**
- 311/2001/paragraf-63

**Model-Selected Provisions:**
- 311/2001/paragraf-63
- 311/2001/paragraf-64

**Structured output:**

```json
[
  {
    "zakon": "311/2001/paragraf-63",
    "odpoved_vygenerovana": "Zamestnávateľ môže dať zamestnancovi výpoveď iba z dôvodov presne stanovených v zákone. Medzi tieto dôvody patrí napríklad zrušenie alebo premiestnenie zamestnávateľa, nadbytočnosť zamestnanca z dôvodu organizačných zmien, alebo zdravotné dôvody na strane zamestnanca. Výpoveď je možná aj pri nespĺňaní predpokladov, neuspokojivom plnení úloh alebo pri porušení pracovnej disciplíny za stanovených podmienok."
  },
  {
    "zakon": "311/2001/paragraf-64",
    "odpoved_vygenerovana": "Zákonník práce ustanovuje tzv. ochrannú dobu, počas ktorej zamestnávateľ nesmie dať zamestnancovi výpoveď. Takouto dobou je napríklad obdobie dočasnej práceneschopnosti, tehotenstva, materskej, otcovskej alebo rodičovskej dovolenky. Zákon zároveň definuje aj výnimky, kedy sa tento zákaz výpovede neuplatňuje."
  }
]
```

**True positives:** ["311/2001/paragraf-63"]
**False positives:** ["311/2001/paragraf-64"]
**False negatives:** []

**Verdict:** extra citation

---
