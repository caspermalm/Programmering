#Kodexempel som ledtråd till slumptal. (4p)

#import random
#tal = random.randint(1, 6) # slumptal 1, 2, 3, 4, 5 eller 6.

#Översätt nedanstående till kod.

#Kasta en sexsidig tärning 20 gånger. Spara resultaten i en lista.
#Räkna antalet 3:or. Skriv ut antalet.

import random
lista = []
for i in range(20):
    randomint = random.randint(1, 6)
    lista.append(randomint)
print(lista)

svar = 0

for i in lista:
    if i == 3:
        svar += 1

print(svar)