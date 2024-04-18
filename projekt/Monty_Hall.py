import random

# 0 = goat, 1 = car
doors=[0, 0, 0]
loop = input("?: ")
while loop == True:
    doors[random.randint(0, 2)] = 1
    print(doors)
    anwser_loop = True
    
    
    while anwser_loop == True:
        answer = int(input("Which door do you choose? (1, 2, 3) "))
        if answer == "1" or answer == "2" or answer == "3":
            answer = int(answer)
            answer = answer - 1
            anwser_loop = False 
        found_goat_door = False    
        for i in range(3): 
            if doors[i] == 0 and i != answer and found_goat_door == False:
                print("door number", i + 1, "is wrong, now choose again")
                found_goat_door = True
        loop == False

print("Rätt dörr är: ", doors.index(1) + 1)
    


