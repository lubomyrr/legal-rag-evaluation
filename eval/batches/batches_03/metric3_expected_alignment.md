# Metric 3 - Expected Alignment

## Summary

Evaluated questions: 2
Evaluated model-selected provisions: 3
Mean question score: 0.625
Mean provision score: 0.667
Skipped questions: 1
Metrika 3 porovnava text modelu s relevantnym vyrezom expertnej expected odpovede pre ten isty pravny predpis. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Dobrý deň. Chcem sa, prosím Vás, spýtať, ako je to s majetkom do svadby a po svadbe. Je to tak, že čo nadobudnem do svadby, na to žena nemá nárok?

**Model-Selected Provisions:**
- 40/1964/paragraf-143
- 40/1964/paragraf-150

**Question score:** 0.750

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-143

**Text written by the model for this provision:**

```text
Do bezpodielového spoluvlastníctva manželov patrí všetko, čo nadobudol niektorý z manželov za trvania manželstva. Nevzťahuje sa to však na veci získané dedičstvom, darom, veci slúžiace osobnej potrebe alebo výkonu povolania jedného z manželov, ani na veci vydané v reštitúcii.
```

**Extracted expected span:**

```text
Podľa ***§ 143*** Občianskeho zákonníka v BSM je všetko, čo môže byť predmetom vlastníctva a čo nadobudol niektorý z manželov za trvania manželstva, s výnimkou vecí získaných dedičstvom alebo darom, ako aj vecí, ktoré podľa svojej povahy slúžia osobnej potrebe alebo výkonu povolania len jedného z manželov, a vecí vydaných v rámci predpisov o reštitúcii majetku jednému z manželov, ktorý mal vydanú vec vo vlastníctve pred uzavretím manželstva alebo ktorému bola vec vydaná ako právnemu nástupcovi pôvodného vlastníka.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecne zhodný s expertnou odpoveďou. Správne definuje, čo patrí do bezpodielového spoluvlastníctva manželov (BSM) – majetok nadobudnutý počas manželstva – a zároveň vymenúva všetky zákonné výnimky (dedičstvo, dar, veci osobnej potreby/výkonu povolania, reštitúcia). Mierne zjednodušenie pri reštitúcii je v poriadku, keďže jadro informácie zostalo zachované.

### Model-Selected Provision 2

**Provision:**
40/1964/paragraf-150

**Text written by the model for this provision:**

```text
Pri vyporiadaní bezpodielového spoluvlastníctva má každý z manželov právo požadovať, aby sa mu uhradilo to, čo zo svojho výlučného majetku vynaložil na spoločný majetok. Zároveň je každý z manželov povinný nahradiť to, čo sa zo spoločného majetku vynaložilo na jeho ostatný (výlučný) majetok.
```

**Extracted expected span:**

```text
Podľa ***§ 150*** Občianskeho zákonníka pri vyporiadaní sa vychádza z toho, že podiely oboch manželov sú rovnaké. Každý z manželov je oprávnený požadovať, aby sa mu uhradilo, čo zo svojho vynaložil na spoločný majetok, a je povinný nahradiť, čo sa zo spoločného majetku vynaložilo na jeho ostatný majetok. Ďalej sa prihliadne predovšetkým na potreby maloletých detí, na to, ako sa každý z manželov staral o rodinu, a na to, ako sa zaslúžil o nadobudnutie a udržanie spoločných vecí. Pri určení miery pričinenia treba vziať tiež zreteľ na starostlivosť o deti a na obstarávanie spoločnej domácnosti.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu je v súlade s expertnou odpoveďou iba čiastočne. Správne popisuje princíp, podľa ktorého si manželia pri vyporiadaní BSM navzájom uhrádzajú, čo investovali zo svojho výlučného majetku do spoločného a naopak. Model však nespomína ďalšie dôležité zásady vyporiadania, ktoré expert uvádza, ako napríklad rovnosť podielov, prihliadnutie na potreby detí či zásluhy o nadobudnutie majetku. Keďže ide o významné opomenutie, text je neúplný a skóre je 0.5.

---

## ID 1 | Status: OK

**Question:** Potreboval by som sa poradiť ohľadom vydania vecí alebo vrátenia zaplatených splátok. S bývalou partnerkou sme si počas spolužitia zakúpili viacero vecí na splátky, na ktoré som prispel aj ja. Po našom rozchode si väčšinu týchto vecí vzala ona. Chcel by som vedieť, aké mám práva na vrátenie časti zaplatených splátok alebo na vydanie týchto vecí. Ako môžem postupovať, aby som dosiahol spravodlivé vyrovnanie?

**Model-Selected Provisions:**
- 40/1964/paragraf-141

**Question score:** 0.500

### Model-Selected Provision 1

**Provision:**
40/1964/paragraf-141

**Text written by the model for this provision:**

```text
Spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. Ak je predmetom spoluvlastníctva nehnuteľnosť, dohoda musí byť písomná. V prípade, že dohoda o zrušení a vyporiadaní spoluvlastníctva nemala písomnú formu, je každý zo spoluvlastníkov povinný vydať ostatným na požiadanie písomné potvrdenie o spôsobe vyporiadania.
```

**Extracted expected span:**

```text
Ak ste veci nadobudli spoločne a ste uvedení ako spoluvlastníci, môžete požiadať o zrušenie podielového spoluvlastníctva. Podľa ***§ 141*** Občianskeho zákonníka platí, že spoluvlastníci sa môžu dohodnúť o zrušení spoluvlastníctva a o vzájomnom vyporiadaní. Ak dohoda nie je možná, môže o tom rozhodnúť súd, ktorý prihliadne na veľkosť podielov a účelné využitie veci. Ak vec nie je možné fyzicky rozdeliť, môže ju súd prikázať jednému zo spoluvlastníkov
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu správne uvádza základnú myšlienku, že spoluvlastníci sa môžu dohodnúť na zrušení spoluvlastníctva a na vzájomnom vyporiadaní. V tom je zhoda s expertnou odpoveďou. Rozdiel je v tom, že model sa ďalej venuje formálnym náležitostiam dohody (písomná forma), zatiaľ čo expertná odpoveď spomína kľúčovú alternatívu pre prípad sporu – možnosť rozhodnutia súdom, ak dohoda nie je možná. Keďže text modelu zachytáva len časť právnej úpravy a vynecháva tú, ktorá je pre riešenie sporu zásadná (súdne vyporiadanie), ide o neúplnú informáciu. Preto je skóre 0.5.

---
