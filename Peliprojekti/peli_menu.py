import math
import time

def aloita():
    # Peli funktio täällä
    print("aloita -func")
    
    
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
    

def sulje():
    print('Sulje peli kiejoittamalla "lopeta": ')
    komento = input("> ").lower()
    if komento == "lopeta":
        quit()


def menu():
    print('''
                 MENU 
    ALOITA      OHJEET      SULJE''')
    komento = input("> ").lower()
    if komento == "aloita":
        aloita()
    if komento == "ohjeet":
        ohjeet()
    if komento == "sulje":
        sulje()


user_nimi = input("Kuka olet: ")
user_ika = int(input("Ikä: "))

if user_ika <= 11:
    print("Pelaaja liian nuori. Pelaajan tulee olla vähintään 12-vuotias.")
    quit()
if user_ika >= 12:
    print("Tervetuloa LABRAAN", user_nimi, "!")
    time.sleep(1)

while True:
    menu()

 

##MAHDOLLINEN LIIKKUMIS TAPA??
# def suunta():
#     while True:
#         go = input("Mihin suuntaan haluat mennä? ")
#         go = go[0].lower()
#         if go in ["o", "v", "y", "a"]:
#             return go
#         else:
#             print("Anna jokin muu suunta")
