# Määrittelydokumentti
- Käytän pythonia ja hallitsen pythonia.
- Ajattelin käyttää "Damarau-Levenshtein-etäisyys" algoritmiä ja trie-tietorakennetta.
- Käyttämällä kyseistä algoritmiä, niin pystytään arvioimaan kahden merkkijonon välisiä eroja ja siten löytämään sanoille korjauksen. Algoritmillä voidaan ehdottaa korjauksia sanalle, koska algoritmi valitsee sanan, joka on lähimpänä käyttäjän syöttämää sanaa. Kyseisellä tietorakenteellä pystytään tallentamaan joukko sanoja tai merkkijonoja ja se nopeuttaa etsintää sanakirjasta. Trie-tietorakennella voidaan ehdottaa korjauksia sanoille. 
- Ohjelma saa syötteiksi jokin tekstinpätkän(englanniksi alustavasti) ja palauttaisi korjatun tekstipätkän ja siinä olisi listana vieressä alkuperäiset virheelliset sanat ja siitä korjatut sanat ja käyttäjä pystyisi valita, minkä korjatun sanan se haluaa ottaa mukaan tekstipätkään. Voi olla, että tämä muuttuu projektin edetäessä. Jos kerkeän, niin tekstipätkään virhelliset sanat olisi erivärisellä.
- Aikavaativuutena algoritmille olisi O(mn) ja tietorakenteelle O(n). Tilavaativuus algoritmille ja tietorakenteelle olisi O(nm).
- Lähteenä on Chatgpt, wikipedia ja Geeksforgeeks.
- Olen tietojenkäsittelytieteen kandidaatti.
- Dokumentaatiossa käytetään suomen kieltä.