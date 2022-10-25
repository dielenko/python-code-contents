#Password Generator Project
import random

#Prepare the list collections to provide usable user choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input Params
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Iterate over the user input to create a strong password and define the final output
password_list = []

#Use a random sample function to pick up elements from a sequence of length based on user input
for letter in range(1):
    random_letters = random.sample(letters, nr_letters)
for pass_letter in random_letters:
    password_list.append(pass_letter)

for symbol in range(1):
    random_symbols = random.sample(symbols, nr_symbols)
for pass_symbol in random_symbols:
    password_list.append(pass_symbol)

for number in range(1):
    random_numbers = random.sample(numbers, nr_numbers)
for pass_number in random_numbers:
    password_list.append(pass_number)

#Use a random shuffle function to prepare a strong and reorder-generated password
random.shuffle(password_list)
generated_password = ''.join(password_list)

print(f"Your password is: {generated_password}")