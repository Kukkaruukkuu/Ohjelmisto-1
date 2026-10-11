#TÄNNE REITTI 2 JA SEN VALINNAT
#IMPORTIT
import time
import peli1
import hahmot
import healthbar
from user import user_nimi
from user import user_ika

#HAHMOT
rotta = hahmot.Rotta(nimi = "Rotta", health = 10, ase = hahmot.purema)
pelaaja = hahmot.Pelaaja(nimi = user_nimi, health = 50)

#REITTI 2
def reitti2():
    print()
    print("Suuntaat kohti huonetta. Täältä ehkä löytyy jotain hyödyllistä.")
    print("Astut sisälle.")
    time.sleep(2)
    print("Huone on ihan sekaisin.")
    print("Rikkoutunutta lasia ja erilaisia papereita ympäri lattiaa.")
    time.sleep(2)
    print()
    print("Huone on pimeä, mutta näet pienen valon pilkkeen taaimmaisella seinällä.")
    time.sleep(1)
    print("Yrität katsoa tarkemmin ja huomaat, että seinää vasten on pöytä jonka päällä on tietokone.")
    print()
    time.sleep(1)
    print("Kuulet pientä vikinää... mistä ihmeestä se tulee...")
    print()
    time.sleep(2)
    print("ROTTA??")
    print("Rotta, mutta se on jotenkin oudon näköinen...")
    print()
    time.sleep(1)
    print("Ennen kuin ehdit edes ajatella asiaa, rotta lähestyy sinua samalla painaen tietokoneen näppäintä.")
    print()
    print("Huoneen ovi sulkeutuu ja lukittuu.")
    print()
    time.sleep(1)
    print("Et pääse enään ulos.")
    print()
    time.sleep(1)
    print("Rotta lähestyy sinua...")
    print()
    time.sleep(1)
    print("Aika puolustautua.")
    time.sleep(2)
    print()
    pelaaja.healthbar.bar()
    rotta.healthbar.bar()
    print()
    time.sleep(3)
#TAISTELU
    while True:
        print("(paina enteriä edetäksesi)")
        pelaaja.attack(rotta)
        rotta.attack(pelaaja)
        pelaaja.healthbar.bar()
        rotta.healthbar.bar()
        input("> ")
        if rotta.health == 0:
            print("VOITTO")
            break
        if pelaaja.health == 0:
            print("hävisit")
            break
    time.sleep(1)
    print()
    print("Rotta oli normaalia paljon suurempi, mutta selvisit silti.")
    print()
    time.sleep(1)
    print("Nyt pitää vain selvittää miten saat huoneen oven auki ja ulos.")
    print()
    time.sleep(2)
    print("Katsot tietokoneen näytölle.")
    print('''
        Kirjoita koodi ovien aukaisua varten
                    3 YRITYSTÄ''')
    salasana = input("> ")
    yritykset = 1
    while yritykset < 3:
        if salasana == "salasana":
            print("Lukitus avattu!")
            break
        yritykset = yritykset + 1
        print("Väärä koodi!")
        print('''
        Kirjoita koodi ovien aukaisua varten
                    3 YRITYSTÄ
                   vihje: salasana''')
        salasana = input("> ")
    else: 
        print("Yritykset käytetty")
        reitti2_a()
    reitti2_b()

#REITTI 2 - A (LOSE)
def reitti2_a():
    print()
    print("Vaikka yritit kovasti avata ovea se ei millään aukea...")
    print("Nostat tuolin pöydänluota ja olet heittämässä sitä ovea päin...")
    print()
    time.sleep(1)
    print("Huomaat jaloissasi savua....")
    time.sleep(1)
    print("Tuloi putoaa otteestasi ja lyyhistyt maahan...")
    print("Pitelet kurkkuasi ja sinun on vaikea hengittää...")
    print()
    time.sleep(1)
    print("Silmissäsi pimenee...")
    time.sleep(2)
    print("Voit palata takaisin reitin alkuun tai luovuttaa.")
    print()
    print("1: Takaisin reitin alkuun")
    print("2: Luovuta")
    ya = input("> ")
    if ya == "1":
        reitti2()
    if ya == "2":
        quit()

#REITTI 2 - B (WIN)
def reitti2_b():
    print("Onnistuit saamaan oven auki.")
    print("Huokaiset helpotuksesta. Ajatus huoneeseen jäämisestä vie hetken toipua")
    time.sleep(3)
    print("Huomaat, että pöydällä on avainkortti.")
    print()
    time.sleep(1)
    print("Otat sen ja laitat sen reppuusi.")
    peli1.reppu.append("Avainkortti")
    print(peli1.reppu)
    time.sleep(2)
    print()
    print("Palaat hissille.")
    time.sleep(1)
    peli1.reitti1_b()


