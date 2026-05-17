# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 4
False positives: 0
False negatives: 8
Precision: 1.000
Recall: 0.333
F1: 0.500

## ID 0 | Status: OK

**Question:** Chcem si založiť s.r.o., ale nerozumiem, aký je rozdiel medzi konateľom a spoločníkom. Môžem byť oboje?

**Expected Provisions:**
- 513/1991/paragraf-115
- 513/1991/paragraf-122
- 513/1991/paragraf-123
- 513/1991/paragraf-131
- 513/1991/paragraf-133
- 513/1991/paragraf-150
- 513/1991/paragraf-153
- 513/1991/paragraf-566

**Model-Selected Provisions:**
- 513/1991/paragraf-122
- 513/1991/paragraf-133

**Structured output:**

```json
[
  {
    "zakon": "513/1991/paragraf-133",
    "odpoved_vygenerovana": "Štatutárnym orgánom spoločnosti s ručením obmedzeným je jeden alebo viac konateľov. Konateľov vymenúva valné zhromaždenie, pričom ich môže vybrať z radov spoločníkov alebo aj z iných fyzických osôb. Zákon teda pripúšťa, aby jedna osoba bola zároveň spoločníkom aj konateľom."
  },
  {
    "zakon": "513/1991/paragraf-122",
    "odpoved_vygenerovana": "Spoločníci si uplatňujú svoje práva, ktoré sa týkajú riadenia a kontroly činnosti spoločnosti, na valnom zhromaždení. Medzi ich práva patrí najmä možnosť žiadať od konateľov informácie o záležitostiach spoločnosti a nahliadať do jej dokladov."
  }
]
```

**True positives:** ["513/1991/paragraf-122", "513/1991/paragraf-133"]
**False positives:** []
**False negatives:** ["513/1991/paragraf-115", "513/1991/paragraf-123", "513/1991/paragraf-131", "513/1991/paragraf-150", "513/1991/paragraf-153", "513/1991/paragraf-566"]

**Verdict:** missing annotated citations (25.0% matched)

---

## ID 1 | Status: OK

**Question:** Dobrý deň. Približne pred mesiacom sme mali v spoločnosti zasadnutie valného zhromaždenia. Ostatní spoločníci schválili zmeny, s ktorými ja nesúhlasím a mám záujem sa voči ním brániť. Existujú nejaké limity alebo obmedzenia toho, voči akému uzneseniu mám možnosť sa brániť?

**Expected Provisions:**
- 40/1964/paragraf-127
- 40/1964/paragraf-132
- 513/1991/paragraf-131

**Model-Selected Provisions:**
- 513/1991/paragraf-131

**Structured output:**

```json
[
  {
    "zakon": "513/1991/paragraf-131",
    "odpoved_vygenerovana": "Spoločník môže podať na súd návrh na určenie neplatnosti uznesenia valného zhromaždenia, ak je toto uznesenie v rozpore so zákonom, spoločenskou zmluvou alebo stanovami. Súd však môže určiť neplatnosť uznesenia len vtedy, ak toto porušenie mohlo obmedziť práva spoločníka, ktorý sa určenia neplatnosti domáha."
  }
]
```

**True positives:** ["513/1991/paragraf-131"]
**False positives:** []
**False negatives:** ["40/1964/paragraf-127", "40/1964/paragraf-132"]

**Verdict:** missing annotated citations (33.3% matched)

---

## ID 2 | Status: OK

**Question:** Dobrý deň, chcel by som si založiť spoločnosť. Všetky dokumenty som si pripravil a zaslal na obchodný register. Moja spoločnosť však nebola založená, nakoľko som podanie neurobil elektronicky. Je možnosť založiť spoločnosť aj v papierovej forme alebo musím podanie uskutočniť iba elektronicky?

**Expected Provisions:**
- 530/2003/paragraf-5

**Model-Selected Provisions:**
- 530/2003/paragraf-5

**Structured output:**

```json
[
  {
    "zakon": "530/2003/paragraf-5",
    "odpoved_vygenerovana": "Návrh na zápis do obchodného registra, návrh na zápis zmeny údajov alebo návrh na výmaz údajov sa podáva výlučne elektronickými prostriedkami. Registrový súd na návrh podaný inou ako elektronickou formou, napríklad v listinnej podobe, neprihliada."
  }
]
```

**True positives:** ["530/2003/paragraf-5"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---
