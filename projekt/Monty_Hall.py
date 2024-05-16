import random

# 0 = get, 1 = bil
doors=[0, 0, 0]
doors[random.randint(0, 2)] = 1
answer = input("Which door do you choose? (1, 2, 3) ").lower()
if answer.isdigit() == True:
   answer = int(answer)
if answer == 1 or answer == 2 or answer == 3:
    print(doors)
    
potential_dors_to_open = []   
if answer == 1 or answer == 2 or answer == 3:
    answer = int(answer)
    answer = answer - 1
for i in range(3): 
    if doors[i] == 0 and i != answer:
        potential_dors_to_open.append(i)
index = random.randint(0,(len(potential_dors_to_open) -1))
print("door number", potential_dors_to_open[index] + 1, "is wrong, now choose again")
print(potential_dors_to_open ,index)
switch_door = input("Do you want to switch door? ")
if switch_door == "yes":
    new_answer = int(input("Which door do you choose? (1, 2, 3) "))
    new_answer = new_answer - 1
    if doors[new_answer] == 1:
        print("You won! ")
    else:
        print("You lost :( ")
else:
    if doors[answer] == 1:
        print("You won! ")
    else:
        print("You lost :( ")


#print("Rätt dörr är: ", doors.index(1) + 1)
    









