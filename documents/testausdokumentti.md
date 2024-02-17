# Testausdokumentti
Ohjelma on testattu automatisoidulla unittesteillä.

## Testit
Testit on jaettu kolmeen osaan:
- [distance_test](../src/tests/distance_test.py)
- [trie_test](../src/tests/trie_test.py)
- [spellchecker_test](../src/tests/spellchecker_test.py)
Jaettu näin, koska sitten omille luokille on omat testit, joka selkentää asiaa. Testeihin on kirjoitettu komentilla, että mitä eri testit merkitsevät ja miksi testataan niillä syötteillä.
Nämä testit kattavat kaikki ohjelman toiminallisuuden tuottavat funktiot. Testihin laitettu onnistuneet tapaukset(sana löyty) ja epäonnistuneet tapukset(sana ei löydy) ja rajatapauksia(eri sanapituuksille eri testit).

## Manuaaliset testit
Ohjelman teon aikana on tehty erilaisia manuaalisia testejä. Aluksi testattu vaan yhdellä kirjaimilla ja siiten lisätty sanan pituutta ja sitten väärää sanaa. Tämä auttoi tekemään funktiot, jotka antoivat ehdotuksia väärälle sanalle. Hyvät manualiset testit on sitten lisätty unitestihin. Esim sana "apend" tuotti listan eri tuloksista (oikeista sanoista). Lopuksi testattu teksi kappaletta, jossa on kirjoitusvirheitä, jonka avulla sitten tehtiin fix text funktio ja hyvä testisyöte laitetttiin unitesteihin.
On testattu algorimin ja ohjelman nopeutta sekä optimointia testattiin python time funktion avulla. Isoa sanakirjaa on vaan testattu manuaalisesti. Unittesteissä käytetään omaa pienempää sanakirjaa.

### Testikattavuus
![Coverage_report](coverage_report.png)!
