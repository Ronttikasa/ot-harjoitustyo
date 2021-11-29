# Ohjelmistotekniikan harjoitustyö

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/Ronttikasa/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Ronttikasa/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

### Asennus

Asenna riippuvuudet komennolla

`poetry install`

### Komentorivitoiminnot

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