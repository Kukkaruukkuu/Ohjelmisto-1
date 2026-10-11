#TÄNNE REITTI 3 JA SEN VALINNAT

#IMPORTIT
import time
from user import user_nimi
import hahmot
from hahmot import purema
from hahmot import kirves


#HAHMOT
pelaaja = hahmot.Pelaaja(nimi = user_nimi, health = 50)
vihu = hahmot.Vihu(nimi = "Vihu", health = 50, ase = purema)

#PELI - REITTI 3
def reitti3():
    print("Yrität lähteä etsimään toista reittiä ulkokautta.")
    print("Ulkona on enemmän valoisaa kuin sisällä joten et jännitä siellä liikkumista niin paljoa.")
    print()
    time.sleep(1)
    print("Yhtäkkiä kuulet omituista ääntä edestä päin.")
    print()
    print("1: Mene ääntä kohti")
    print("2: Yritä kiertää ääni hiljaa")
    paatos = input("> ")
    if paatos == "1":
        reitti3_a()
    if paatos == "2":
        reitti3_b()
    else:
        paatos = input("> ")

#REITTI 3 - A (WIN - kunhan nostaa kirveen)
def reitti3_a():
    print("Liikut hitaasti, mutta päättäväisesti ääntä kohti.")
    print()
    time.sleep(1)
    print("Näet kirveen nojaamassa labran seinää vasten.")
    print()
    print("1: nosta kirves")
    print("2: jätä kirves")

    nosta = input("> ")
    if nosta == "1":
        pelaaja.ota(hahmot.kirves)
        print("Nostat kirveen. Ehkä tälle on käyttöä myöhemmin.")
        print()
    if nosta == "2":
        print("Jätät kirveen paikalleen. Et usko, että tarvitset sitä mihinkään.")
        print()
    else:
        nosta = input("> ")

    time.sleep(2)
    print("Kävelet lähemmäksi ääntä ja kuulet... murinaa?")
    time.sleep(2)
    print("Liikut lähemmäksi ja eteesi astuu jokin olio...")
    time.sleep(1)
    print("Se näyttää koiran ja rotan sekoitukselta...")
    print()
    time.sleep(1)
    print("se ei näytä ystävälliseltä....")
    pelaaja.healthbar.bar()
    vihu.healthbar.bar()
    print()
    print("Valmistaudut taistoon!")
    print()
    time.sleep(3)
#TAISTELU
    while True:
        print("(paina nappia edetäksesi)")
        pelaaja.attack(vihu)
        vihu.attack(pelaaja)
        pelaaja.healthbar.bar()
        vihu.healthbar.bar()
        input("> ")
        if vihu.health == 0:
            print("VOITIT")
            print()
            time.sleep(1)
            print("Päihit olion, mutta et selvinnyt ihan naarmuitta.")
            print()
            time.sleep(1)
            print("Jatkat ulkona kiertelyä ja eteesi ilmestyy portaat.")
            print("Näillä voisi ehkä päästä ylös asti.")
            print()
            time.sleep(1)
            print("Lähdet kiipeämään portaita ylös.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Kiipeämisessä menee kauan, mutta pääset ylös asti.")
            print()
            print("Yläpuolellasi on luukku, jonka lukko on ajan myötä heikentynyt ja saat avattua sen käsin pienellä voimalla.")
            print()
            time.sleep(1)
            print("Nouset luukusta ylös ja sokaistut hetkeksi auringon valosta.")
            time.sleep(3)
            print()
            print("Tunnet auringon lämmön ensimmäistä kertaa ikinä ihollasi.")
            print()
            time.sleep(2)
            print("Kiitos kun pelasit!")
            print("Voit sulkea pelin tai etsiä muut lopetukset aloittamalla alusta.")
            break
        if pelaaja.health == 0:
            print("HÄVISIT")
            print()
            time.sleep(2)
            print("Et saanut päihitettyä oliota...")
            print()
            print("Voit palata reitin alkuun tai luovuttaa")
            print()
            print("1: Takaisin reitin alkuun")
            print("2: Luovuta")
            aaa =input("> ")
            if aaa == "1":
                reitti3()
            if aaa == "2":
                quit()
            else:
                aaa =input(">")
            break


#REITTI 3 - B (LOSE)
def reitti3_b():
    print("Yrität hiipiä äänen ohi mahdollisimman hiljaa.")
    print("Et tiedä mikä ääntä tekee, mutta et halua jäädä selvittämäänkään.")
    print()
    time.sleep(2)
    print("Olet päässyt jo hyvän matkaa eteenpäin kun tajuat ettei ääntä kuulu enään...")
    print()
    print("Käännyt ympäri ja huomaat, että takanasin on jotain.")
    print()
    time.sleep(2)
    print("Et edes ehdi ajatella mikä kimppuusi käy kun on jo liian myöhäistä...")
    print()
    print("Voit palata takaisin reitin alkuun tai luovuttaa.")
    print()
    print("1: Takaisin reitin alkuun")
    print("2: Luovuta")
    aab =input("> ")
    if aab == "1":
        reitti3()
    if aab == "2":
        quit()
    else:
        aab =input(">")
