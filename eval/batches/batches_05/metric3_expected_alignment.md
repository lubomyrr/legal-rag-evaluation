# Metric 3 - Expected Alignment

## Summary

Evaluated questions: 3
Evaluated model-selected provisions: 5
Mean question score: 0.944
Mean provision score: 0.900
Skipped questions: 0
Metrika 3 porovnava text modelu s relevantnym vyrezom expertnej expected odpovede pre ten isty pravny predpis. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

## ID 0 | Status: OK

**Question:** Dobrý deň, zamestnávateľ mi oznámil, že sa ruší moje pracovné miesto. Na čo mám nárok od zamestnávateľa v takejto situácii?

**Model-Selected Provisions:**
- 311/2001/paragraf-63
- 311/2001/paragraf-64
- 311/2001/paragraf-76

**Question score:** 0.833

### Model-Selected Provision 1

**Provision:**
311/2001/paragraf-63

**Text written by the model for this provision:**

```text
Zamestnávateľ môže dať zamestnancovi výpoveď, ak sa zamestnanec stane nadbytočným na základe písomného rozhodnutia o organizačných zmenách, napríklad o znížení stavu zamestnancov. Pred podaním výpovede z tohto dôvodu je zamestnávateľ povinný zamestnancovi ponúknuť inú pre neho vhodnú prácu, ak má takúto prácu k dispozícii.
```

**Extracted expected span:**

```text
Výpovedný dôvod podľa ***§ 63 ods. 1*** písm. b) zákona č. 311/2001 Z. z. Zákonníka práce – teda nadbytočnosť zamestnanca – oprávňuje zamestnávateľa dať výpoveď zamestnancovi v prípade, ak sa zamestnanec stane nadbytočným na základe písomného rozhodnutia zamestnávateľa alebo príslušného orgánu o zmene jeho úloh, vybavenia, o znížení počtu zamestnancov za účelom zvýšenia efektívnosti práce alebo z iných organizačných dôvodov. Tento výpovedný dôvod možno uplatniť až po prijatí rozhodnutia , pričom toto rozhodnutie musí mať písomnú formu . Medzi organizačnou zmenou a nadbytočnosťou zamestnanca musí existovať príčinná súvislosť .
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je v súlade s expertnou odpoveďou. Správne uvádza, že výpoveď z dôvodu nadbytočnosti musí byť podložená písomným rozhodnutím o organizačných zmenách. Model navyše správne dopĺňa aj súvisiacu ponukovú povinnosť zamestnávateľa, ktorá je pre danú situáciu relevantná. Informácie sú vecne správne.

### Model-Selected Provision 2

**Provision:**
311/2001/paragraf-64

**Text written by the model for this provision:**

```text
Zákonník práce ustanovuje ochranné doby, počas ktorých zamestnávateľ nesmie dať zamestnancovi výpoveď, napríklad počas práceneschopnosti, tehotenstva alebo rodičovskej dovolenky. Tento zákaz výpovede sa však neuplatní, ak sa zamestnávateľ alebo jeho časť zrušuje.
```

**Extracted expected span:**

```text
Zákaz výpovede v tzv. ochrannej dobe (***§ 64*** Zákonníka práce). Vhodnou prácou je aj práca na kratší týždenný pracovný čas, aj keď zamestnanec predtým pracoval na plný úväzok. Môže ísť o akúkoľvek prácu, ktorá sa nachádza v mieste výkonu práce dohodnutom v pracovnej zmluve, aj keď nezodpovedá pôvodne dohodnutému druhu práce. Zákaz výpovede , resp. ochranná doba, je obdobie, počas ktorého zamestnávateľ nesmie dať zamestnancovi výpoveď, aj keď by na to mal zákonný dôvod. Ide napríklad o čas: dočasnej pracovnej neschopnosti pre chorobu alebo úraz (ak ju zamestnanec úmyselne nevyvolal alebo nespôsobil pod vplyvom alkoholu či drog), tehotenstva zamestnankyne, materskej, otcovskej alebo rodičovskej dovolenky a pod.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s expertnou odpoveďou. Správne definuje ochrannú dobu ako obdobie, počas ktorého zamestnávateľ nemôže dať zamestnancovi výpoveď, a uvádza správne príklady (PN, tehotenstvo, rodičovská dovolenka). Model navyše správne dopĺňa aj dôležitú výnimku zo zákazu výpovede, ktorá sa uplatní pri zrušení zamestnávateľa.

