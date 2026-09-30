import math
import peli_menu

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

##MAHDOLLINEN LIIKKUMIS TAPA??
# def suunta():
#     while True:
#         go = input("Mihin suuntaan haluat mennä? ")
#         go = go[0].lower()
#         if go in ["o", "v", "y", "a"]:
#             return go
#         else:
#             print("Anna jokin muu suunta")


#MONSTERI
class Monster:
    def __init__(self, name, sijainti, health = 100):
        self.name = name
        self.sijainti = sijainti
        self.health = health

#HUONEET
class Esine:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti