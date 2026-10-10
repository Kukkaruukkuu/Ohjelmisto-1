# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, kerros=0, alin_kerros=0, ylin_kerros=10):
        self.kerros = kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kerros_nro):
        if self.kerros < kerros_nro:
            for x in range(kerros_nro - self.kerros):
                self.kerros_ylös()
        else:
            for y in range(self.kerros - kerros_nro):
                self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
        print(self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros)

class Talo:
    def __init__(self, talon_alin=0, talon_ylin=10, hissien_määrä=5):
        self.talon_alin = talon_alin
        self.talon_ylin = talon_ylin
        self.hissien_määrä = hissien_määrä
        self.hissit = []

        for x in range(hissien_määrä):
            self.hissit.append(Hissi(talon_alin, talon_alin, talon_ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.talon_alin)

talo1 = Talo(0, 10, 3)

talo1.aja_hissia(0, 6)
talo1.palohälytys()