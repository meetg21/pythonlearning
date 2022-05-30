import random

x = input("names of people present\n")

y = x.split(" ")

print(y)

c = len(y)-1


a = random.randint(0 , c)
e = y[a]

print(f"{e} will pay the bill")


