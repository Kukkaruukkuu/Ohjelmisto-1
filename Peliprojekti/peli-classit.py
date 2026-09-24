import math
import time
import peli_menu
from peli_menu import user_nimi

inventory = []

class User:
    def __init__(self, name, health = 50, weight = 20):
        self.name = name
        self.health = health
        self.weight = weight

user1 = User((user_nimi))

def status():
    print(f'''
    {user_nimi} 
    ELÄMÄT:{user1.health} KANTOPAINO:{user1.weight}
    -------------------------------------------
    Inventory''')
    print(inventory[0])


# class Monster:
#     def __init__(self, name, health = 100):
#         self.name = name
#         self.health = health


status()