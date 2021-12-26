# Testausdokumentti

# JÄRJESTELMÄTESTAUS PUUTTUU

Ohjelmaa on testattu unittestilla automatisoiduin testein sekä manuaalisilla järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavat luokat `EntryService` treenipäiväkirjatoiminnallisuuden, `GoalService` tavoitteiden ja `StatsService` tilastotoiminnallisuuden osalta.

Luokkaa `EntryService` testataan [TestEntryService](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/services/entry_service_test.py)-testiluokalla. `EntryService`-olio on testauksessa alustettu niin, että sille on injektoitu valekomponenttina repositorio-oliot jotka tallentavat tietoa muistiin tekstitiedoston sijasta. Tähän tarkoitukseen testeissä on käytetty luokkaa `FakePracticeRepository`.

Luokkaa `GoalService` testataan [TestGoalService](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/services/goal_service_test.py)-luokalla. Kuten edellä, `GoalService`-oliolle on injektoitu riippuvuutena valekomponentti; muistiin tallentava `FakeGoalRepository`-olio.

Luokkaa `StatsService` testataan [TestStatsService](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/services/stats_service_test.py)-testiluokalla. Myös tämän luokan testauksessa käytetään valekomponenttina luokan `FakePracticeRepository` oliota.

### Repositorio-luokat

Repositorio-luokkien `PracticeRepository` ja `GoalRepository` testauksessa käytetään pelkästään testeissä käytössä olevia tiedostoja, joiden nimet voidaan konfiguroida *.env.test*-tiedostossa. `PracticeRepository`-luokkaa testataan testiluokalla [TestPracticeRepository](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/repositories/practice_repository_test.py) ja `GoalRepository`-luokkaa testiluokalla [TestGoalRepository](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/repositories/goal_repository_test.py).

### Goal- ja Practice-luokat

Sovellus käsittelee tiedostoon talletettavaa tietoa `Goal`- ja `Practice`-luokkien olioina. Näitä luokkia testataan [TestGoal](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/entities/goal_test.py)- ja [TestPractice](https://github.com/Ronttikasa/treenipaivakirja/blob/master/src/tests/entities/practice_test.py)-testiluokilla.

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 97%. Käyttöliittymän koodi ei ole mukana testauksessa.

![](./kuvat/test_coverage.png)


## Järjestelmätestaus

Sovellusta on testattu manuaalisesti järjestelmätasolla.

### Asennus ja konfigurointi

Sovellus on asennettu ja testattu käyttöohjeessa kuvatulla tavalla Windows- ja Linux-ympäristöissä. Testauksessa on myös muutettu tallennukseen käytettävien tiedostojen nimiä *.env*-tiedoston kautta.

Sovellusta on testattu sekä niin että tallentamiseen käytettävät tiedostot ovat olleet valmiiksi olemassa, että niin että ohjelma on luonut ne automaattisesti.

### Toiminnallisuudet

Järjestelmätestauksessa on käyty läpi määrittelydokumentissa ja käyttöohjeessa mainitut toiminnallisuudet. Testauksen yhteydessä on yritetty antaa myös virheellisiä syötteitä, kuten väärässä muodossa olevia kellonaikoja ja tyhjiä syötteitä.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna järkevää virheilmoitusta mikäli konfiguraatiotiedostossa määriteltyihin tiedostoihin ei ole luku- tai kirjoitusoikeuksia.
