import time

#PELAAJA
class User:
    def __init__(self, name, liiku, health = 50, weight = 20, ):
        self.name = name
        self.health = health
        self.weight = weight
        self.liiku = liiku
        # self.sijainti = sijainti



#INVENTORY
inventory = []
def inv_add():
    lisaa = input("Lisää inventoriin: ")
    inventory.append(lisaa)

#SATUS
def status():
    print(f'''
    {user_nimi} 
    ELÄMÄT:{user1.health} KANTOPAINO:{user1.weight}
    -------------------------------------------
    Inventory''')
    print(inventory)



#KYSYTYT TIEDOT
user_nimi = input("Kuka olet: ")
user_ika = int(input("Ikä: "))

if user_ika <= 11:
    print("Pelaaja liian nuori. Pelaajan tulee olla vähintään 12-vuotias.")
    quit()
if user_ika >= 12:
    print("Tervetuloa LABRAAN", user_nimi, "!")
    time.sleep(1)

