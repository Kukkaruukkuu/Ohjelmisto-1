## Ohjelmisto 1 - PELIPROJEKTI ##

pelin nimi tähän

**Milla Sundell**

Aikaisempi oli niin sekava niin piti alottaa alusta.

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

# RAKENNE

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
    user.py tiedot kysytään ihan ensimmäisenä kun peli aloitetaan. Siellä kysytään nimi ja ikä. Molempia pitää vielä korjata koska nyt jos esim vahingossa painaa enteriä niin peli joko menee eteenpäin tai lopettaa kokonaan.

SAVE:
    Save.py kautta löytyy tallentaminen joka viedään json tiedostoon. Tätä pitää vielä korjailla koska tällä hetkellä tallentuu vain pelaajan nimi ja ikä eikä esim mihin kohtaan peliä pelaaja jäi.

# JUTTUJA

tehty json ja tallennus toiminto. 9.10.2026
tehty combat-systeemi ja classeja. 11.10.2026
peli tarttee vielä nimen ja tarinan koodin ympärille.
2 reitti puuttuu vielä kokonaan. Sinne vois tehä koodinpurku tms.
Pitää myös korjata kaikkien inputtien kohdalla elset.