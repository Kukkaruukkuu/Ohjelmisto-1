# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen 
# sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä 
# if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.

# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hytti_luokka = input("Kerro hyttiluokkasi: ")

if hytti_luokka == "LUX" or hytti_luokka == "lux":
    print ("LUX on parvekkeellinen hytti yläkannella.")
elif hytti_luokka == "A" or hytti_luokka == "a":
    print ("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti_luokka == "B" or hytti_luokka == "b":
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti_luokka == "C" or hytti_luokka == "c":
    print ("C on ikkunaton hytti autokannen alapuolella.")
else: 
    print ("Virheellinen hyttiluokka.")

# tai jos haluaa tehä helpommin niin hytti_luokka = input("Kerro hyttiluokkasi: ").lower()
#                                                                                ---------
