nykyinen_huone = "aula"

huoneet = {"aula" : {"oikea" : "huone1"},
           
           "huone1" : {"vasen" : "aula",
                       "oikea" : "huone3",
                       "alas" : "huone2"},

            "huone2" : {"ylös" : "huone1"},

            "huone3" : {"vasen" : "huone1",
                        "oikea" : "huone4",
                        "alas" : "huone5"},

            "huone4" : {"vasen" : "huone3"},

            "huone5" : {"alas" : "hissi",
                       "ylös" : "huone3"},

            "hissi" : {"ylös" : "huone5"}}

def liiku():
    go = input("Valitse suunta\n>")
    if go in huoneet[nykyinen_huone]:
        nykyinen_huone = huoneet[nykyinen_huone][go]
        print(f"Olet nyt {nykyinen_huone}")
    else:
        print("noup")

liiku()
# def liiku():
#     while True:
#         go = input("Mihin suuntaan haluat mennä?\n>")
#         go = go[0].lower()
#         if go in ["o", "v", "y", "a"]:
#             return go
#         else:
#             print("Anna jokin muu suunta")

# liiku()

# class Huone:
#     def __init__(self, nimi, suunnat = []):
#         self.nimi = nimi
#         self.suunnat = suunnat

#     def liiku(suunnat):
#         while True:
#             go = input("Mihin suuntaan haluat mennä?\n>")
#             go = go[0].lower()
#             if go in ["o", "v", "y", "a"]:
#                 nykyinen_huone
#                 return go
#             else:
#                 print("Anna jokin muu suunta")


# aula = Huone("aula", ["oikea"])
# huone1 = Huone("huone1", ["vasen", "oikea", "alas"])
# huone2 = Huone("huone1", ["ylös"])
# huone3 = Huone("huone3", ["vasen", "oikea", "alas"])
# huone4 = Huone("huone4", ["vasen"])
# huone5 = Huone("huone5", ["alas", "ylös"])
# hissi = Huone("hissi", ["ylös"])

# print(aula.nimi)
# aula.liiku()
