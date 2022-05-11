# tip calculator
print("Welcome to the tip calculator")

x = float(input("What was the total bill?"))
y = int(input("What percentage tip would you like to give ? 10,12, or 15?")) 

a = (y/100)*(x)
total = (x)+(a)
# print(type(total))
c = int(input("How many people to split the bill"))
final = round((total/c), 2)
print(f"Each person should pay {final}")
