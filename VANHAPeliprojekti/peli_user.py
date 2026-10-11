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

#PELAAJA
class User:
    def __init__(self, name, health: int, damage: int, ):
        self.name = name
        self.health = health


main_user = User(user_nimi, "ylös")


#SATUS
def status():
    print(f'''
    {user_nimi} 
    ELÄMÄT:{main_user.health} KANTOPAINO:{main_user.weight}
    -------------------------------------------
    Inventory''')
    print(inventory)

