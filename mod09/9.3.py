# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.  Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + muutos
        if float(self.tamanhetkinen_nopeus) > float(self.huippunopeus):
            self.tamanhetkinen_nopeus = self.huippunopeus
        if float(self.tamanhetkinen_nopeus) < 0:
                    self.tamanhetkinen_nopeus = 0
        return muutos

    def kulje(self, kulje):
        kulje > 0
        self.kuljettu_matka = kulje * self.tamanhetkinen_nopeus
        return kulje
    
uusi_auto = Auto("ABC-123", 142, 60)
uusi_auto.kulje(2)

print(f"Uuden auton \nRekisteri numero: {uusi_auto.rekisteritunnus} \nHuippunopeus: {uusi_auto.huippunopeus}\nTämänhetkinen nopeus: {uusi_auto.tamanhetkinen_nopeus}km/h \nKuljettu matka: {uusi_auto.kuljettu_matka}km")
