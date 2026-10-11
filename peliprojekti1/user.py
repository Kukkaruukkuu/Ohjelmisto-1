import time
#KYSYTYT TIEDOT
#NIMI
print("Kuka olet: ")
user_nimi = input("> ")

#IKÄ
user_ika = int(input("Ikä:\n> "))

if user_ika <= 11:
    print("Pelaaja liian nuori. Pelaajan tulee olla vähintään 12-vuotias.")
    quit()
if user_ika >= 12:
    print("Tervetuloa Labraan", user_nimi, "!")
    time.sleep(1)  