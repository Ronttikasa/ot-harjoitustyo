# Treenipäiväkirja

Sovellus toimii treenipäiväkirjana urheilun harrastajalle. Nykyisessä muodossaan treenipäiväkirja sopii kenelle tahansa liikunnan harrastajalle, mutta jatkokehityksessä kohdekäyttäjiä ovat taitoluistelun harrastajat.

## Dokumentaatio

[Vaatimusmäärittely](.dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Release viikko 5

tähän linkki

## Asennus

Asenna riippuvuudet komennolla

`poetry install`

Suorita ohjelma komennolla

`poetry run invoke start`

## Komentorivitoiminnot

#### Ohjelman suorittaminen

Ensimmäinen käyttökerta viikolla 4: Jos juurihakemistossa on tiedosto trainingjournal.txt, poista se.

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
