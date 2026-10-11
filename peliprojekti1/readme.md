## Ohjelmisto 1 - PELIPROJEKTI ##

LABRA

**Milla Sundell**

Aikaisempi oli niin sekava niin piti alottaa alusta.

PROJEKTITEHTÄVIEN 1-4 PALAUTUKSET ON NYT SIIRTYNYT UUDEN PROJEKTIKANSION ALLE!
Eli kaikki Omaan palautetut linkit ovat ns. vanhoja paitsi tehtävä 5.

# IDEOITA

kolme eri reittiä päästä loppuun, mutta kaikki ei vie voittoon.

näiden kolmen sisälle lisää vaihtoehtoja?

käytä time sleeppiä, jos mahdollista niin kirjaimia yksitellen?

combat? esim 3a taistelun kautta voittoon?

TARINA:
Kestävä kehitys pitää olla osana.
Portal/FallOut/Stray inspiroima maanalainen asutus josta hissillä ylös?
Roskien keruu valintapeli?
Puhetta?
Kestäväkehitys:
Ilmastonmuutos ja sen tuottama tuho maapallolle.

# TIEDOSTOJEN RAKENNE

PELI:
    Pelin pää tiedosto jonka kautta peli pelataan on peli.py. Tämä tiedosto pidetään selkeänä ja ns puhtaana.

REITIT:
    Eri reiteille on omat tiedostot johon rakentuu reittien rakenne.

CLASSIT:
    hahmot.py tiedostossa on hahmo classi josta on luotu pelaajalle oma classi ja vihulle oma classi. Hahmo classistä löytyy myös ase class jonka sisällä on toiminta aseen nostamiseen ja jättämiseen.
    healthbar.py sisällä on hahmo classin healthbar eli elämien seuraaminen. Healthbar toimii hahmo ja ase classien kanssa combat systeeminä kun pelaaja valitsee reitin 3.

MENU:
    Menun sisällä on omat funktiot. Pelin sulkeminen, aloittaminen ja tallentaminen.

USER:
    user.py tiedot kysytään ihan ensimmäisenä kun peli aloitetaan. Siellä kysytään nimi ja ikä.

SAVE:
    Save.py kautta löytyy tallentaminen joka viedään json tiedostoon. Tätä pitää vielä korjailla koska tällä hetkellä tallentuu vain pelaajan nimi ja ikä eikä esim mihin kohtaan peliä pelaaja jäi.

# JUTTUJA

tehty json ja tallennus toiminto. 9.10.2026
tehty combat-systeemi ja classeja. 11.10.2026
viimeistelty peli 11.10.2026

# REITTIEN RAKENNE

|ALOITUS|
    ---|reitti 1|
            |reitti 1a|>> Kuolema >> LOSE
            
            |reitti 1b|>> ei avainkorttia >> reitti 2
                |reitti 1b|>> avainkortti >> WIN

    ---|reitti 2|
            |reitti 2a|>> ei saa ovea auki >> Kuolema >> LOSE

            |reitti 2b|>> saa oven auki >> avainkorrti >> reitti 1b >> WIN

    ---|reitti 3|
            |reitti 3a|>> ei nosta kirvestä >> kuolee >> LOSE
                |reitti 3a|>> nostaa kirveen >> WIN

            |reitti 3b|>> yrittää hiipiä >> kuolema >> LOSE