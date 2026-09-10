#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvaa = float(input("Arvaa luku: "))
luku = random.randint(1, 10)
while arvaa != luku:
    if (arvaa < luku):
        print("Liian pieni arvaus")
        arvaa = float(input("Arvaa luku: "))
    elif (arvaa > luku):
        print("Liian suuri arvaus")
        arvaa = float(input("Arvaa luku: "))
print("Oikein arvattu!")