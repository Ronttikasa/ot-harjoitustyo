# Treenipäiväkirja

Sovellus toimii treenipäiväkirjana urheilun harrastajalle. Nykyisessä muodossaan treenipäiväkirja sopii kenelle tahansa liikunnan harrastajalle, mutta jatkokehityksessä kohdekäyttäjiä ovat taitoluistelun harrastajat.

## Dokumentaatio

[Käyttöohje](./dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Testausdokumentti](./dokumentaatio/testausdokumentti.md)

[Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Release (loppupalautus)

[Github-release](https://github.com/Ronttikasa/treenipaivakirja/releases/tag/viikko6) UPDATE THIS

## Asennus

1. Asenna riippuvuudet komennolla

```bash
poetry install
```

2. Suorita ohjelma komennolla

```bash
poetry run invoke start
```

## Komentorivitoiminnot

#### Ohjelman suorittaminen

Suorita ohjelma komennolla:

```bash
poetry run invoke start
```

#### Testaus

Suorita testit komennolla:

```bash
poetry run invoke test
```

#### Testikattavuus

Testikattavuusraportin generointi:

```bash
poetry run invoke coverage-report
```

Raportti luodaan *htmlcov*-hakemistoon.

#### Pylint

Tiedostossa .pylintrc määriteltyjen tarkastusten suorittaminen:

``` bash
poetry run invoke lint
```
