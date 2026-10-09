import save
import user
# def ohjeet():
#     print('''
#         -----------------------------------------------------------------
#         KONRTOLLIT:
        
#         -----------------------------------------------------------------
#         LIIKKUMINEN:
#         Liiku kirjoittamalla jokin seuraavista: 
#         YLÖS
#         ALAS
#         OIKEALLE
#         VASEMMALLE
#         -----------------------------------------------------------------
#         STATUS:
#         Avaa statuksesi kirjoittamalla: status.
#         Statuksesta näet: 
#         ELÄMIEN MÄÄRÄN
#         KANTO PAINO
#         INVENTAARIO
#         -----------------------------------------------------------------''')

def sulje():
    print('Sulje peli kiejoittamalla "lopeta": ')
    komento = input("> ").lower()
    if komento == "lopeta":
        quit()
def menu():
    while True:
        print('''
                    MENU 
        ALOITA      OHJEET      SULJE''')
        komento = input("> ").lower()
        if komento == "aloita":
            break
        if komento == "jatka":
            save_data = save.load()
            user.user_nimi = save_data["pelaaja"]
            user.user_ika = save_data["ika"]
        if komento == "sulje":
            sulje()