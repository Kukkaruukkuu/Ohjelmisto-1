import json
import user

def save():
    save_data = {"pelaaja" : user.user_nimi,
                 "ika" : user.user_ika}
    
    with open("save.json", "w") as tiedosto:
        json.dump(save_data, tiedosto)

def load():
    with open("save.json", "r") as tiedosto:
            data_read = json.load(tiedosto)
    return data_read