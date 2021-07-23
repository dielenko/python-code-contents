# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
	if var % 2 == 0:
		output_list.append(var)

print("Output List using for loop:", output_list)

# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
							list_using_comp)

# When use Dictionary:
x = {i:0 for i in range(10) if i % 2 == 0}
print(x)

# When use Set:
x = {i for i in range(10) if i % 2 == 0}
print(x)

# When use Tuple:
x = tuple(i for i in range(10) if i % 2 == 0)
print(x)
