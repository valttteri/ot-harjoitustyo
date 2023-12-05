# Aineopintojen harjoitustyö: ohjelmistotekniikka

Tämä on repositorio kurssille **Ohjelmistotekniikka TKT20018.** Projektin aiheena on matopeli. Pelissä ohjataan matoa nurmikentällä, jolle on ripoteltu kirsikoita.
Mato kasvaa sitä mukaa kun sille syöttää kirsikoita. Pelin voittaa, kun mato on kasvanut riittävän pitkäksi.

## Dokumentaatio

[Määrittelydokumentti](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/maarittelydokumentti.md)

[Tuntikirjanpito](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/valttteri/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/valttteri/ot-harjoitustyo/releases/tag/v1.0.0)

## Käyttöohje

1. Asenna riippuvuudet:
```bash
poetry install
```

2. Käynnistä virtuaaliympäristö
```bash
poetry shell
```

3. Käynnistä sovellus
```bash
poetry run invoke start
```

## Testaaminen

Sovelluksen testit voi suorittaa komennolla
```bash
poetry run invoke test
```

Testikattavuusraportin saa luotua komennolla
```bash
poetry run invoke coverage-report
```

## Pylint
Koodin kirjoitusasun voi tarkastaa komennolla
```bash
poetry run invoke lint
```



