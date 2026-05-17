# Metric 3 - Expected Alignment

## Summary

Evaluated questions: 2
Evaluated model-selected provisions: 3
Mean question score: 0.875
Mean provision score: 0.833
Skipped questions: 1
Metrika 3 porovnava text modelu s relevantnym vyrezom expertnej expected odpovede pre ten isty pravny predpis. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Dobrý deň, chcem sa spýtať na krádež. Ak si v obchode vezmem nejakú drobnosť, napríklad žuvačky alebo čokoládu, ale hneď ma pri tom chytia, stále mi hrozí trest? Počul som, že ak je to len do určitej sumy, tak je to len priestupok. Kde je hranica medzi priestupkom a trestným činom a aké môžu byť následky?

**Model-Selected Provisions:**
- 300/2005/paragraf-212
- 372/1990/paragraf-50

**Question score:** 0.750

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-212

**Text written by the model for this provision:**

```text
Trestného činu krádeže sa dopustí ten, kto si prisvojí cudziu vec, zmocní sa jej a spôsobí tak malú škodu. Za trestný čin sa to považuje aj vtedy, ak je skutok spáchaný napríklad vlámaním alebo na veci, ktorú má iná osoba na sebe alebo pri sebe.
```

**Extracted expected span:**

```text
V prípade, ak: hodnota odcudzenej veci je vyššia než 700,- EUR, čin je spáchaný vlámaním, bezprostredne po čine sa páchateľ pokúsi uchovať si vec násilím alebo hrozbou bezprostredného násilia, čin spácha na veci, ktorú má iný na sebe alebo pri sebe, vec je z úrody z pozemku, ktorý patrí do poľnohospodárskeho pôdneho fondu, alebo drevo nachádzajúce sa na lesnom pozemku, alebo ryba z rybníka s intenzívnym chovom, alebo čin spácha na veci, ktorej odber podlieha spoplatneniu na základe osobitného predpisu čin už nie je priestupkom, ale trestným činom krádeže podľa ***§ 212 ods. 1*** Trestného zákona (zákon č. 300/2005 Z. z.). Následkami trestného činu krádeže je napr. trest odňatia slobody až na dva roky (v základnej skutkovej podstate) a zápis v registri trestov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je v súlade s expertnou odpoveďou. Správne uvádza, že krádež sa stáva trestným činom buď pri spôsobení malej škody, alebo ak je spáchaná za špecifických okolností (vlámanie, krádež veci, ktorú má niekto pri sebe). Hoci model používa zákonný pojem "malá škoda" a neuvádza konkrétnu sumu ako expert, jadro právneho bodu je zachytené správne a vecne.

### Model-Selected Provision 2

**Provision:**
372/1990/paragraf-50

**Text written by the model for this provision:**

```text
Priestupku proti majetku sa dopustí ten, kto úmyselne spôsobí škodu na cudzom majetku krádežou. Za takýto priestupok možno uložiť pokutu do výšky 1 400 eur. V prípade opakovaného spáchania priestupku v priebehu 12 mesiacov môže byť uložená pokuta až do výšky 2 000 eur.
```

**Extracted expected span:**

```text
Ak je hodnota odcudzenej veci do 700,- EUR vrátane , ide o priestupok proti majetku podľa ***§ 50*** zákona č. 372/1990 Zb. o priestupkoch. Je dôležité podotknúť, že aj v prípade pokusu o odcudzenie je postih rovnaký. Sankciou za tento priestupok je najmä pokuta do 1.400,- EUR, v blokovom konaní do 500,- EUR a v rozkaznom konaní do 1.000,- EUR.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu je iba čiastočne v súlade s expertnou odpoveďou. Zhoda je v správne uvedenej výške pokuty (1 400 eur). Model však nespomína kľúčovú informáciu, ktorou je hodnotová hranica (do 700 eur), ktorá definuje skutok ako priestupok a odlišuje ho od trestného činu. Keďže práve táto hranica je jadrom otázky, jej absencia robí odpoveď modelu neúplnou. Jadro teda sedí len v časti o sankcii, ale chýba mu podstatná časť definície.

---

## ID 2 | Status: OK

**Question:** Potrebovala by som poradiť ohľadom premeny trestu. Môj brat bol nedávno odsúdený na trest odňatia slobody a zvažujeme možnosť požiadať o jeho premenu na alternatívny trest – domáce väzenie alebo podmienečné prepustenie. Aké sú prosím podmienky a proces pre takúto zmenu trestu? Podľa čoho sa určuje vhodnosť odsúdenej osoby?

**Model-Selected Provisions:**
- 300/2005/paragraf-66

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-66

**Text written by the model for this provision:**

```text
Súd môže odsúdeného podmienečne prepustiť na slobodu, ak odsúdený svojím správaním a plnením povinností vo výkone trestu preukázal polepšenie a možno od neho očakávať, že bude viesť riadny život. Podmienkou je tiež výkon určitej časti trestu, ktorá je spravidla polovica pri prečine a dve tretiny pri zločine. Pri rozhodovaní súd prihliadne aj na povahu spáchaného trestného činu.
```

**Extracted expected span:**

```text
Inštitút podmienečného prepustenia je upravený v ***§ 66 a nasl.*** Trestného zákona. Aplikuje sa v prípade, ak odsúdený plnením svojich povinností a svojím správaním preukázal polepšenie a dá sa od neho očakávať, že v budúcnosti povedie riadny život.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s expertne označenou časťou odpovede. Správne identifikuje kľúčové podmienky pre podmienečné prepustenie, a to preukázanie polepšenia odsúdeným a prognózu vedenia riadneho života. Model navyše správne dopĺňa ďalšie relevantné podmienky, ktoré síce nie sú v krátkej expertnej odpovedi, ale sú vecne správne a priamo súvisia s daným paragrafom (výkon časti trestu). Keďže jadro informácie je zhodné a doplňujúce informácie sú správne a relevantné, udeľujem skóre 1.0.

---
