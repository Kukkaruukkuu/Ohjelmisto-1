#IMPORTIT
import healthbar

#ASE CLASS
class Ase:
    def __init__(self, nimi, damage):
        self.nimi = nimi
        self.damage = damage

#ASEET
nyrkit = Ase("nyrkit", 3)
kirves = Ase("kirves", 10)
purema = Ase("purema", 5)

#HAHMO CLASS
class Hahmo:
    def __init__(self, nimi, health):
        self.nimi = nimi
        self.health = health
        self.health_max = health
        self.ase = nyrkit

    def attack(self, kohde):
        kohde.health -= self.ase.damage
        kohde.health = max(kohde.health, 0)
        kohde.healthbar.muutos()
        print(f"{self.nimi} teki {self.ase.damage} vahinkoa {kohde.nimi} käyttämällä asetta {self.ase.nimi}.")

#PELAAJA CLASS
class Pelaaja(Hahmo):
    def __init__(self, nimi, health):
        super().__init__(nimi, health)

        self.default_ase = self.ase
        self.healthbar = healthbar.HealthBar(self, color = "green")

    def ota(self, ase):
        self.ase = ase
        print(f"{self.nimi} käyttää nyt asetta {self.ase.nimi}!")

    def tiputa(self):
        print(f"{self.nimi} tiputti aseen {self.ase}!")
        self.ase = self.default_ase

#VIHU CLASS
class Vihu(Hahmo):
    def __init__(self, nimi, health, ase):
        super().__init__(nimi, health)
        self.ase = ase

        self.healthbar = healthbar.HealthBar(self, color = "red")