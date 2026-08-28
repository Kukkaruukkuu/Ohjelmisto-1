# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla 
# käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, 
# jos sen pituus on alle 37 cm.

kuha_pituus = float(input("Anna kuhan pituus cm: "))

kuha_lyhyt = 37 - kuha_pituus

if kuha_pituus < 37:
    print("Laske kuha takaisin järveen.")
    print (f"Kuhan pituudesta puuttuu {kuha_lyhyt: .2}cm :(")

if kuha_pituus >= 37:
        print("Kuha on tarpeeksi pitkä. Voit pitää sen! :)")