import math
import time

print("Welcome to the GAME")
time.sleep(1)
user_nimi = input("Who are you: ")
user_ika = int(input("How old are you: "))

while user_ika <= 11:
    print("You are not ready. You are too young.\nGame will close now.")
    break
else: 
    print("We have long waited for you.")
    time.sleep(1)
    print("WELCOME ", user_nimi,"!")