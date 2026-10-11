#IMPORTIT
import save
import user

#MENU
def sulje():
    print('Sulje peli kirjoittamalla "lopeta": ')
    komento = input("> ").lower()
    if komento == "lopeta":
        quit()
def menu():
    while True:
        print('''
                        MENU 
        ALOITA      TALLENNUKSET      SULJE''')
        komento = input("> ").lower()
        if komento == "aloita":
            break
        if komento == "tallennukset":
            save_data = save.load()
            user.user_nimi = save_data["pelaaja"]
            user.user_ika = save_data["ika"]
        if komento == "sulje":
            sulje()