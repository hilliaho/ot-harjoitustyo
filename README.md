# Tetris

Sovelluksen avulla käyttäjä voi pelata Tetris-peliä.

## Pelin ohjeet

Pelin aikana pelikentälle ilmestyy Tetromino-palikoita, jotka putoavat alaspäin. Tetromino-palikoita voi liikuttaa nuolinäppäimillä vasemmalle ja oikealle, kääntää ylänuolinäppäimellä, pudottaa nopeammin alanuolinäppäimellä ja pudottaa saman tien välilyönnillä. Tetrominoja ohjaillaan toistensa lomaan ja yritetään saada rivi täyteen, jolloin täysi rivi tyhjenee ja kentälle tulee lisää tilaa. Peli päättyy, kun uusi tetromino ei enää mahdu pelikentälle.

## Viikon 7 release

[Release](https://github.com/hilliaho/ot-harjoitustyo/releases/tag/viikko7)

## Dokumentaatio

[Käyttöohje](https://github.com/hilliaho/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/hilliaho/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/hilliaho/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/hilliaho/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/hilliaho/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

## Komentorivitoimintoja

Riippuvuuksien asennus: `poetry install`

Sovelluksen käynnistys: `poetry run invoke start`

Testien suoritus: `poetry run invoke test`

Testikattavuusraportin luominen: `poetry run invoke coverage-report`

Pylint-tarkistus: `poetry run invoke lint`
