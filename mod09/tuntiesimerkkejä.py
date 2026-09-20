# class/luokka = blueprint, sen pohjalta rakentuu oliot = objects
# python vaatii luokan=classin sisään jotain 
# >> pass on tyhjä lause joka vaan jatkaa koodia
# >> metodi = funktio classin sisällä
# Luokat aina isolla.

class Auto:
    pass

class Koulu:
        pass

class Opiskelija:
      pass

Opiskelija1 = Opiskelija()

Opiskelija1.nimi = "Jaakko"
Opiskelija1.syntymavuosi = "2006"
Opiskelija1.keskiarvo = 1

print(f"{Opiskelija1.nimi} syntyi vuonna {Opiskelija1.syntymavuosi}.")

#Fiksumpi ja nopeampi tapa jos luokka=class toistuu useasti

class Hero:
    sankarien_maara = 0

    def __init__(self, nimi, tyyppi, voima, ammu, huudahdus="'Hei!'"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.ammu = ammu
        self.huudahdus = huudahdus
        Hero.sankarien_maara = Hero.sankarien_maara + 1

    def huuda(self, kerrat=1):
         for i in range(kerrat):  
            print(f"{self.huudahdus}")

    def ase(self):
        print(self.ammu)
    

hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "BANG", "'AAARGH!'")
hero2 = Hero("Tracer", "Vahingontekijä", "Nopea", "PIU")
hero3 = Hero("Jonne", "Tukija", "ES", "jippii", "JIPPII")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}. Hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}.  Hän sanoo {hero2.huudahdus}")
print(f"{hero3.nimi} on {hero3.tyyppi} ja hän on {hero3.voima}.  Hän sanoo {hero3.huudahdus}")

hero1.huuda()
hero1.ase()

hero2.huuda(2)
hero2.ase()

hero3.huuda()
hero3.ase()

print(f"Sankarien määrä joukkueessa: {Hero.sankarien_maara}")


# def laske_kaden_luvun_summa(luku1, luku2):
#       summa = luku1 + luku2
#       return summa

# yhteenlaskettu_summa = laske_kaden_luvun_summa(1, 2)

# print(f"Summa: {yhteenlaskettu_summa}")

# Jos joku asia toistuu koodissa usein, kannattaa tehdä funktio
## esim pelissä kolikoiden kerääminen josta saa pisteitä ja elämiä

