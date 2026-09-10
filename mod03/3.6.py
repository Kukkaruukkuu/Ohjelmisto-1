# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
## kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
## nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

start = 000
stop = 666
print(random.randint(start , stop ))


a = str(random.randint(1, 6))
b = str(random.randint(1, 6))
c = str(random.randint(1, 6))
d = str(random.randint(1, 6))

print(a+b+c+d)

