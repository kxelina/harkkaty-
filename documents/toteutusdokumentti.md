# Toteutusdokumetti
Ohjelma ottaa vastaan teksipätkän ja tarkistaa sanojen oikean englannin kirjotuksen. Sanat ovat kirjoitettu a-z kirjamilla (voi olla isoja kirjaimia, mutta palauttaa vain pieniä kirjaimia), muita merkkejä ja numeroita ei tarkisteta vaan ne hyväksytään sellaisenaan. Käyttäjä voi halutessa vaihtaa oman sanaston vaihtomalla file_path. 

## Ohjelman rakenne
Ohjelma koostuu [distance](/src/entities/distance.py) algoritmi luokasta (vertaa kahta sanaa ja kertoo niiden eron etäisyytenä), [trie](/src/entities/trie.py) puimaisesta tietorakenne luokasta (säilyttää sanakirjan) ja luokasta [spellchecker](/src/services/spellchecker.py) (etsii väärinkirjoitetulle sanalle läheisimään ehdotuksen), joka käyttää näitä funktioita distance ja trie luokasta. Käyttäjä pääsee [indexin](/src/index.py) avulla spellchecker luokkaan käyttämään tarvittavia funktiota, jotka korjaa tekstin sanakirjoitusvirheet.

### Optimointi
Korjatun sanan haku funktiota [get_correct_word](/src/services/spellchecker.py) on optimoitu. Jos sana on oikein kirjoitettu ja löytyy sanakirjasta, niin funktio on nopea, koska käytetään trie search funktiota siinä. Jos oikein kirjoitettua sanaa ei löydy oli alkuperäinen funktio hidas, sillä se kävi kaikki sanakirjan sanat läpi ja yritti etsiä lyhintä etäisyyttä ("paras" oikein kirjoitettu vaihtoehto). 

Ensimmäinen optimointi on tehty käyttämällä nopeaa trie serch funktiota, missä katsotaan löytyykö oikein kirjoitettu sana tekemällä pieni muutos: lisäämällä alkukirjain tai ottamalla pois alkukirjain ja samoin loppukirjaimelle, jos löytyy tällä tavalla oikein kirjoitettu sana, niin etäisyys on 0,5 ja palautetaan käyttäjälle nämä sanat. 

Toisen optimointia ideana on käyttää ensin pientä sanakirjaa (yleisimmät sanat), joka on tietenkin nopeampi kuin iso sanakirjan läpi käyminen. Pienestä sanakirjasta palautetaan vain etäisyydellä 1 olevat sanat käyttäjälle. Jos ei vieläkään löytynyt sanalle ehdotusta, niin etsitään isosta sanakirjasta (kaikki sanat) pieninmällä etäisyydellä olevat sanat (alkuperäinen optimoimaton get_correct_word funktio) ja palautetaan ne käyttäjälle. 

## O-analyysi
Wikipedian mukaan Trie:n aikavaativuus olisi O(n), missä n on sananpituus ja sen tilavaativuus olisi myös O(nm), missä n nodenjen määrä kertaa 26^(n-1) kirjainta pahimmassa tapauksessa ja m sanakirjan sanojen keskimääräinen pituus.
Kokeilin kuinka kauan kestää omassa ohjelmassa tallentaa sanakirja trieelle: 4,959 s.

Algorimin aikavaativuus pitäisi pahminmassa tapauksessa olla O(mn), missä m on sanan pituus ja n on sanakirjoijen sanojen keskimäärinen pituus. Sen tilavaativuus pitäisi olla O(n), missä n on pidempi sana kahden vertailevan sanan välistä.
Ohjelmassa, jos löytyy sana, niin nopeus on n*10^⁻6 s, missä n on keskimäärin 5 eli siihen vaikuttaa sanan pituus ja sanalistan pituus.

## Puutteet ja parannusehdot
Puutteena on, että ohjelma on vielä jossain tapauksissa hidas (käy ison sanakirjan kokonaan läpi) ja ohjelma ei ehdota parasta vaihtoehtoa vääriinkirjoitetulle sanalle käyttäjän kannalta vaan palauttaa sanat jossa on lähin etäisyys, koska käytetään pelkästään valittua distance algoritmia. UI:sen on lisätty, että käyttäjä pystyy valita haluamansa sanaehdotuksen tai olla valitsematta ehdotusta jos sana on mielestään oikea. Tätä voisi jatkokehittää siten, että käyttäjä voisi pyytää lisää sanaehdotuksiä, esim. distance on 2, jos sopivaa sanaa ei löytynyt. Ohjelma voisi muistaa käyttäjän valitsemat korjaukset, jotta voisi automaattisesti ehdottaa suoraan nämä sanaehdotukset. Voisi myös lisätä automaatikorjaus-toiminnon, missä ohjelma korjaa sanat automaattisesti. 

Ohjelma voisi muistaa käyttäjän tekemät yleiset virheet tai muuten yleisiä oikeinkirjoitus virheitä ja siitä syntyisi oma sanakirja. Sanat olisivat samalla tyylillä, miten käyttäjä on lisännyt sinne, tällä hetkellä ohjelma muuttaa kaikki sanat pieneksi kirjaimiseksi. Ohjelma voisi toimi myös muilla kielillä, mutta ohjelman toimintoja pitäisi muuttaa. Esim. suomenkielellä on haastavampi tehdä taivutusten takia.

Distance-algotimia voisi optimoida siten, että costin arvo muuttuisi dynaamisesti eri tapauksissa varsinkin virheiden kasvaessa (cost kasvaa). Pitäisi käyttää map-funktiota/tietorakennetta (eri costeja), joka "yhdistää" näppäimistön vierekkäiset kirjaimet ja helposti sekottuvat kirjaimet (esim.p ja b). Distance-algoritmille voisi tehdä myös pruning eli jos costin arvo kasvaa liian suureksi, niin lopettaisi ajoissa. Lisäksi voisi käyttää jotain toista algoritmia apuna ohjelman nopeuttamiselle.

Get-suggestion funktiota voisi optimoida siten (trie pruning), että turhia nodeja ei käytäisi läpi, esimerkiksi käytetään distance tietoa. Trien luominen kestää tässä ohjelmassa, koska sanasto on iso, mutta sitä voisi ehkä yrittää optimoida. Nyt trieseen luodaan yksi sana kerraallaan ja jos muistaisi edellisen sanan, niin pystyisi hypätä suoraan oikeaan nodeen.

## Lähteet
Trie tietorakenteen lähde: https://en.wikipedia.org/wiki/Trie

Algoritmin lähde: https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance 

Lähteet datalle/sanakirja ohjelmassa: https://github.com/dwyl/english-words/tree/master

Käytetty Chatgpt vain alussa kysymään aika- ja tilavaativuksia, sitten UI:n teossa nopeuttamaan ohjelman tekoa, kuten kysytty miten laittaa punaisen värin ja miten käyttäjä voi laittaa exit komennon, muuten ei ole käytetty.
