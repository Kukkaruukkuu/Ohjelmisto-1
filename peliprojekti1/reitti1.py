#TÄNNE REITTI 1 JA SEN VALINNAT
import menu
reppu = []

# def invi():
#     reppu = []
#     print(f'''
#     Repun sisältö:
#     --------------
#     {reppu}''')
#     return


def reitti1():
    print()
    print("tarinaa tarinaa")
    print("löydät avainkortin maasta")
    print("otatko sen?")
    print("1: ota")
    print("2: jätä maahan")
    kortti = input("> ")
    if kortti == "1":
        reppu.append("Avainkortti")
        print(reppu)
        print()
    else:
        pass
    print("reitti 1 - täällä valitaan 1(reitti a) tai 2(reitti b)")
    go = input("mitä teet (1/2)\n> ")
    if go == "1":
        reitti1_a()
    elif go == "2":
        reitti1_b()
    else:
        go = input("mitä teet (1/2)\n>")

def reitti1_a():
    print()
    print("reitti 1 a - lose")
    print("kysyy takaisin reitti 1 alkuun tai voi luovuttaa")
    print("1: Takaisin reitin alkuun")
    print("2: luovuta")
    goa =input("> ")
    if goa == "1":
        reitti1()
    if goa == "2":
        quit()
    else:
        goa =input(">")

def reitti1_b():
    print()
    if "Avainkortti" in reppu:
        print("reitti 1 b - win, pääsit hissille")
        print("jippii peli voitettu")
        print("voit sulkea pelin tai etsiä muut lopetukset aloittamalla alusta.\n  Lopeta peli kirjoittamalla 'sulje'")
        gob = input("> ").lower()
        if gob == "sulje":
            quit()
        else:
            gob = input(">")
    else:
        print("ovi on lukittu. Tarvitset avainkortin")
        print("1: palaa takaisin reitin alkuun")
        print("2: sulje peli")
        x = input("> ")
        if x == "1":
            reitti1()
        elif x == "2":
            quit()
        else:
            x = input("> ")
    