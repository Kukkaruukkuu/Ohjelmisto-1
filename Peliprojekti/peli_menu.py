import math
import time

def aloita():
    print("peli alkaa")
    return

def ohjeet():
    print('''
        -----------------------------------------------------------------
        KONRTOLLIT:
        
        -----------------------------------------------------------------
        LIIKKUMINEN:
        Liiku kirjoittamalla jokin seuraavista: 
        YLÖS
        ALAS
        OIKEALLE
        VASEMMALLE
        -----------------------------------------------------------------
        STATUS:
        Avaa statuksesi kirjoittamalla: status.
        Statuksesta näet: 
        ELÄMIEN MÄÄRÄN
        KANTO PAINO
        INVENTAARIO
        -----------------------------------------------------------------''')
    return

def sulje():
    print('Sulje peli kiejoittamalla "lopeta": ')
    komento = input("> ").lower()
    if komento == "sulje":
        komento = "lopeta".lower()
    return komento


def menu():
    print('''
                 MENU 
    ALOITA      OHJEET      SULJE''')
    komento = input("> ").lower()
    if komento == "aloita":
        komento = aloita()
    if komento == "ohjeet":
        komento = ohjeet()
    if komento == "sulje":
        komento = sulje()
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
 |      ^                                    |          |
 |                                          ---         |
 |                                         |   |        |
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
