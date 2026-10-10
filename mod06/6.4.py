#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

vastaus=0
vastaukset=0
kaupungit=[]

while vastaukset<5:
    vastaus=input("Anna kaupungin nimi: ")
    kaupungit.append(vastaus)
    vastaukset= vastaukset+1

for x in kaupungit:
    print(x)