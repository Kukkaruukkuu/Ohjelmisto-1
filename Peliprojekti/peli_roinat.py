import math
import time
import peli_menu
from peli_menu import user_nimi

inventory = []
def inv_add():
    lisaa = input("Lisää inventoriin: ")
    inventory.append(lisaa)

# tamanhetkinen_huone = 
# sijainti = (tamanhetkinen_huone)

class User:
    def __init__(self, name, health = 50, weight = 20, ):
        self.name = name
        self.health = health
        self.weight = weight
        # self.sijainti = sijainti

user1 = User((user_nimi))

def status():
    print(f'''
    {user_nimi} 
    ELÄMÄT:{user1.health} KANTOPAINO:{user1.weight}
    -------------------------------------------
    Inventory''')
    print(inventory)


class Monster:
    def __init__(self, name, sijainti, health = 100):
        self.name = name
        self.sijainti = sijainti
        self.health = health

def kartta():
    print(''' 
 --------------------------------------------------------
 |         --------     --------     --------     ----  |
 |        |        |---|        |---|        |---|    | |
 |         --------     --------     --------     ----  |
 |        /                  |             |            |
 |    -----               --------      --------        |
 |   |     |             |        |    |        |       |
 |    -----               --------      --------        |
 |      ^                                    |          |
 |     Olet tässä                           ---         |
 |   Liiku kartan mukaan                   |   |        |
 |                                          ---         |
 --------------------------------------------------------                                                                                ''') 
    return         

huoneet = {"start" : {"ylös" : "huone1"},
           
           "huone1" : {"alas" : "start",
                       "oikealle" : "huone2"},

            "huone2" : {"alas" : "huone3",
                       "oikealle" : "huone4",
                       "vasemmalle" : "huone5"},

            "huone3" : {"ylös" : "huone2"},

            "huone4" : {"alas" : "huone5",
                       "oikealle" : "huone6",
                       "vasemmalle" : "huone2"},

            "huone5" : {"alas" : "hissi",
                       "ylös" : "huone4"},

            "huone6" : {"vasemmalle" : "huone4"},

            "hissi" : {"ylös" : "huone5"}}