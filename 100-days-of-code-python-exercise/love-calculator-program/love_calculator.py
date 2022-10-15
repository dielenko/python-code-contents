print("Welcome to the Love Calculator!")
# Input Params
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Constant words for matching
true = 'TRUE'
love = 'LOVE'

# Start the actual code structure section
true_count = 0
love_count = 0

# Create a list of input params and convert it to a string
names_list = [name1, name2]
names_string = ''.join(names_list).upper().replace(' ', '')

# Iterate over the first constant word to find a match
for i in names_string:
    for t in true:
        if i == t:
            true_count += 1

# Iterate over the second constant word to find a match
for n in names_string:
    for l in love:
        if n == l:
            love_count += 1

# Calculate the final matching count
total_count = str(true_count) + str(love_count)

# Make a decision statement and print the result
if int(total_count) < 10 or int(total_count) > 90:
    print(f"Your score is **{total_count}**, you go together like coke and mentos.")
elif int(total_count) > 39 and int(total_count) < 51:
    print(f"Your score is **{total_count}**, you are alright together.")
else:
    print(f"Your score is **{true_count}{love_count}**.")
