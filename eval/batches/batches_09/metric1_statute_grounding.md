# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 6
False positives: 1
False negatives: 3
Precision: 0.857
Recall: 0.667
F1: 0.750

## ID 0 | Status: OK

**Question:** Na internete som sa dočítal, že ak kataster nezapíše vlastnícke právo v lehote 30 dní, mám možnosť žiadať o vrátenie správneho poplatku. Je to pravda? Ako mám postupovať, aby mi správny poplatok bol vrátený a na koho sa mám v tejto veci obrátiť?

**Expected Provisions:**
- 145/1995/paragraf-10
- 162/1995/paragraf-22
- 162/1995/paragraf-29
- 162/1995/paragraf-32

**Model-Selected Provisions:**
- 145/1995/paragraf-10
- 162/1995/paragraf-32

**Structured output:**

```json
[
  {
    "zakon": "145/1995/paragraf-10",
    "odpoved_vygenerovana": "Správny orgán rozhodne o vrátení správneho poplatku v plnej výške, ak sa úkon alebo konanie nevykonalo v zákonom stanovenej lehote bez zavinenia poplatníka. Lehota sa považuje za zachovanú, ak správny orgán v jej posledný deň odovzdá vybavenie na poštovú prepravu, odošle ho elektronicky alebo ho odovzdá priamo poplatníkovi."
  },
  {
    "zakon": "162/1995/paragraf-32",
    "odpoved_vygenerovana": "Okresný úrad má na rozhodnutie o návrhu na vklad do katastra nehnuteľností lehotu 30 dní odo dňa doručenia návrhu. V osobitných prípadoch, ako napríklad pri zmluve vo forme notárskej zápisnice alebo pri žiadosti o urýchlené konanie, sú lehoty kratšie."
  }
]
```

**True positives:** ["145/1995/paragraf-10", "162/1995/paragraf-32"]
**False positives:** []
**False negatives:** ["162/1995/paragraf-22", "162/1995/paragraf-29"]

**Verdict:** missing annotated citations

---

## ID 1 | Status: OK

**Question:** Môj partner ma psychicky ponižuje, vyhráža sa mi a kontroluje mi telefón. Je to už týranie, aj keď ma neudrel?

**Expected Provisions:**
- 300/2005/paragraf-127
- 300/2005/paragraf-208
- 372/1990/paragraf-127

**Model-Selected Provisions:**
- 300/2005/paragraf-127
- 300/2005/paragraf-208

**Structured output:**

```json
[
  {
    "zakon": "300/2005/paragraf-208",
    "odpoved_vygenerovana": "Trestného činu týrania blízkej osoby sa dopustí ten, kto jej spôsobí fyzické alebo psychické utrpenie. Zákon ako príklady foriem psychického utrpenia uvádza ponižovanie, pohŕdavé zaobchádzanie, neustále sledovanie, vyhrážanie, vyvolávanie strachu alebo stresu, či iné správanie, ktoré ohrozuje psychické zdravie."
  },
  {
    "zakon": "300/2005/paragraf-127",
    "odpoved_vygenerovana": "Pre účely trestného činu týrania sa za blízku osobu považuje okrem iných aj druh, bývalý druh alebo osoba, ktorá s páchateľom žije alebo žila v spoločnej domácnosti."
  }
]
```

**True positives:** ["300/2005/paragraf-127", "300/2005/paragraf-208"]
**False positives:** []
**False negatives:** ["372/1990/paragraf-127"]

**Verdict:** missing annotated citations

---

## ID 2 | Status: OK

**Question:** Dobrý deň. Bol som bol prichytený pri šoférovaní pod vplyvom alkoholu, ale bez nehody. Čo mi za tento čin hrozí?

**Expected Provisions:**
- 300/2005/paragraf-289
- 372/1990/paragraf-22

**Model-Selected Provisions:**
- 300/2005/paragraf-289
- 300/2005/paragraf-51
- 372/1990/paragraf-22

**Structured output:**

```json
[
  {
    "zakon": "372/1990/paragraf-22",
    "odpoved_vygenerovana": "Vedenie vozidla v čase po požití alkoholu, keď sa ešte nachádza v organizme, je priestupkom proti bezpečnosti a plynulosti cestnej premávky. Za tento priestupok možno uložiť pokutu od 150 eur do 800 eur a zákaz činnosti do troch rokov."
  },
  {
    "zakon": "300/2005/paragraf-289",
    "odpoved_vygenerovana": "Vykonávanie činnosti, pri ktorej by mohol byť ohrozený život alebo zdravie ľudí, v stave vylučujúcom spôsobilosť privodenom návykovou látkou, je trestným činom. Páchateľovi takéhoto činu hrozí trest odňatia slobody až na jeden rok."
  },
  {
    "zakon": "300/2005/paragraf-51",
    "odpoved_vygenerovana": "Súd môže v rámci trestného konania uložiť páchateľovi aj rôzne povinnosti. Medzi takéto povinnosti patrí napríklad príkaz podrobiť sa liečeniu závislosti od návykových látok."
  }
]
```

**True positives:** ["300/2005/paragraf-289", "372/1990/paragraf-22"]
**False positives:** ["300/2005/paragraf-51"]
**False negatives:** []

**Verdict:** extra citation

---
