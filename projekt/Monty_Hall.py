import random

# 0 = goat, 1 = car
doors=[0, 0, 0]
loop = True
while loop == True:
    doors[random.randint(0, 2)] = 1
    answer = input("Which door do you choose? ")
    
