import math

# fruit prices in kilogram
banana_price_kilograms = 2.85
apple_price_kilograms = 3.15
orange_price_kilograms = 4.05

amount_of_banana = input("Banaanien määrä kiloina: ")
amount_of_apple = input("Omenoiden määrä kiloina: ")
amount_of_oranges = input("Appelsiinien määrä kiloina: ")

banana_price = (float(banana_price_kilograms)) * (float(amount_of_banana))
apple_price = (float(apple_price_kilograms)) * (float(amount_of_apple))
orange_price = (float(orange_price_kilograms)) * (float(amount_of_oranges))

print(f"Banaanien hinta: {banana_price: .2f}")
print(f"Omenoiden hinta: {apple_price: .2f}")
print(f"Appelsiinien hinta: {orange_price: .2f}")