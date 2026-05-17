# Metric 3 - Expected Alignment

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 6
Mean question score: 0.667
Mean provision score: 0.667
Skipped questions: 0
Metrika 3 porovnava text modelu s relevantnym vyrezom expertnej expected odpovede pre ten isty pravny predpis. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Na internete som sa dočítal, že ak kataster nezapíše vlastnícke právo v lehote 30 dní, mám možnosť žiadať o vrátenie správneho poplatku. Je to pravda? Ako mám postupovať, aby mi správny poplatok bol vrátený a na koho sa mám v tejto veci obrátiť?

**Model-Selected Provisions:**
- 145/1995/paragraf-10
- 162/1995/paragraf-32

**Question score:** 0.750

### Model-Selected Provision 1

**Provision:**
145/1995/paragraf-10

**Text written by the model for this provision:**

```text
Správny orgán rozhodne o vrátení správneho poplatku v plnej výške, ak sa úkon alebo konanie nevykonalo v zákonom stanovenej lehote bez zavinenia poplatníka. Lehota sa považuje za zachovanú, ak správny orgán v jej posledný deň odovzdá vybavenie na poštovú prepravu, odošle ho elektronicky alebo ho odovzdá priamo poplatníkovi.
```

**Extracted expected span:**

```text
S nedodržaním lehôt na rozhodnutie je spojená povinnosť orgánu katastra vrátiť zaplatený správny poplatok ex offo (teda aj bez Vášho návrhu), príp. na návrh, a to v zmysle ust. ***§ 10 ods. 1*** Zákona o správnych poplatkoch, ktorý ustanovuje, že správny orgán rozhodne o vrátení poplatku v plnej výške, ak sa nemohol vykonať úkon alebo uskutočniť konanie bez zavinenia poplatníka v lehote ustanovenej podľa osobitného predpisu.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je v zhode s expertnou odpoveďou. Oba texty správne uvádzajú kľúčovú informáciu, že správny orgán vráti poplatok v plnej výške, ak sa úkon nevykonal v stanovenej lehote bez zavinenia poplatníka. Hoci text modelu obsahuje navyše vetu o tom, kedy sa lehota považuje za zachovanú, a naopak neobsahuje zmienku o vrátení poplatku z úradnej povinnosti (ex offo), jadro právnej informácie je totožné a vecne správne. Preto udeľujem skóre 1.0.

### Model-Selected Provision 2

**Provision:**
162/1995/paragraf-32

**Text written by the model for this provision:**

```text
Okresný úrad má na rozhodnutie o návrhu na vklad do katastra nehnuteľností lehotu 30 dní odo dňa doručenia návrhu. V osobitných prípadoch, ako napríklad pri zmluve vo forme notárskej zápisnice alebo pri žiadosti o urýchlené konanie, sú lehoty kratšie.
```

**Extracted expected span:**

```text
***§ 32*** Katastrálneho zákona nám stanovuje lehoty na rozhodnutie o návrhu na vklad: základná lehota: 30 dní odo dňa doručenia návrhu na vklad, ak bola zmluva o prevode nehnuteľnosti vyhotovená vo forme notárskej zápisnice alebo ak bola autorizovaná advokátom: 20 dní odo dňa doručenia takého návrhu na vklad, na základe žiadosti o urýchlené konanie o návrhu na vklad a zaplatení príslušného správneho poplatku do 15 dní odo dňa doručenia návrhu na vklad. Ak v tejto lehote nerozhodne, rozhodne v základnej lehote. Predmetné lehoty nemožno predĺžiť.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu je iba čiastočne v súlade s expertnou odpoveďou. Správne identifikuje základnú 30-dňovú lehotu na rozhodnutie o vklade a tiež správne spomína, že v osobitných prípadoch (napr. notárska zápisnica, urýchlené konanie) sú lehoty kratšie. Na rozdiel od expertnej odpovede však nešpecifikuje konkrétnu dĺžku týchto skrátených lehôt (20 a 15 dní). Keďže jadro informácie je správne, ale chýbajú dôležité detaily, hodnotím text skóre 0.5.

