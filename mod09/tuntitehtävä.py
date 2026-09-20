
class Pelihahmo:
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

pelaaja1 = Pelihahmo("Mario")

print(f"Nimi: {pelaaja1.nimi}")
print(f"Elämät: {pelaaja1.elämät}")
print(f"Kolikot: {pelaaja1.kolikot}")
print(f"Pisteet: {pelaaja1.pisteet}")


class Merirosvolaiva:
    def __init__(self, nimi, tykkien_maara, miehiston_maara, kulta=0):
        self.nimi = nimi
        self.tykkien_maara = tykkien_maara
        self.miehiston_maara = miehiston_maara
        self.kulta = kulta

    def loyda_aarre(self, maara):
        self.kulta += maara

    