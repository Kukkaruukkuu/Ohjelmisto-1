import random

#INVENTORY
inventory = []
def nosta():
    print("pöö")

#TAVARAT
class Tavara:
    def __init__(self, nimi, tehtava, dmg):
        self.nimi = nimi
        self.tehtava = tehtava
        self.dmg = dmg

# taskulamppu = Tavara("Taskulamppu", "valaisee")
# avainkortti = Tavara("Avainkortti", "avaa hissin")
# rohto = Tavara("Rohto", user_health = 50)
kirves =Tavara("Kirves", "tekee dmg", random.randint(1, 15))

#KARTTA
def kartta():
    print(''' 
 ----------------------------------------------
 |   ---    --------     --------     ----    |
 |  |   |--|        |---|        |---|    |   |
 |   ---    --------     --------     ----    |
 |    ^           |           |               |
 | Olet tässä   --------      --------        |
 |             |        |    |        |       |
 |              --------      --------        |
 |                                 |          |
 |                                ---         |
 |   Liiku kartan mukaan         |   |        |
 |                                ---         |
 ----------------------------------------------                                                                               ''') 
    return 