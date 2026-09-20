#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, muutos):
        if muutos <= 0:
            self.tamanhetkinen_nopeus += muutos
        else: 
            self.tamanhetkinen_nopeus += muutos
            
        
       
uusi_auto = Auto("ABC-123", "142 km/h")
uusi_auto.kiihdyta(30)
print(uusi_auto.tamanhetkinen_nopeus)
uusi_auto.kiihdyta(70)
print(uusi_auto.tamanhetkinen_nopeus)
uusi_auto.kiihdyta(50)
print(uusi_auto.tamanhetkinen_nopeus)
uusi_auto.kiihdyta(-200)
print(uusi_auto.tamanhetkinen_nopeus)

print(f"Uuden auton \nRekisteri numero: {uusi_auto.rekisteritunnus} \nHuippunopeus: {uusi_auto.huippunopeus}\nTämänhetkinen nopeus: {uusi_auto.tamanhetkinen_nopeus}km/h \nKuljettu matka: {uusi_auto.kuljettu_matka}km")