### Model-Selected Provision 3

**Provision:**
311/2001/paragraf-76

**Text written by the model for this provision:**

```text
Zamestnancovi, s ktorým zamestnávateľ skončí pracovný pomer výpoveďou alebo dohodou z dôvodu nadbytočnosti, patrí odstupné. Výška odstupného závisí od dĺžky trvania pracovného pomeru a pohybuje sa od jedného až po päťnásobok priemerného mesačného zárobku. Odstupné je vyplatené po skončení pracovného pomeru v najbližšom výplatnom termíne, pokiaľ sa zamestnávateľ a zamestnanec nedohodnú inak.
```

**Extracted expected span:**

```text
Podľa ***§ 76*** Zákonníka práce má zamestnanec pri výpovedi z dôvodu nadbytočnosti nárok na odstupné podľa dĺžky trvania pracovného pomeru: 2 až menej ako 5 rokov : 1-násobok priemerného mesačného zárobku, 5 až menej ako 10 rokov : 2-násobok, 10 až menej ako 20 rokov : 3-násobok, 20 rokov a viac : 4-násobok priemerného mesačného zárobku.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu je iba čiastočne v súlade s expertnou odpoveďou. Jadro informácie, že zamestnancovi patrí odstupné, ktorého výška závisí od dĺžky trvania pracovného pomeru, je správne. Model však uvádza nepresný rozsah odstupného (jeden až päťnásobok), čím spája výšku odstupného pri výpovedi a pri dohode. Expertná odpoveď správne špecifikuje, že pri výpovedi je maximálna výška štvornásobok priemerného zárobku. Formulácia modelu je preto nepresná a mierne zavádzajúca.

---

## ID 1 | Status: OK

**Question:** Dobrý deň, zamestnávateľa som požiadal o dovolenku na budúci týždeň, nakoľko by som chcel ísť na výlet s rodinou. Zamestnávateľ mi však odmietol dovolenku poskytnúť. Má na to právo alebo si môže dovolenku vybrať aj napriek tomu?

**Model-Selected Provisions:**
- 311/2001/paragraf-111

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
311/2001/paragraf-111

**Text written by the model for this provision:**

```text
Čerpanie dovolenky určuje zamestnávateľ po prerokovaní so zamestnancom a podľa plánu dovoleniek. Pri rozhodovaní o termíne dovolenky je potrebné prihliadať na úlohy zamestnávateľa, ako aj na oprávnené záujmy zamestnanca. Zamestnávateľ je povinný oznámiť zamestnancovi určené čerpanie dovolenky aspoň 14 dní vopred, ak sa nedohodnú na kratšej dobe.
```

**Extracted expected span:**

```text
In concreto v ***§ 111*** Zákonníka práce je zakotvené, že je to zamestnávateľ, ktorý určuje nástup na dovolenku. Zamestnanec ako oprávnený subjekt práva na dovolenku nemôže preto sám rozhodovať, kedy si bude čerpať dovolenku. Čerpanie dovolenky určuje zamestnávateľ po prerokovaní so zamestnancom podľa plánu dovoleniek s predchádzajúcim súhlasom zástupcov zamestnancov, pričom má pritom prihliadať na oprávnené záujmy zamestnancov.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecne v súlade s expertnou odpoveďou. Oba texty správne uvádzajú kľúčovú informáciu, že čerpanie dovolenky určuje zamestnávateľ, nie zamestnanec. Model správne spomína, že sa tak deje po prerokovaní so zamestnancom a s prihliadnutím na jeho oprávnené záujmy. Hoci model nespomína súhlas zástupcov zamestnancov, jadro právneho bodu je zachytené presne a v plnom rozsahu.

