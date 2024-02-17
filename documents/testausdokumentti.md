# Testausdokumentti
Ohjelma on testattu automatisoidulla unittesteillä.

## Testit
Testit on jaettu kolmeen osaan:
- [distance_test](../src/tests/distance_test.py)
- [trie_test](../src/tests/trie_test.py)
- [spellchecker_test](../src/tests/spellchecker_test.py)
Nämä testit kattavat kaikki ohjelman toiminallisuuden tuottavat funktiot.

## Manuaaliset testit
Ohjelman teon aikana on tehty erilaisia manuaalisia testejä. Aluksi testattu vaan yhdellä kirjaimilla ja siiten lisätty sanan pituutta ja sitten väärää sanaa. Tämä auttoi tekemään funktiot, jotka antoivat ehdotuksia väärälle sanalle. Hyvät manualiset testit on sitten lisätty unitestihin. Esim sana "apend" tuotti listan eri tuloksista (oikeista sanoista). Lopuksi testattu teksi kappaletta, jossa on kirjoitusvirheitä, jonka avulla sitten tehtiin fix text funktio ja hyvä testisyöte laitetttiin unitesteihin.

### Testikattavuus
![Coverage_report](coverage_report.png)
