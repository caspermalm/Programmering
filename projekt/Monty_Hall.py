import random

# 0 = get, 1 = bil
doors=[0, 0, 0]
doors[random.randint(0, 2)] = 1
answer = int(input("Which door do you choose? (1, 2, 3) "))
if answer == 1 or answer == 2 or answer == 3:
    print(doors)
    
    
if answer == 1 or answer == 2 or answer == 3:
    answer = int(answer)
    answer = answer - 1
for i in range(3): 
    if doors[i] == 0 and i != answer:
        print("door number", i + 1, "is wrong, now choose again")
switch_door = input("Do you want to switch door? ")
if switch_door == "yes":
    new_answer = int(input("Which door do you choose? (1, 2, 3) "))
    new_answer = new_answer - 1
#print("Rätt dörr är: ", doors.index(1) + 1)
    









