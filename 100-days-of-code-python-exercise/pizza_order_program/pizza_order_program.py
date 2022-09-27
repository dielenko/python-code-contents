print("Welcome to Python Pizza!")
print("Please select a size for your pizza. The available choices are: Small, Medium, and Large.")
size = input("Add the pizza size:\n->'S'(Small)\n->'M'(Medium)\n->'L'(Large)\n").upper()
add_pepperoni = input("Do you want Peperoni. Answer with 'Y'(Yes), or 'N'(No): ").upper()
extra_cheese = input("Do you want extra cheese. Answer with 'Y'(Yes), or 'N'(No): ").upper()

price = 0

if size == 'S':
    price += 15
    if add_pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1

elif size == 'M' or size == 'L':
    if size == 'M':
        price += 20
    else:
        price += 25

    if add_pepperoni == 'Y':
        price += 3

    if extra_cheese == 'Y':
        price += 1

print(f"Your final bill is: ${price}.")