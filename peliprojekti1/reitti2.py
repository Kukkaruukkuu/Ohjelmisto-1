#TÄNNE REITTI 2 JA SEN VALINNAT

def reitti2():
    print("reitti 2 - täällä valitaan a vai b")
    print("valitse reitti a tai b")
    y = input("> ")
    if y == "1":
        reitti2_a()
    if y == "1":
        reitti2_b()

def reitti2_a():
    print()
    print("reitti 2 a - lose, jää jumiin huoneeseen eikä pääse pois - ded")
    print("kysyy takaisin alkuun vai takaisin reitti 2 alkuun")
    print("1: takaisin reitin alkuun")
    print("2: luovuta")
    ya = input("> ")
    if ya == "1":
        reitti2()
    if ya == "2":
        quit()

def reitti2_b():
    print("reitti 2 b - selvitä koodi ja pääse ulos")
    print("koodi salasanaan puuttuu vielä, vapaa pääsy :DD ")
    print("WIN")
    print("Sulje peli tai palaa alkuun etsimään muutkin lopetukset")
    # yy = input(print">" )


