# Changelog

## Viikko 3
#### Komponentit
- Lisätty Loop-luokka, joka käynnistää pelisilmukan
- Lisätty LevelGenerator-luokka, joka generoi pelattavan tason
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