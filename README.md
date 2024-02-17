# harkkaty-
[![workflow_badge](https://github.com/kxelina/ohtuvarasto/workflows/CI/badge.svg)](https://github.com/kxelina/harkkaty-/blob/main/.github/workflows/main.yml)
[![codecov](https://codecov.io/gh/kxelina/ohtuvarasto/graph/badge.svg?token=NGPX79ATFB)](https://codecov.io/gh/kxelina/harkkaty-)


Kirjoitusvirheiden korjaajassa käytetään "Damerau-Levenshtein-etäisyys" algoritmiä ja trie-tietorakenetta. Tarkoituksena olisi korjata käyttäjän syöttämä tekstipätkä(englanniksi).

## Dokumentaatio
- [määrittelydokumentti](./documents/määrittelydokumentti.md)
- [toteutusdokumentti](./documents/toteutusdokumentti.md)
- [testausdokumentti](./documents/testausdokumentti.md)
- [käyttöohje](./documents/käyttöohje.md)

### Viikkoraportit
- [viikko1](./documents/viikkoraportit/raportti1.md)
- [viikko2](./documents/viikkoraportit/raportti2.md)
- [viikko3](./documents/viikkoraportit/raportti3.md)
- [viikko4](./documents/viikkoraportit/raportti4.md)
- [viikko5](./documents/viikkoraportit/raportti5.md)
- [viikko6](./documents/viikkoraportit/raportti6.md)

## Komennot
Kloonaa aluksi repo omalle koneelle.
Lataa poetry:
```
poetry install
```
Avaa virtuaaliympäristö:
```
poetry shell
```
### Avaa ohjelman:
```
poetry run invoke start
```
### Testit:
```
poetry run invoke test
```
### Coverage-report:
```
poetry run invoke coverage
```
Raportti tulee _htmlcov_ kansioon index tiedostoon

### Pylint:
```
poetry run invoke lint
