# Käyttöohje

## Ohjelman asentaminen

1. Lataa projektin uusin release

2. Asenna ohjelman riippuvuudet
```bash
poetry install
```

## Ohjelman käynnistäminen

1. Navigoi snakegame-hakemistoon ja käynnistä virtuaaliympäristö
```bash
cd snakegame
poetry shell
```

2. Käynnistä ohjelma
```bash
invoke start
```

## Pelaaminen

Ohjelman käynnistyessä näytölle avautuu aloitusnäkymä. Näkymästä voi joko aloittaa uuden pelin painamalla 1, katsella huipputuloksia painamalla 2 tai poistua pelistä painamalla Esc-näppäintä.
Pelin aikana käärmettä voi ohjata nuolinäppäimillä. Tehtävänä on kerätä 100 kirsikkaa, jolloin peli päättyy voittoon. Jos käärme törmää seinään tai itseensä, peli päättyy häviöön. Pelin päätyttyä
omat pisteet voi tallentaa painamalla 2. Pelin saa tauolle painamalla p-näppäintä.
