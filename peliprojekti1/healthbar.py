#HEALTHBAR

import os

#HEALTHBAR CLASS
class HealthBar:
    remaining = "█"
    lost = "_"
    raja = "|"
    colors = {"red": "\033[91m",
                "purple": "\33[95m",
                "blue": "\33[34m",
                "blue2": "\33[36m",
                "blue3": "\33[96m",
                "green": "\033[92m",
                "green2": "\033[32m",
                "brown": "\33[33m",
                "yellow": "\33[93m",
                "grey": "\33[37m",
                "default": "\033[0m"
                }

    def __init__(self, kuka, pituus = 20, colored = True, color = ""):
        self.kuka = kuka
        self.pituus = pituus
        self.health_nyt = kuka.health
        self.max = kuka.health_max

        self.colored = colored
        self.color = self.colors.get(color) or self.colors["default"]

    def muutos(self):
        self.health_nyt = self.kuka.health

    def bar(self):
        jaljella = round(self.health_nyt / self.max * self.pituus)
        menetetyt = self.pituus - jaljella
        print(f"{self.kuka.nimi} elämät: {self.kuka.health}/{self.kuka.health_max}")
        print(f"{self.raja}"f"{self.color if self.colored else ''}"f"{jaljella * self.remaining}"f"{menetetyt * self.lost}"f"{self.colors['default'] if self.colored else ''}"f"{self.raja}")