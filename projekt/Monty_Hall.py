import random

# 0 = goat, 1 = car
doors=[0, 0, 0]
loop = True
while loop == True:
    doors[random.randint(0, 2)] = 1
    anwser_loop = True
    while anwser_loop == True:
        answer = input("Which door do you choose? (1, 2, 3) ")
        if answer == "1" or answer == "2" or answer == "3":
            answer = int(answer)
            answer = answer - 1
            anwser_loop = False 
        found_goat_door = False
        for i in range(3): 
            if doors[i] == 0 and i != answer and found_goat_door == False:
                print(i + 1)
                found_goat_door = True

    