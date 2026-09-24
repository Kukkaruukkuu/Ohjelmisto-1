import math
import time

inventory = []

def menu():
    print('''
                 MENU 
    ALOITA      OHJEET      SULJE''')
    komento = input("> ").lower()
    if komento == "aloita":
        print("peli alkaa")
    if komento == "ohjeet":
        print('''
        -----------------------------------------------------------------
        LIIKKUMINEN:
        Liiku kirjoittamalla jokin seuraavista: 
        ylös
        alas
        oikealle
        vasemmalle
        -----------------------------------------------------------------
        STATUS:
        Avaa statuksesi kirjoittamalla: status.
        Statuksesta näet: 
        elämien määrän
        kanto painon
        inventaarion.
        -----------------------------------------------------------------''')
    if komento == "sulje":
        input('Sulje peli kiejoittamalla "lopeta": ')
        komento = "lopeta".lower()
    return komento

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
 |     Move with the map.                    |          |
 |   Remember where you are!                ---         |
 | Move up, down, left or right.           |   |        |
 |                                          ---         |
 --------------------------------------------------------                                                                                ''') 
    return 

class User:
    def __init__(self, name, health = 50, weight = 20):
        self.name = name
        self.health = health
        self.weight = weight

class Monster:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        

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

user_nimi = input("Kuka olet: ")
user_ika = int(input("Ikä: "))

while True:
    if user_ika <= 11:
        print("Pelaaja liian nuori. Pelaajan tulee olla vähintään 12-vuotias.")
        break
    if user_ika >= 12:
        print("Tervetuloa LABRAAN", user_nimi, "!")
        time.sleep(1)
        if menu() == "lopeta":
            break

##MAHDOLLINEN LIIKKUMIS TAPA??
# def suunta():
#     while True:
#         go = input("Mihin suuntaan haluat mennä? ")
#         go = go[0].lower()
#         if go in ["o", "v", "y", "a"]:
#             return go
#         else:
#             print("Anna jokin muu suunta")
