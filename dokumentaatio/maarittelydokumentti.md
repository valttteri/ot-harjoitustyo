# Määrittelydokumentti

### Sovelluksen tarkoitus
Projektin aihe on matopeli. Pelissä ohjataan matoa pitkin pelialuetta. Pelialueelle ilmestyy "ruokaa", jota keräämällä mato kasvaa pidemmäksi.
Mitä pidemmäksi mato kasvaa, sitä enemmän pelaaja saa pisteitä. Peli päättyy, kun tietty pistemäärä saavutetaan tai mato törmää seinään tai itseensä.

### Perusversion toiminnallisuudet
- Aloitusnäkymä
  - Pelin käynnistyessä avautuu aloitusnäkymä &#x2714;
  - Aloitusnäkymästä voi aloittaa uuden pelin, tarkastella huipputuloksia tai sulkea ohjelman &#x2714;
- Pelaaminen
  - Pelaaja voi ohjata matoa nuolinäppäimillä &#x2714;
  - Pelialueella on "ruokaa", jota pelaaja kerää &#x2714;
  - Mato pitenee aina kun sille syöttää ruokaa &#x2714;
  - Peli päättyy voittoon, jos madosta tulee riittävän pitkä &#x2714;
  - Peli päättyy häviöön, jos mato törmää seinään tai itseensä &#x2714;
  - Kun peli päättyy, pelaaja voi tallentaa omat pisteensä huipputuloksiin &#x2714;
- Taukonäkymä
  - Käynnissä olevan pelin voi laittaa tauolle &#x2714;
  - Taukonäytöltä voi poistua pelistä tai jatkaa meneillään olevaa peliä &#x2714;
- Game Over-näkymä
  - Näytetään kun käärme törmää seinään tai itseensä &#x2714;
  - Näkymästä voi aloittaa uuden pelin tai palata aloitusnäkymään &#x2714;
- Voitto-näkymä
  - Näytetään, kun pelaaja läpäisee tason &#x2714;
  - Näkymästä voi aloittaa uuden pelin tai palata aloitusnäkymään &#x2714;
- Huipputulokset
  - Sivu, jolle on listattu pelissä saavutetut pisteet parhausjärjestyksessä &#x2714;
  - Tulokset tallennetaan SQLite-tietokantaan &#x2714;
- Ulkoasu
  - Pelin ulkoasun näyttää järkevältä &#x2714;

### Jatkokehitysideoita
Perusversion valmistuttua peliin voi lisätä seuraavia ominaisuuksia

- Muita keräiltäviä asioita
  - Parempi ruoka joka pidentää matoa tavallista enemmän
  - Myrkyllinen ruoka, joka lyhentää matoa
  - Ruoka, joka antaa madolle hetkeksi erityisen kyvyn, kuten oman ruumiin läpi kulkemisen kuolematta
- Uusia pelialueita, joihin voi luoda haastetta esimerkiksi seinien ja muiden esteiden avulla.
- Näkymä, jossa voi valita haluamansa pelialueen
- Eri vaikeustasoja
- Kaksinpeli, jossa voi pelata toista ihmistä vastaan
 



