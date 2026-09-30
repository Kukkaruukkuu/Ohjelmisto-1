# Ohjelmisto 1 - Peliprojekti

NIMI??

**Milla Sundell**

# Ideoita

MAP?? mappi funktio jonka kautta näkis kartan koko alueesta? näkyiskö pelihahmo vai ei? Kartta vois olla piirretty viivoilla, [], yms
    piilotettuja huoneita?

Useampi eri huone?
    osasta voi kuolla/game over tai jos kuolee niin palata paikkaan ennen kuolemaa?

Huoneet jotka tarttee tietyn asian jotta voi kulkea sitä kautta. Esim avain, torchi pimeässä huoneessa.

Inventori jossa on painoraja? Inviin vois lisätä/poistaa tavaraa, vois saada listan mitä siellä on. Kaikilla tavaroilla oma paino?

Vaikeustaso??

KARTTA:
 --------------------------------------------------------
 |         --------     --------     --------     ----  |
 |        |   1    |---|    2   |---|    4   |---|  6 | |
 |         --------     --------     --------     ----  |
 |        /                  |             |            |
 |    -----               --------      --------        |
 |   |ALKU |             |   3    |    |    5   |       |
 |    -----               --------      --------        |
 |                                           |          |
 |                                          ---         |
 |                                         |WIN|        |
 |                                          ---         |
 --------------------------------------------------------           

Maailma jossa ihmiset on muuttanu ilmastonmuutoksen takia maan alle.
Muutosta on yli (hyvin monta vuotta). Kukaan elävä ihminen ei ole käynyt maan pinnalla, mutta huhuja kuitenkin sinne pääsystä on.
Huhujen mukaan erään labran sisällä sijaitsee hissi jonka avulla kulku maan pinnalle olisi mahdollista.


# Projektin teko
Luotu tiedosto joka kysyy nimen ja iän

Tehty while joka estää pelaajaa pelaamasta jos on alle 12v
Jos pelaaja on 12 tai yli niin aukeaa menu.

Menusta pääsee tällä hetkellä starttiin, ohjeisiin ja sulkemaan pelin.

Peli_roinat tiedostossa on sekalaisesti classeja ja funktioita.
Pitää vielä siivota ja laittaa vaikka omiin tiedostoihin.

Tehty inventory lista ja tätä varten tehty funktio joka lisää listaan tavaran.
Inventory print löytyy status funktiosta.

# TIEDOSTOJEN RAKENNE

peli.py on päätiedosto jossa peli pelataan. Sinne importataan musita tideot.

peli_menu.py sisältää menu tiedot ja funktiot.

peli_roinat.py sisältää vielä sekalaisesti funktioita, classejä ja muita juttuja. Nämä todnäk siirrellään muualle kunhan peliä tehdään eteenpäin.

peli_user.py sisältää pelaajan antamat tiedot, pelaaja classin sekä inventaario listan ja pelaajan statuksen josta näkee inventaarion, healthin yms.
