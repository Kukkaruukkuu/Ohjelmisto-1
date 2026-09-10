#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia 
# arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
import math

kuutio = float(input("Kuinka monta arpakuutiota heitetään? "))
heitot = 0
summa = []

while heitot < kuutio:
    luku = random.randint(1, 6)
    heitot = heitot + 1
    summa.append(luku)
    tulos = sum(summa)
for luku in summa:
    print(f"Arpakuutioiden luvut: {luku}")
print("Lukujen summa: ", tulos )

