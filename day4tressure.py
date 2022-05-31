import random
from tkinter import Y 

row1 = ["x","x","x"]
row2 = ["x","x","x"]
row3 = ["x","x","x"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where u have to put the tressure")

a = int(position[0])
b = int(position[1])
# print(a,b)
row = map[b-1]
row[a-1]=Y

# print(map)
print(f"{row1}\n{row2}\n{row3}")
