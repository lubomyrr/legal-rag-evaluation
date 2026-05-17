# Zhrnutie hodnotenia

## Metrika 1 - Zhoda vybraných paragrafov

Táto metrika hodnotí, či model vybral tie isté právne ustanovenia, ktoré boli uvedené v expertnej odpovedi.

- Počet hodnotených otázok: 29
- Správne nájdené paragrafy: 39 z 58 paragrafov očakávaných expertom
- Nesprávne pridané paragrafy: 10 z 49 paragrafov vybraných modelom
- Nenájdené paragrafy: 19 z 58 paragrafov očakávaných expertom
- Presnosť: 39/49 = 0,796
- Pokrytie: 39/58 = 0,672
- F1 skóre: 0,729

Presnosť ukazuje, aká časť paragrafov vybraných modelom bola správna. Pokrytie ukazuje, aká časť expertom očakávaných paragrafov bola modelom nájdená. F1 skóre spája presnosť a pokrytie do jednej hodnoty.

## Metrika 2 - Vernosť odpovede právnemu textu

Táto metrika hodnotí, či text vytvorený modelom správne vychádza z citovaného právneho ustanovenia a nemení jeho význam.

### Celkový výsledok

- Počet hodnotených záznamov: 49
- Plne podložené odpovede: 39 (80 %) - odpoveď modelu je vecne v súlade s citovaným právnym textom.
- Čiastočne podložené odpovede: 10 (20 %) - hlavná myšlienka je správna, ale odpoveď je neúplná alebo menej presná.
- Nepodložené odpovede: 0 (0 %) - odpoveď nemá oporu v citovanom právnom texte alebo ho nesprávne interpretuje.

### Výsledok pre metriku 2

Model vo väčšine prípadov vytvoril odpovede, ktoré boli priamo podložené citovaným právnym textom. Pri čiastočne podložených odpovediach bol problém najmä v tom, že model vynechal dôležité podmienky, výnimky alebo presnejšie časti právnej úpravy. V niektorých prípadoch model doplnil aj informácie, ktoré mohli byť vecne správne, ale neboli priamo obsiahnuté v hodnotenom právnom ustanovení.

## Metrika 3 - Zhoda s expertnou odpoveďou

Táto metrika hodnotí, či odpoveď modelu obsahovo zodpovedá relevantnej časti expertnej odpovede.

### Celkový výsledok

- Počet hodnotených záznamov: 39
- Plne zhodné odpovede: 30 (77 %) - odpoveď modelu vecne zodpovedá expertnej odpovedi.
- Čiastočne zhodné odpovede: 6 (15 %) - model zachytil hlavnú myšlienku, ale vynechal dôležité detaily alebo odpovedal menej presne.
- Nezhodné odpovede: 3 (8 %) - model odpovedal na iný právny bod alebo uviedol vecne nesprávnu informáciu.

### Výsledok pre metriku 3

Výsledky ukazujú, že model vo väčšine prípadov správne zachytil hlavný právny význam expertnej odpovede. Pri čiastočnej zhode model často odpovedal správnym smerom, ale vynechal konkrétne lehoty, alternatívne postupy, sadzby alebo iné podstatné detaily. Nezhodné odpovede sa objavili najmä v prípadoch, keď model riešil iný právny problém, než ktorý bol dôležitý v expertnej odpovedi.
