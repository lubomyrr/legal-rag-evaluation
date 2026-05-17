# Metric 1 - Statute Grounding

## Summary

Questions with gold annotations: 3
True positives: 3
False positives: 1
False negatives: 3
Precision: 0.750
Recall: 0.500
F1: 0.600

## ID 0 | Status: OK

**Question:** Dobrý deň. Chcem sa, prosím Vás, spýtať, ako je to s majetkom do svadby a po svadbe. Je to tak, že čo nadobudnem do svadby, na to žena nemá nárok?

**Expected Provisions:**
- 40/1964/paragraf-143
- 40/1964/paragraf-150

**Model-Selected Provisions:**
- 40/1964/paragraf-143
- 40/1964/paragraf-150

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-143",
    "odpoved_vygenerovana": "Do bezpodielového spoluvlastníctva manželov patrí všetko, čo nadobudol niektorý z manželov za trvania manželstva. Nevzťahuje sa to však na veci získané dedičstvom, darom, veci slúžiace osobnej potrebe alebo výkonu povolania jedného z manželov, ani na veci vydané v reštitúcii."
  },
  {
    "zakon": "40/1964/paragraf-150",
    "odpoved_vygenerovana": "Pri vyporiadaní bezpodielového spoluvlastníctva má každý z manželov právo požadovať, aby sa mu uhradilo to, čo zo svojho výlučného majetku vynaložil na spoločný majetok. Zároveň je každý z manželov povinný nahradiť to, čo sa zo spoločného majetku vynaložilo na jeho ostatný (výlučný) majetok."
  }
]
```

**True positives:** ["40/1964/paragraf-143", "40/1964/paragraf-150"]
**False positives:** []
**False negatives:** []

**Verdict:** exact match

---

## ID 1 | Status: OK

**Question:** Potreboval by som sa poradiť ohľadom vydania vecí alebo vrátenia zaplatených splátok. S bývalou partnerkou sme si počas spolužitia zakúpili viacero vecí na splátky, na ktoré som prispel aj ja. Po našom rozchode si väčšinu týchto vecí vzala ona. Chcel by som vedieť, aké mám práva na vrátenie časti zaplatených splátok alebo na vydanie týchto vecí. Ako môžem postupovať, aby som dosiahol spravodlivé vyrovnanie?

**Expected Provisions:**
- 40/1964/paragraf-141
- 40/1964/paragraf-451

**Model-Selected Provisions:**
- 40/1964/paragraf-141

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-141",
    "odpoved_vygenerovana": "Spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. Ak je predmetom spoluvlastníctva nehnuteľnosť, dohoda musí byť písomná. V prípade, že dohoda o zrušení a vyporiadaní spoluvlastníctva nemala písomnú formu, je každý zo spoluvlastníkov povinný vydať ostatným na požiadanie písomné potvrdenie o spôsobe vyporiadania."
  }
]
```

**True positives:** ["40/1964/paragraf-141"]
**False positives:** []
**False negatives:** ["40/1964/paragraf-451"]

**Verdict:** missing annotated citations (50.0% matched)

---

## ID 2 | Status: OK

**Question:** Potrebujem právnu poradu týkajúcu sa predaja pozemku, ktorý má viacerých vlastníkov. Spolu s mojimi štyrmi súrodencami som spoluvlastníkom pozemku, ktorý sme zdedili po našich rodičoch. Dvaja z nás by teraz chceli ten pozemok predať. Chcela by som vedieť, aké sú právne požiadavky a postupy pre predaj pozemku, keď má viacerých vlastníkov.

**Expected Provisions:**
- 40/1964/paragraf-116
- 40/1964/paragraf-603

**Model-Selected Provisions:**
- 40/1964/paragraf-141

**Structured output:**

```json
[
  {
    "zakon": "40/1964/paragraf-141",
    "odpoved_vygenerovana": "Spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. Ak je predmetom spoluvlastníctva nehnuteľnosť, zákon vyžaduje, aby takáto dohoda mala písomnú formu. Každý spoluvlastník je tiež povinný na požiadanie vydať ostatným písomné potvrdenie o spôsobe vyporiadania."
  }
]
```

**True positives:** []
**False positives:** ["40/1964/paragraf-141"]
**False negatives:** ["40/1964/paragraf-116", "40/1964/paragraf-603"]

**Verdict:** partial match (0.0% matched)

---
