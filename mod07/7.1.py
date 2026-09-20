#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heitto():
    x = random.randint (1, 6)
    return x

while True:
    luku = heitto()
    print(f"Nopan heitto: {luku}")
    if luku == 6:
        break