---

## ID 1 | Status: OK

**Question:** Môj partner ma psychicky ponižuje, vyhráža sa mi a kontroluje mi telefón. Je to už týranie, aj keď ma neudrel?

**Model-Selected Provisions:**
- 300/2005/paragraf-127
- 300/2005/paragraf-208

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-127

**Text written by the model for this provision:**

```text
Pre účely trestného činu týrania sa za blízku osobu považuje okrem iných aj druh, bývalý druh alebo osoba, ktorá s páchateľom žije alebo žila v spoločnej domácnosti.
```

**Extracted expected span:**

```text
Na účely Trestného zákona je v zmysle ***§ 127 ods. 4*** TZ blízkou osobou: príbuzný v priamom pokolení, súrodenec, manžel, osvojiteľ a osvojenec. Iné osoby v rodinnom alebo obdobnom pomere sa pokladajú za blízke osoby, ak by ujmu, ktorú utrpela jedna z nich, druhá právom pociťovala ako vlastnú. Blízkou osobou sa ďalej na účely tohto ustanovenia v zmysle ***§ 127 ods. 5*** TZ rozumie aj: bývalý manžel, druh alebo bývalý druh, rodič spoločného dieťaťa, osoba, ktorá je vo vzťahu k nim blízkou osobou, osoba, ktorá s páchateľom žije alebo žila v spoločnej domácnosti.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je v úplnom súlade s expertnou odpoveďou. Správne uvádza, že za blízku osobu sa považuje aj druh, bývalý druh alebo osoba žijúca v spoločnej domácnosti. Hoci model neuvádza kompletný výpočet všetkých kategórií blízkych osôb, presne a vecne správne zachytáva tú časť definície, ktorá je relevantná pre kontext partnerského vzťahu. Zadanie nevyžaduje úplnú vyčerpávajúcnosť, preto je skóre 1.0.

### Model-Selected Provision 2

**Provision:**
300/2005/paragraf-208

**Text written by the model for this provision:**

```text
Trestného činu týrania blízkej osoby sa dopustí ten, kto jej spôsobí fyzické alebo psychické utrpenie. Zákon ako príklady foriem psychického utrpenia uvádza ponižovanie, pohŕdavé zaobchádzanie, neustále sledovanie, vyhrážanie, vyvolávanie strachu alebo stresu, či iné správanie, ktoré ohrozuje psychické zdravie.
```

**Extracted expected span:**

```text
Trestný čin týrania blízkej osoby alebo zverenej osoby upravuje ***§ 208*** Trestného zákona. Nejde pritom len o fyzické útoky, ale aj o konanie, ktoré spôsobuje psychické utrpenie. Psychické utrpenie sa musí skúmať individuálne u každej samostatnej osoby, nakoľko každá osoba konanie prežíva inak a inak na ňu konanie páchateľa vplýva. Podľa zákona sa ho dopustí ten, kto blízkej osobe alebo osobe, ktorá je v jeho starostlivosti alebo výchove, spôsobí fyzické alebo psychické utrpenie: a) bitím, kopaním, údermi, spôsobením rán a popálenín rôzneho druhu, ponižovaním, pohŕdavým zaobchádzaním, neustálym sledovaním, vyhrážaním, vyvolávaním strachu alebo stresu, násilnou izoláciou, citovým vydieraním alebo iným správaním, ktoré ohrozuje jej fyzické alebo psychické zdravie alebo obmedzuje jej bezpečnosť, b) bezdôvodným odopieraním stravy, oddychu alebo spánku alebo odopieraním nevyhnutnej osobnej starostlivosti, ošatenia, hygieny, zdravotnej starostlivosti, bývania, výchovy alebo vzdelávania, c) nútením k žobrote alebo k opakovanému vykonávaniu činnosti vyžadujúcej jej neúmernú fyzickú alebo psychickú záťaž vzhľadom na jej vek alebo zdravotný stav alebo spôsobilej poškodiť jej zdravie, d) vystavovaním vplyvu látok spôsobilých poškodiť jej zdravie, alebo e) neodôvodneným obmedzovaním v prístupe k majetku, ktorý má právo užívať.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecne správny a v plnom súlade s expertne označenou časťou odpovede. Správne definuje, že trestný čin týrania zahŕňa nielen fyzické, ale aj psychické utrpenie. Príklady foriem psychického utrpenia, ktoré model uvádza (ponižovanie, vyhrážanie, sledovanie, vyvolávanie strachu), sú priamo prevzaté z textu zákona, ktorý cituje aj expert. Model sa zameriava na relevantné aspekty a presne vystihuje podstatu.

