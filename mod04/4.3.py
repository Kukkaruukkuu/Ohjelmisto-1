# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

# sukupuoli = int(input("Anna biologinen sukupuolesi: "))
# hemoglob = int(input("Anna hemoglobiiniarvo (g/l)"))

sukupuoli = (input("Anna biologinen sukupuolesi: "))
if sukupuoli == "nainen":
    hemoglob = (input("Anna hemoglobiiniarvo (g/l): "))
if (sukupuoli == "nainen" and hemoglob <= "175" or hemoglob >= "117"):
    print("Hemoglobiini on normaali.")
elif (sukupuoli == "nainen" and hemoglob < "117"):
    print("Hemoglobiini on alhainen")
elif (sukupuoli == "nainen" and hemoglob > "175"):
    print("Hemoglobiini on korkea")

# or sukupuoli== "mies":