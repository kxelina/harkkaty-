Olen tehnyt trie tietorakenteen ja algoritmin loppuun. Tein funktion, joka antaa vaihtoehtoisen sanan väärinkirjoitetulle sanalle. Ohjelman pääfunktiot on nyt tehtynä. Tein testjä ja coverage-raportin(100%) avulla tiedän, että ne ovat kattavat. En tiedä, miksi en saa codecov:a toimimaan, jotenkin se ei löydä minun main-branchiä reposta. Olisi kiva saada apua tähän asiaan. Laitoin pylintin pyörimään. Mietin, että onko algoritmi tehty tarpeeksi hyvin, testasin kyllä sen aikaa(indexin printinstä löytyy aika) ja pitääkö sitä vielä jotenkin opitmoida. Seuraavaksi ajattelin tehdä spellcheckeriä eli käyttöliittymän puolta. 

Päiväys       | aika | mitä tein |
-----------|------|--------|
2024-01-21 | 3h | trie.py tehty toimivaksi. Tutustuttu Damerau-Levenshtein-distance-algoritmiin seuraavaksi. |
2024-01-25 | 2h | Aloitettu testien tekemistä, tuli module-error ja piti korjaa sitä. Huomasin, että triessä search funktio ei toiminut enää. Aloin korjaaman sitä. |
2024-01-26 | 5h | Trie korjattu, tehty testejä sille ja aloitettu algoritmin tekemistä. Otin valmiin algoritmin netistä: https://www.geeksforgeeks.org/damerau-levenshtein-distance/ ja aloin tekemään get suggestions funktiota eli antais ehdotuksen virheelle sanalle. Ajattelin tehdä algoritmin vasta sitten kun saan tämän funktion tehtyä. Laiton codecovin näkyviin readme:seen. |
2024-01-27 | 6h | Tehty get suggestions funktio loppuun, tein omaa distance algoritmiä loppuun, katsoin mallia pseudokoodista. |
yht | 16h
