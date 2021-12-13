# Treenipäiväkirja

Sovellus toimii treenipäiväkirjana urheilun harrastajalle. Nykyisessä muodossaan treenipäiväkirja sopii kenelle tahansa liikunnan harrastajalle, mutta jatkokehityksessä kohdekäyttäjiä ovat taitoluistelun harrastajat.

## Dokumentaatio

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Release viikko 5

[Github-release](https://github.com/Ronttikasa/treenipaivakirja/releases)

## Asennus

Asenna riippuvuudet komennolla

`poetry install`

Suorita ohjelma komennolla

`poetry run invoke start`

Huom. ohjelma tallentaa tietoa tiedostoihin jotka luodaan siinä vaiheessa kun ensimmäiset treeni- ja tavoitemerkinnät tehdään. Tällä hetkellä ohjelma kaatuu jos merkintöjä yrittää tarkastella ennen kuin niitä on tehty. Aloita siis luomalla merkintöjä!

## Komentorivitoiminnot

#### Ohjelman suorittaminen

Suorita ohjelma komennolla

`poetry run invoke start`

#### Testaus

Suorita testit komennolla

`poetry run invoke test`

#### Testikattavuus

Testikattavuusraportin generointi:

`poetry run invoke coverage-report`

Raportti löytyy htmlcov-hakemistosta.

#### Pylint

Tiedostossa .pylintrc määriteltyjen tarkastusten suorittaminen:

`poetry run invoke lint`
