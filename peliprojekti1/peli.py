#SAVE
with open("C:\\Users\\milla\\Documents\\Python-harjoitukset\\peliprojekti1\\intro.txt","r") as tiedosto:
    data = tiedosto.read()
    print(data)

#IMPORTIT
import time
import user
import menu
import reitti1
import reitti2
import reitti3
import save


#INVENTORY
reppu = []

#PELI
menu.menu()
time.sleep(2)
print()
print("lets go")
print("1: Menee reitti 1")
print("2: Menee reitti 2")
print("3: Menee reitti 3")
valinta = input(f"Mitä teet {user.user_nimi} (1/2/3)\n> ").lower()
if valinta == "save":
    save.save()
if valinta == "1":
    reitti1.reitti1()
elif valinta == "2":
    reitti2.reitti2()
elif valinta == "3":
    reitti3.reitti3()
else:
    valinta = input("Mitä teet (1/2/3)\n>")
