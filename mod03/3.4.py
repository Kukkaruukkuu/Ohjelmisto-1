# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. 
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

eka_luku = float(input("Anna ensimmäinen luku: "))
toka_luku = float(input("Anna toinen luku: "))
kolmas_luku = float(input("Anna kolmas luku: "))

summa = eka_luku + toka_luku + kolmas_luku
tulo = eka_luku * toka_luku * kolmas_luku
keskiarvo = (eka_luku + toka_luku + kolmas_luku) / 3

print(f"Lukujen summa: {summa: .2}")
print(f"Lukujen tulo: {tulo: .2}")
print(f"Lukujen keskiarvo: {keskiarvo: .2}")