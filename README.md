# Aineopintojen harjoitustyö: ohjelmistotekniikka

Tämä on repositorio kurssille **Ohjelmistotekniikka TKT20018.** Projektin aiheena on matopeli. Pelissä ohjataan matoa nurmikentällä, jolle on ripoteltu kirsikoita.
Mato kasvaa sitä mukaa kun sille syöttää kirsikoita. Pelin voittaa, kun mato on kasvanut riittävän pitkäksi.

## Dokumentaatio

- [Käyttöohje](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Määrittelydokumentti](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Tuntikirjanpito](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Testaus](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)
- [Releases](https://github.com/valttteri/ot-harjoitustyo/releases)

## Asentaminen

1. Aloita asentamalla repositorio laitteellesi. Siirry snakegame-hakemistoon ja asenna riippuvuudet:
```bash
cd snakegame
poetry install
```

2. Käynnistä virtuaaliympäristö
```bash
poetry shell
```

3. Käynnistä sovellus
```bash
invoke start
```

## Testaaminen

Sovelluksen testit voi suorittaa komennolla
```bash
invoke test
```

Testikattavuusraportin saa luotua komennolla
```bash
invoke coverage-report
```

## Pylint
Koodin kirjoitusasun voi tarkastaa komennolla
```bash
invoke lint
```
