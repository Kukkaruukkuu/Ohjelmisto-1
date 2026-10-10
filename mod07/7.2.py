#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

maksimi = int(input("Nopan maksimi lukumäärä: "))

def heitto():
    heitto=random.randint(1,maksimi)
    return heitto

while True:
    luku = heitto()
    print(f"Nopan heitto: {luku}")
    if luku == maksimi:
        break