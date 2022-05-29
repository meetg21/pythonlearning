print('''Welcome to treasure Island.
Your mission is to find the treasure''')

start = input(print("you're at a cross road. where do you want go ?left or right"))

if start == "left":
    a = input(print("swim or wait"))
    
    if a == "wait":
        b = input(print("Which door u wanna open?red,blue or yellow"))

        if b == "yellow":
            print("you win")

        else:
            print("game over")

    else:
        print("game over")        


else:
    print("Game over")



