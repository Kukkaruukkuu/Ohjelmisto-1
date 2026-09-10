#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuumamäärä: "))
sentit = tuuma * 2.54
while tuuma > 0:
    print(f"Tuumamäärä senttimetreinä: {sentit: .2f}cm")
    tuuma = float(input("Anna tuumamäärä: "))
print("Liian pieni tuumamäärä")