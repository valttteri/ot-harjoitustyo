# Changelog

## Viikko 3
#### Komponentit
- Lisätty Loop-luokka, joka käynnistää pelisilmukan
- Lisätty LevelHandler-luokka, joka generoi pelattavan tason
- Lisätty Snake-luokka, joka vastaa pelattavan käärmeen toiminnasta
- Lisätty Wall-luokka, jonka avulla voi luoda pelialueelle seiniä

#### Sovelluslogiikka
- Pelissä on yksi taso, joka aukeaa pelin käynnistymisen yhteydessä
- Käärmettä voi ohjata nuolinäppäimellä
- Käärmettä voi kasvattaa painamalla g-näppäintä. Tämä muuttuu kun peliin lisätään keräiltävä ruoka
- Jos käärme törmää seinään tai itseensä, se siirtyy takaisin pelialueen keskelle
- Pelin voi sulkea ESC-näppäimellä

#### Testit
- Käärme generoidaan oikeisiin koordinaatteihin käynnistyksen yhteydessä
- Käärme voi liikkua pelialueella jokaiseen suuntaan ja se liikkuu oikean mittaisen matkan kerrallaan
- Käärme ei voi kääntyä menosuuntaansa nähden päinvastaiseen suuntaan
- Käärmettä voi kasvattaa
- Ohjelma huomaa, jos käärme törmää itseensä

## Viikko 4
#### Komponentit
- Food-luokka, jonka avulla voi generoida pelialueelle ruokaa
- Score-luokka, jonka avulla voi seurata pelaajan pisteitä
- Uudet grafiikat: pelialuetta ympäröi kiviseinä ja käärmeelle tarjotaan kirsikoita
- GameStates-luokka, joka hallinnoi pelin eri tiloja
- Displays-hakemisto, josta haetaan aloitus- tauko- ja peli ohi- näkymät

#### Sovelluslogiikka
- Pelialueella on yksi ruoka kerrallaan
- Käärmettä voi kasvattaa syömällä ruokaa
- Kun ruoka syödään, sille arvotaan uusi paikka pelialueelta
- Ruoan syöminen kasvattaa pelaajan pisteitä, jotka näkyvät näytön ylänurkassa
- Pelin käynnistyessä avautuu aloitusnäkymä, josta voi aloittaa uuden pelin
- Pelin saa tauolle painamalla p-näppäintä
- Peli päättyy, kun käärme törmää seinään tai itseensä
- Pelin päätyttyä voi palata takaisin aloitusnäkymään tai aloittaa uuden pelin

#### Testit
- Käärme siirtyy oikealle paikalle, kun kutsutaan reset_snake-funktiota
- Nyt invalid_direction_change-testi käy läpi jokaisen kielletyn suunnanmuutoksen
- Pelisilmukan testaaminen aloitettu

## Viikko 5
#### Komponentit
- Voittonäkymä
- Huipputulokset-näkymä
- Renderer-luokka, joka renderöi kaikki pelin grafiikat
- Uudet grafiikat: Käärme näyttää nyt käärmeeltä ja se liikkuu nurmikolla

#### Sovelluslogiikka
- Peli päättyy voittoon kun käärme kasvaa riittävän pitkäksi
- Pelin päättyessä voittoon avautuu voittonäkymä
- Voittonäkymästä voi aloittaa uuden pelin, palata aloitusnäkymään tai tallentaa pisteet
- Game over- näkymästä voi myös tallentaa pisteet
- Huipputulokset-näkymässä on listattu kaikki saman pelikerran aikana tallennetut pisteet

#### Testit
- Pelisilmukan testikattavuutta laajennettu
- GameStateHandlerin testaaminen aloitettu

## Viikko 6
#### Komponentit
- Database-luokka, joka kommunikoi SQLite-tietokannan kanssa

#### Sovelluslogiikka
- Huipputulokset tallennetaan SQLite-tietokantaan

#### Testit
- Testikattavuutta kasvatettu ~40 prosentista ~75 prosenttiin
- Levelhandlerille on nyt testejä
