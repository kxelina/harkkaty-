# Toteutusdokumetti
Ohjelma ottaa vastaan teksipätkän ja tarkistaa sanojen oikean englannin kirjotuksen. Sanat ovat kirjoitettu a-z kirjamilla (voi olla isoja kirjaimia, mutta palauttaa vain pieniä kirjaimia), muita merkkejä ja numeroita ei tarkisteta vaan ne hyväksytään sellaisenaan. Käyttäjä voi halutessa vaihtaa oman sanaston vaihtomalla file_path. 

## Ohjelman rakenne
Ohjelma koostuu [distance](/src/entities/distance.py) algoritmi luokasta (vertaa kahta sanaa ja kertoo niiden eron etäisyytenä), [trie](/src/entities/trie.py) puimaisesta tietorakenne luokasta (säilyttää sanakirjan) ja luokasta [spellchecker](/src/services/spellchecker.py) (etsii väärinkirjoitetulle sanalle läheisimään ehdotuksen), joka käyttää näitä funktioita distance ja trie luokasta. Käyttäjä pääsee indexin avulla spellchecker luokkaan käyttämään tarvittavia funktiota, jotka korjaa tekstin sanakirjoitusvirheet. 

## O-analyysi
Wikipedian mukaan Trie:n aikavaativuus olisi O(n), missä n on sananpituus ja sen tilavaativuus olisi myös O(nm), missä n nodenjen määrä kertaa 26^(n-1) kirjainta pahimmassa tapauksessa ja m sanakirjan sanojen keskimääräinen pituus.
Kokeilin kuinka kauan kestää omassa ohjelmassa tallentaa sanakirja trieelle: 4,959 s.

Algorimin aikavaativuus pitäisi pahminmassa tapauksessa olla O(mn), missä m on sanan pituus ja n on sanakirjoijen sanojen keskimäärinen pituus. Sen tilavaativuus pitäisi olla O(n), missä n on pidempi sana kahden vertailevan sanan välistä.
Ohjelmassa, jos löytyy sana, niin nopeus on n*10^⁻6 s, missä n on keskimäärin 5 eli siihen vaikuttaa sanan pituus ja sanalistan pituus.

## Puutteet ja parannusehdot
Puutteena on, että ohjelma on jossain tapauksissa hidas ja ohjelma ei palauta parasta vaihtoehtoa vääriinkirjoitetulle sanalle käyttäjän kannalta vaan palauttaa sanan mikä on lähin etäisyys, koska käytetään distance algoritmia. Esim. sanalle voi löytyä monta vaihtoehtoa ja parannusehtona olisi, että käyttäjä saisi kaikki vaihtoedot ja voisi itse valita sopivan sanan. Tai ohjelmassa voisi lisätä sellaisen arpomisfunktio eli osaisi arvata, minkä oikean sanan käyttäjä haluisi. Parannusehtona olisi, että ohjelma voisi muistaa käyttäjän tekemät yleiset virheet ja siitä syntyisi oma sanakirja.
Toisena parannusehtona olisi, että sanat olisivat samalla tyylillä, mitten käyttäjä on lisännyt sinne, tällä hetkellä ohjelma muuttaa kaikki sanat pieneksi kirjaimiseksi.
Trien luominen kestää tässä ohjelmassa, koska sanasto on iso, mutta sitä voisi ehkä yrittää optimoida. Algotimiä voisi optimoida siten, että käyttäsi jotain map-työkalua ja laittaisi esim. lähellä olevat kirjaimet näppäimistössä tallenteen ja käyttäsi sitä hyödyksi. 
Voisi käyttää jotain toista algoritmia apuna ohjelman nopeuttamiselle. Ohjelma voisi toimi myös muilla kielillä, mutta ohjelman toimintoja pitäisi muuttaa. Esim. suomenkielellä on haastavampi tehdä taivutusten takia.

## Lähteet
Trie tietorakenteen lähde: https://en.wikipedia.org/wiki/Trie

Algoritmin lähde: https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance 

Lähteet datalle/sanakirja ohjelmassa: https://github.com/dwyl/english-words/tree/master
