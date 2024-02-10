# Toteutusdokumetti

## Ohjelman rakenne
Ohjelma koostuu [distance](/src/entities/distance.py) algoritmistä omasta luokasta, [trie](/src/entities/trie.py) tietorakenteen omasta luokasta ja luokasta [spellchecker](/src/services/spellchecker.py), joka käyttää näitä funktioita distance ja trie luokasta. Käyttäjä pääsee indexin avulla spellchecker luokkaan käyttämään tarvittavia funktiota, jotka korjaa tekstin sanakirjoitusvirheet.

## Lähteet
Trie tietorakenteen lähde: https://en.wikipedia.org/wiki/Trie

Algoritmin lähde: https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance 

Lähteet datalle/sanakirja ohjelmassa: https://github.com/dwyl/english-words/tree/master
