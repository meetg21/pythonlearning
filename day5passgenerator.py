from lib2to3.pytree import LeafPattern
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passs = ""
for letter in range(0,nr_letters):
    letter_list = random.choice(letters)
    # print(letter_list)
    passs += letter_list
# print(passs)

for symbol in range(0,nr_symbols):
    symbol_list = random.choice(symbols)
    passs += symbol_list

for number in range(0,nr_numbers):
    number_list = random.choice(numbers)
    passs += number_list

simple_pass = passs
print(simple_pass)

passs_list = list(passs)
random.shuffle(passs_list)
hard_pass = ""
for shuffle in passs_list:
    hard_pass += shuffle
print(hard_pass)