---

## ID 2 | Status: OK

**Question:** Dobrý deň. Bol som bol prichytený pri šoférovaní pod vplyvom alkoholu, ale bez nehody. Čo mi za tento čin hrozí?

**Model-Selected Provisions:**
- 300/2005/paragraf-289
- 372/1990/paragraf-22

**Question score:** 0.250

### Model-Selected Provision 1

**Provision:**
300/2005/paragraf-289

**Text written by the model for this provision:**

```text
Vykonávanie činnosti, pri ktorej by mohol byť ohrozený život alebo zdravie ľudí, v stave vylučujúcom spôsobilosť privodenom návykovou látkou, je trestným činom. Páchateľovi takéhoto činu hrozí trest odňatia slobody až na jeden rok.
```

**Extracted expected span:**

```text
Ak však hladina alkoholu dosiahne 1 promile alebo viac , ide už o trestný čin ohrozenia pod vplyvom návykovej látky podľa ***§ 289*** Trestného zákona. Tresty v takom prípade sú odňatie slobody až na 1 rok a zákaz činnosti viesť motorové vozidlo na 1 až 10 rokov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Model správne identifikuje, že ide o trestný čin s možným trestom odňatia slobody až na jeden rok. V tomto je zhoda s expertom. Text modelu je však neúplný, pretože nespomína druhú, veľmi dôležitú časť trestu, a to zákaz činnosti viesť motorové vozidlo, ktorý môže byť uložený na 1 až 10 rokov. Keďže jadro (trestný čin, trest odňatia slobody) je správne, ale chýba podstatná časť sankcie, hodnotím odpoveď skóre 0.5.

### Model-Selected Provision 2

**Provision:**
372/1990/paragraf-22

**Text written by the model for this provision:**

```text
Vedenie vozidla v čase po požití alkoholu, keď sa ešte nachádza v organizme, je priestupkom proti bezpečnosti a plynulosti cestnej premávky. Za tento priestupok možno uložiť pokutu od 150 eur do 800 eur a zákaz činnosti do troch rokov.
```

**Extracted expected span:**

```text
Pri hodnote, ktorá bola nameraná, predstavujúcej menej než 1 promile , ide o priestupok proti bezpečnosti a plynulosti cestnej premávky podľa ***§ 22*** zákona č. 372/1990 Zb. o priestupkoch. Za tento priestupok možno uložiť pokutu od 200 do 1 000 eur a zákaz činnosti viesť motorové vozidlo až na 5 rokov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.000
**Verdict:** UNSUPPORTED

**Judge Explanation:**
Model správne identifikuje, že ide o priestupok proti bezpečnosti a plynulosti cestnej premávky. V tomto je zhoda. Model však uvádza úplne nesprávne sadzby sankcií. Pokuta podľa modelu je 150-800 eur a zákaz činnosti do 3 rokov, zatiaľ čo správne sadzby podľa expertnej odpovede sú pokuta 200-1000 eur a zákaz činnosti až na 5 rokov. Keďže model poskytuje nesprávne faktické informácie o výške trestu, je v rozpore s expertnou odpoveďou, a preto je skóre 0.0.

---
