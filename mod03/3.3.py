# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion 
# piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = input("Anna suorakulmion kannan pituus: ")
korkeus = input("Anna suorakulmion korkeuden pituus: ")

piiri = (float(kanta) * 2) + (float(korkeus) * 2)
pinta_ala = (float(kanta)) * (float(korkeus))

print(f"Suorakulmion piiri: {piiri: .2f}")
print(f"Suorakulmion pinta-ala: {pinta_ala:.2f}")