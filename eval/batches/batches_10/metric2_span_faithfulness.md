# Metric 2 - Structured Answer Faithfulness to Legal Text

## Summary

Evaluated questions: 2
Evaluated model-selected provisions: 3
Mean question score: 0.875
Mean provision score: 0.833
Skipped questions: 1
Metrika 2 porovnava text modelu pre kazdy zvoleny paragraf s textom samotneho pravneho predpisu. Skore 0.0 znamena nepodporene, 0.5 ciastocne podporene a 1.0 plne podporene.

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

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20250217
PARAGRAPH: 212
TITLE: Krádež
TEXT:
Kto si prisvojí cudziu vec tým, že sa jej zmocní a
a) spôsobí tak malú škodu,
b) čin spácha vlámaním,
c) bezprostredne po čine sa pokúsi uchovať si vec násilím alebo hrozbou bezprostredného násilia,
d) čin spácha na veci, ktorú má iný na sebe alebo pri sebe,
e) takou vecou je vec z úrody z pozemku, ktorý patrí do poľnohospodárskeho pôdneho fondu, alebo drevo nachádzajúce sa na lesnom pozemku, alebo ryba z rybníka s intenzívnym chovom, alebo
f) čin spácha na veci, ktorej odber podlieha spoplatneniu na základe osobitného predpisu,
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 0.500
**Verdict:** PARTIALLY_SUPPORTED

**Judge Explanation:**
Text modelu správne identifikuje základnú skutkovú podstatu krádeže (prisvojenie si cudzej veci) a uvádza aj niektoré kvalifikované skutkové podstaty, ako je spáchanie činu vlámaním alebo na veci, ktorú má iný pri sebe. Formulácia je však nepresná, pretože uvádza spôsobenie malej škody ako základnú podmienku, ku ktorej sa pridávajú ďalšie prípady. Podľa zákona je však spôsobenie malej škody len jednou z viacerých alternatívnych podmienok (uvedených pod písmenami a) až f)), ktoré musia byť splnené, aby sa konanie kvalifikovalo ako trestný čin krádeže. Jadro informácie je správne, ale jej štruktúra a vzťahy medzi jednotlivými podmienkami sú podané nepresne.

### Model-Selected Provision 2

**Provision:**
372/1990/paragraf-50

**Text written by the model for this provision:**

```text
Priestupku proti majetku sa dopustí ten, kto úmyselne spôsobí škodu na cudzom majetku krádežou. Za takýto priestupok možno uložiť pokutu do výšky 1 400 eur. V prípade opakovaného spáchania priestupku v priebehu 12 mesiacov môže byť uložená pokuta až do výšky 2 000 eur.
```

**Text of legal provision:**

