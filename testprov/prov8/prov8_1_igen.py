#lägg talen 2, 3, 2, 4, 1 i en lista
#ändra det andra elementet (3) till 5
#ändra det sista elementet (1) till 6
#Lägg till 4 sist i listan (längst till höger)
#beräkna och skriv ut medelvärdet av talen i listan
#Sortera listan och skriv ut den

lista = [2, 3, 2, 4, 1]
lista[1] = 5
lista[4] = 6
lista.append(4)
#lista.insert(5, 4)
print(lista)
medel = sum(lista) / len(lista)
print(medel)



