#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon 
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

numerot = []

while True:
    luku = (input("Anna ensimmäinen luku tai lopeta painamalla Enter: "))
    numerot.append(luku)
    if luku == "":
        break
numerot.remove("")
numerot.sort(key=int)
print(numerot[0])
print(numerot[-1])

    