#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).

user = str(input("Anna käyttäjätunnus: "))
salasana = str(input("Anna salasana: "))
yritykset = 1
while yritykset < 5:
    if user == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    yritykset = yritykset + 1
    print("Käyttäjätunnus tai salasana väärin.")
    user = str(input("Anna käyttäjätunnut: "))
    salasana = str(input("Anna salasana: "))
else:
    print("Pääsy evätty")
