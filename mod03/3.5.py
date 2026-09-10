# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, 
# nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä 
# ilmoittaa tuloksen käyttäjälle.
## Yksi leiviskä on 20 naulaa.
## Yksi naula on 32 luotia.
## Yksi luoti on 13,3 grammaa.

import math 

print ("Anna massa keskiaikaisten mittojen mukaan. Ohjelma muuntaa kilogrammoiksi ja grammoiksi.")

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luoti_paino = float(luoti * 13.3)
naula_paino = float(naula * (32 * luoti))
leiviska_paino = float(leiviska * ( 20 * naula))

massa = (leiviska_paino + naula_paino + luoti_paino)

kilo = massa // 1000
gramma = massa % 1000

print(f"Massa nykymittojen mukaan:{kilo: .2}kg ja{gramma: .2f}g")