# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


sukupuoli = input("Anna biologinen sukupuolesi: ").lower()
if sukupuoli == "nainen" or sukupuoli == "mies":
    hemoglob = (input("Anna hemoglobiiniarvo (g/l): "))
    if (sukupuoli == "nainen" and hemoglob < "117"):
        print("Hemoglobiini on alhainen")
    elif (sukupuoli == "nainen" and hemoglob > "175"):
        print("Hemoglobiini on korkea")
    elif (sukupuoli == "mies" and hemoglob < "134"):
        print("Hemoglobiini on alhainen")
    elif (sukupuoli == "mies" and hemoglob > "195"):
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali.")
else:
    print("Ei tunnistettu")