```text
LAW: 372/1990
VERSION: 20250201
PARAGRAPH: 50
TITLE: Priestupky proti majetku
TEXT:
(1) Priestupku sa dopustí ten, kto úmyselne spôsobí škodu na cudzom majetku alebo sa o takéto konanie pokúsi
a) krádežou,
b) spreneverou,
c) podvodom,
d) zatajením veci alebo
e) poškodením veci z takého majetku.
(2) Priestupku sa dopustí aj ten, kto úmyselne zosnoval alebo riadil spáchanie priestupku podľa odseku 1, naviedol iného na spáchanie priestupku podľa odseku 1, požiadal iného, aby spáchal priestupok podľa odseku 1, alebo poskytol inému pomoc na spáchanie priestupku podľa odseku 1, najmä zadovážením prostriedkov, odstránením prekážok, radou, utvrdzovaním v predsavzatí alebo sľubom pomôcť po spáchaní priestupku podľa odseku 1.
(3) Za priestupok podľa odsekov 1 a 2 možno uložiť pokutu do 1 400 eur, v blokovom konaní do 500 eur a v rozkaznom konaní do 1 000 eur.
(4) Ak sa páchateľ v priebehu 12 mesiacov dopustí priestupku podľa odseku 1 alebo 2 opakovane, možno mu uložiť pokutu až do výšky 2 000 eur a v rozkaznom konaní do výšky 1 500 eur.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je plne v súlade s právnym predpisom. Správne uvádza, že priestupku proti majetku sa dopustí ten, kto úmyselne spôsobí škodu krádežou. Taktiež presne cituje výšku možnej pokuty (do 1 400 eur) a zvýšenej sadzby v prípade opakovaného spáchania priestupku v priebehu 12 mesiacov (až do 2 000 eur). Všetky uvedené informácie sú priamo podložené v odsekoch 1, 3 a 4 daného paragrafu.

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

**Text of legal provision:**

```text
LAW: 300/2005
VERSION: 20240806
PARAGRAPH: 66
TEXT:
(1) Súd môže odsúdeného podmienečne prepustiť na slobodu, ak odsúdený vo výkone trestu plnením svojich povinností a svojím správaním preukázal polepšenie a môže sa od neho očakávať, že v budúcnosti povedie riadny život, a
a) ak ide o osobu odsúdenú za prečin po výkone polovice uloženého nepodmienečného trestu odňatia slobody alebo rozhodnutím prezidenta Slovenskej republiky zmierneného nepodmienečného trestu odňatia slobody,
b) ak ide o osobu odsúdenú za zločin po výkone dvoch tretín uloženého nepodmienečného trestu odňatia slobody alebo rozhodnutím prezidenta Slovenskej republiky zmierneného nepodmienečného trestu odňatia slobody,
c) ak ide o osobu odsúdenú za zločin, ktorá nebola pred spáchaním trestného činu vo výkone trestu odňatia slobody po výkone polovice uloženého nepodmienečného trestu odňatia slobody alebo rozhodnutím prezidenta Slovenskej republiky zmierneného nepodmienečného trestu odňatia slobody; súd zároveň nariadi kontrolu technickými prostriedkami.
(2) Pri rozhodovaní o podmienečnom prepustení súd prihliadne aj na povahu spáchaného trestného činu a na to, v akom ústave na výkon trestu odsúdený trest vykonáva.
(3) Ak odsúdený má vykonať viac trestov odňatia slobody, odsúdený môže byť podmienečne prepustený najskôr po výkone súčtu pomerných častí uložených trestov podľa odseku 1 písm. a) až c), § 67 ods. 1 a 2 a celého zvyšku trestu podľa § 68 ods. 2 .
(4) Ak ide o podmienečné prepustenie podľa odseku 1 písm. c), kontrolu technickými prostriedkami možno skončiť najskôr po uplynutí doby, ktorá zodpovedá dvom tretinám uloženého nepodmienečného trestu odňatia slobody alebo rozhodnutím prezidenta Slovenskej republiky zmierneného nepodmienečného trestu odňatia slobody.
```

**What the judge evaluated:**
Sudca posudzoval, ci text modelu pre tento paragraf verne vystihuje obsah citovaneho pravneho predpisu, bez doplnenia novych pravidiel, vynimiek alebo skreslenia pravneho vyznamu.

**Score:** 1.000
**Verdict:** SUPPORTED

**Judge Explanation:**
Text modelu je vecným a presným zhrnutím kľúčových podmienok pre podmienečné prepustenie z výkonu trestu. Správne uvádza podmienky týkajúce sa správania odsúdeného a prognózy jeho budúceho života, ktoré sú podložené v odseku 1. Taktiež správne sumarizuje podmienku výkonu časti trestu (polovica pri prečine, dve tretiny pri zločine), čo vychádza z odseku 1 písm. a) a b). Použitie slova „spravidla“ je v tomto kontexte vhodné, keďže zákon pozná aj výnimku (písm. c)). Nakoniec, zmienka o tom, že súd prihliada na povahu trestného činu, je podložená v odseku 2. Model nepridáva žiadne nepodložené informácie a presne vystihuje podstatu právnej úpravy, preto je skóre 1.0.

---
