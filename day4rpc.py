import random

choice = input(print("what do you wanna choose rock , papers or scisoors ?"))

computer = random.randint(0,2)
# 0 = rock 
# 1 = paper
# 2=scisoors

if computer == 0:
    print("computer chooses rock")
elif computer == 1:
    print("computer chooses paper")
else:
    print("computer chooses scisoors")

if choice == "rock":
    if computer == 1:

        print("computer wins")
    elif computer == 0:
        print("tie my boi")
    else:
        print("you won")

if choice == "paper":
    if computer == 2:
        print("computer wins")
    elif computer == 1:
        print("its a tie my boi")
    else:
        print("you won")

if choice == "scisoors":
    if computer == 0:
        print("computer wins")
    elif computer == 2:
        print("tie my boi")

    else:
        print("you won")

else:
    print("  ")





