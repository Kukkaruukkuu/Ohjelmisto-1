#SAVE
with open("C:\\Users\\milla\\Documents\\Python-harjoitukset\\peliprojekti1\\intro.txt","r") as tiedosto:
    data = tiedosto.read()
    print(data)

#IMPORTIT
import time
import user
import menu
import peli1
import peli2
import peli3
import save

#PELI
menu.menu()
time.sleep(2)
print()
print("Astut sisälle labraan.")
print("Sisällä on pimeää. Lattia on täynnä rikkinäistä lasia, paperia ja muuta roinaa.")
print("Huonekaluja on ympäriinsä. Tuoleja kaadettu ja pöytiä rikottu.")
print("Kaikki mahdollinen arvotavara on jo varastettu.")
print()
time.sleep(1)
print("Kuljet syvemmälle labraan.")
time.sleep(2)
print()
print("Päädyt hissille, josta todennäköisesti pääsee pinnalle. Näet myös pimeän huoneen. Voisit myös palata takaisin ja koittaa ulkokautta.")
print()
time.sleep(2)
print("Kolme mahdollista reittiä edetä.")
print()
print("1: Mene suoraan hissiä kohti.")
print("2: Tutki huone.")
print("3: Mene ulkokautta.")
valinta = input(f"Mitä teet {user.user_nimi} (1/2/3)\n> ").lower()
if valinta == "save":
    save.save()
if valinta == "1":
    peli1.reitti1()
elif valinta == "2":
    peli2.reitti2()
elif valinta == "3":
    peli3.reitti3()
else:
    valinta = input("Mitä teet (1/2/3)\n>")
