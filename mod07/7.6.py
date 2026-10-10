#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def lasku(halkaisia, hinta):
    x=float(hinta/(halkaisia**2 * math.pi))
    return x

halkaisia1=float(input("Anna ensimmäisen pizzan halkaisia: "))
hinta1=float(input("Anna ensimmäisen pizzan hinta: "))
halkaisia2=float(input("Anna toisen pizzan halkaisia: "))
hinta2=float(input("Anna toisen pizzan hinta: "))

tulos1= lasku(halkaisia1, hinta1)
tulos2= lasku(halkaisia2, hinta2)

if tulos1<tulos2:
    print("Ensimmäisellä pizzalla on halvempi yksikköhinta")
else: print("Toisella pizzalla on halvempi yksikköhinta")