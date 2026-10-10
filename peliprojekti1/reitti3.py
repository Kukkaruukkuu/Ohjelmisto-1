#TÄNNE REITTI 3 JA SEN VALINNAT

#IMPORTIT
import time
from user import user_nimi
import hahmot
from hahmot import purema
from hahmot import kirves
from peli import reppu

#PELAAJA JA VIHU
pelaaja = hahmot.Pelaaja(nimi = user_nimi, health = 50)
vihu = hahmot.Vihu(nimi = "Vihu", health = 50, ase = purema)

#PELI - REITTI 3
def reitti3():
    print("reitti 3 - täällä valitaan a vai b")
    print("kuulet omituista ääntä edestä päin.")
    print("1: mene ääntä kohti")
    print("2: yritä kiertää ääni hiljaa")
    paatos = input("> ")
    if paatos == "1":
        reitti3_a()
    if paatos == "2":
        reitti3_b()
    else:
        paatos = input("> ")

#REITTI 3 - A
def reitti3_a():
    print("reitti 3 a - win, taistelun kautta hissille")
    print("näkee kirveen, otatko sen")
    print("1: nosta kirves")
    print("2: jätä kirves")

    nosta = input("> ")
    if nosta == "1":
        pelaaja.ota(hahmot.kirves)
        print("nostat kirveen. Ehkä tälle on käyttöä myöhemmin.")
        reppu.append("kirves")
        print(reppu)
        print()
    if nosta == "2":
        print("jätät kirveen paikalleen. Et usko, että tarvitset sitä mihinkään.")
        print()
    else:
        nosta = input("> ")

    time.sleep(2)
    print("kävelet syvemmälle labraan. Kuulet äänen jostakin. Ihan niinkuin.... murinaa?")
    time.sleep(2)
    print("Liikut lähemmäksi ja eteesi astuu jokin olio...")
    time.sleep(1)
    print("se ei näytä ystävälliseltä....")
    pelaaja.healthbar.bar()
    vihu.healthbar.bar()
    print()
    print("Valmistaudut taistoon!")
    print()
    time.sleep(3)

    while True:
        print("(paina nappia edetäksesi)")
        pelaaja.attack(vihu)
        vihu.attack(pelaaja)
        pelaaja.healthbar.bar()
        vihu.healthbar.bar()
        input("> ")
        if vihu.health == 0:
            print("päihitit olion")
            break
        if pelaaja.health == 0:
            print("hävisit")
            break
        
#REITTI 3 - B
def reitti3_b():
    print("reitti 3 b - lose, yrittää ohitta taistelun ja kuolee.")
    print("kysyy takaisin alkuun vai takaisin reitti 3 alkuun")
