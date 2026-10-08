import time
#KYSYTYT TIEDOT
user_nimi = input("Kuka olet: ")
user_ika = int(input("Ikä: "))

if user_ika <= 11:
    print("Pelaaja liian nuori. Pelaajan tulee olla vähintään 12-vuotias.")
    quit()
if user_ika >= 12:
    print("Tervetuloa LABRAAN", user_nimi, "!")
    time.sleep(1)  