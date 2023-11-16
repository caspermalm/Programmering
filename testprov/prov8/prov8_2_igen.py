#import random
#tal = random.randint(1, 6) # slumptal 1, 2, 3, 4, 5 eller 6.

#Översätt nedanstående till kod.

#Kasta en sexsidig tärning 20 gånger. Spara resultaten i en lista.
#Räkna antalet 3:or. Skriv ut antalet.

import random
lista = []
tal = random.randint(1, 6)
for i in range(20):
    lista.append(random.randint(1, 6))
print(lista)
print("antal treor:", lista.count(3))