---

## ID 2 | Status: OK

**Question:** Chcel by som sa informovať ohľadom obrany proti výpovedi z práce. Nedávno som dostal výpoveď zo zamestnania, ktorú považujem za neoprávnenú a neodôvodnenú. Zaujíma ma, aké mám možnosti a akým spôsobom sa môžem brániť proti tejto výpovedi.

**Model-Selected Provisions:**
- 311/2001/paragraf-63

**Question score:** 1.000

### Model-Selected Provision 1

**Provision:**
311/2001/paragraf-63

**Text written by the model for this provision:**

```text
Zamestnávateľ môže dať zamestnancovi výpoveď iba z dôvodov presne stanovených v zákone. Medzi tieto dôvody patrí napríklad zrušenie alebo premiestnenie zamestnávateľa, nadbytočnosť zamestnanca z dôvodu organizačných zmien, alebo zdravotné dôvody na strane zamestnanca. Výpoveď je možná aj pri nespĺňaní predpokladov, neuspokojivom plnení úloh alebo pri porušení pracovnej disciplíny za stanovených podmienok.
```

**Extracted expected span:**

```text
Zamestnávateľ môže ukončiť pracovný pomer výpoveďou len z dôvodov v ust. ***§ 63 ods. 1*** Zákonníka práce, pričom tento výpovedný dôvod treba vymedziť tak, aby neboli pochybnosti o skutočnom dôvode výpovede, inak je táto neplatná.
Výpovedné dôvody zo strany zamestnávateľa sú nasledovné:
- Ak sa zamestnávateľ alebo jeho časť zrušuje alebo premiestňuje a zamestnanec nesúhlasí so zmenou dohodnutého miesta výkonu práce,
- Ak sa zamestnanec stane nadbytočným vzhľadom na písomné rozhodnutie zamestnávateľa alebo príslušného orgánu o zmene jeho úloh, technického vybavenia, o znížení stavu zamestnancov za účelom zvýšenia efektívnosti práce alebo o iných organizačných zmenách,
- Ak zamestnanec vzhľadom na svoj zdravotný stav podľa lekárskeho posudku dlhodobo stratil spôsobilosť vykonávať doterajšiu prácu,
- Ak zamestnanec nespĺňa predpoklady ustanovené právnymi predpismi alebo vnútorným predpisom zamestnávateľa na výkon dohodnutej práce,
- Ak zamestnanec neuspokojivo plní pracovné úlohy a zamestnávateľ ho v posledných 6 mesiacoch písomne vyzval na odstránenie nedostatkov a ten ich neodstránil,
- Ak sú u zamestnanca dôvody, pre ktoré by s ním zamestnávateľ mohol okamžite skončiť pracovný pomer, alebo pre menej závažné porušenie pracovnej disciplíny, ak bol v posledných 6 mesiacoch v súvislosti s porušením pracovnej disciplíny písomne upozornený na možnosť výpovede.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf vecne zodpoveda relevantnej casti expertnej expected odpovede pre ten isty pravny predpis.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecne v súlade s expertnou odpoveďou. Správne a výstižne vymenúva hlavné kategórie výpovedných dôvodov zo strany zamestnávateľa, ako sú organizačné dôvody (zrušenie, nadbytočnosť), zdravotné dôvody, nespĺňanie predpokladov, neuspokojivé plnenie úloh a porušenie disciplíny. Hoci model neuvádza všetky detaily a podmienky (napr. predchádzajúce písomné upozornenie), tieto sú implicitne zahrnuté pod formuláciou "za stanovených podmienok". Ide o presné zhrnutie, ktoré zachytáva jadro právnej úpravy, preto udeľujem skóre 1.0.

---
