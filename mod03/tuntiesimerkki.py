print("Tämä ohjelma muuntaa fahrenheitit celsius asteiksi. \n")
fahrenheit = input("Anna lämpötila fahrenheit yksikössä: ")

celsius = (float(fahrenheit) - 32) * 5 / 9

# print("Konversion tulos: " + str(celsius))
print(f"Lämpötila celsius-asteina: {celsius:6.2f}")