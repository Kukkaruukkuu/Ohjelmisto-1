#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.


def heitto(noppa):
    noppa = input(print("Nopan maksimi lukumäärä: "))
    return noppa

while True:
    luku = heitto(noppa)
    print(f"Nopan heitto: {luku}")
    if luku == noppa:
        break