# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.  Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random

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
        self.kuljettu_matka += kulje * self.tamanhetkinen_nopeus
        return kulje
    
uusi_auto = Auto("ABC-123", 142, 60)
uusi_auto.kulje(2)

autot =[]

#Autot luodaan
for x in range(1,11):
    autot.append(Auto(f"ABC-{[x]}", random.randint (100,200)))

voittaja = False

while voittaja !=True:
    for x in range(len(autot)):
        autot[x].kiihdyta(random.randint(-10, 15))

    for x in range(len(autot)):
        autot[x].kulje(1)

    for x in range(len(autot)):
        if autot[x].kuljettu_matka >= 10000:
            print(f"{autot[x].rekisteritunnus} on voittanut kilpailu")
            voittaja = True
        
print("")
for x in range(len(autot)):
    print(autot[x].rekisteritunnus,autot[x].huippunopeus, autot[x].tamanhetkinen_nopeus, autot[x].kuljettu_matka)