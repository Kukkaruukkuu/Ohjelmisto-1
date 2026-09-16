#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon 
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä 
# suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille 
# argumentiksi reverse=True.

numerot = []

while True:
    luku = (input("Anna ensimmäinen luku tai lopeta painamalla Enter: "))
    numerot.append(luku)
    if luku == "":
        break
numerot.remove("")
numerot.sort(key=int , reverse=True)

print(numerot[0:5])
