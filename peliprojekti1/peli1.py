#TÄNNE REITTI 1 JA SEN VALINNAT

#IMPORTIT
import time
import peli2

#INVENTORY
reppu = []

#REITTI 1
def reitti1():
    print()
    print("Suuntaat suoraan hissiä kohti. Ehkä se olisi vielä toiminnassa.")
    time.sleep(1)
    print("Yrität painaa nappia, mutta ovi ei aukea.")
    print()
    print("Voisit ehkä yrittää korjata hissin tai yrittää vielä uudestaan.")
    print("1: Yritä korjata hissi.")
    print("2: Paina nappia vielä kerran.")
    go = input("> ")
    if go == "1":
        reitti1_a()
    elif go == "2":
        reitti1_b()
    else:
        go = input("mitä teet (1/2)\n>")

#REITTI 1 A - (LOSE)
def reitti1_a():
    print()
    print("Tutkit hissiä.")
    print("Ovi on lukittu.")
    print("Yrität ohittaa lukituksen jotenkin.")
    print("Huomaat kahden johdon roikkuvan hissin nappien paneelin alta.")
    print("Yhdistät johdot.")
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
    print("Se ei ollut hirveän viisasta.... sait sähköiskun ja kuolit.")
    print()
    print("Voit palata takaisin reitin alkuun tai luovuttaa ja aloittaa pelin alusta.")
    print("1: Takaisin reitin alkuun")
    print("2: luovuta")
    goa =input("> ")
    if goa == "1":
        reitti1()
    if goa == "2":
        quit()
    else:
        goa =input(">")

#REITTI 1 B - (WIN - kunhan hakee avainkortin reitti 2 kautta)
def reitti1_b():
    print()
    if "Avainkortti" in reppu:
        print("Yrität avata hissin oven avainkortin avulla.")
        print()
        time.sleep(1)
        print("Asetat avainkortin hissin nappien yläpuolelle.")
        print()
        time.sleep(1)
        print("Kuulet 'piip' äänen.")
        print()
        time.sleep(1)
        print("Hissin ovi aukeaa.")
        print()
        time.sleep(1)
        print("Astut hissin sisään ja painat nappia jossa lukee 'PINTA'")
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
        print("Matka ylös tuntui todella pitkältä, mutta hissi pysähtyy ja ovet avautuvat.")
        time.sleep(1)
        print("Hissi täyttyy ovien raosta tulevasta valosta.")
        time.sleep(1)
        print("Sokaistut hetkeksi kirkkaudesta.")
        time.sleep(1)
        print("Avaat silmäsi uudestaan ja häkellyt siitä mitä näet.")
        time.sleep(1)
        print("Pinta... Pääsit pinnalle!")
        time.sleep(1)
        print("Tunnet ensimmäistä kertaa ikinä auringon lämmön ihollasi.")
        print()
        time.sleep(2)
        print("Kiitos kun pelasit!")
        print("Voit sulkea pelin tai etsiä muut lopetukset aloittamalla alusta.\n  Lopeta peli kirjoittamalla 'sulje'")
        gob = input("> ").lower()
        if gob == "sulje":
            quit()
        else:
            gob = input(">")
#REITTI 1 B - siirrytään reitti 2 luokse
    else:
        print("Yrität painaa hissin nappia vielä kerran, mutta mitään ei tapahdu.\nTutkit hissiä tarkemmin.")
        print("Ovi on lukittu.")
        print("Ehkä huoneesta voisi löytyä avain.")
        print()
        print("1: Mene huoneeseen.")
        print("2: Yritä avata hissi")
        x = input("> ")
        if x == "1":
            peli2.reitti2()
        elif x == "2":
            reitti1_a()
        else:
            x = input("> ")
    