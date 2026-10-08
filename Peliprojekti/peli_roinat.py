import math
import peli_menu
        
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
    def __init__(self, name, sijainti, health = 10):
        self.name = name
        self.sijainti = sijainti
        self.health = health
