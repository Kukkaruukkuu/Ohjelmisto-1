import time
import peli_user
import peli_menu
import invi_ja_tavarat

#TÄNNE TULEE PELI
peli_menu.menu()
time.sleep(2)
print('''
Astut sisälle labraan. Näet ympärilläsi rikkinäisiä huonekaluja 
ja rikkoutuneiden ikkunoiden lasinsirpaleita.
Sirpaleiden seassa huomaat jonkin lapun.
(Nosta lappu kirjoittamalla "nosta")''')
input("> ")
print('Se on kartta! (voit avata kartan kirjoittamalla "kartta")')
input("> ")