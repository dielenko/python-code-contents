# Example of Map
x = [1, 2, 3, 4, 5]

mp = map(lambda i: i + 2, x)

print(list(mp))

# Example of Filter
x = [1, 2, 3, 4, 5]

fl = filter(lambda i: i % 2 == 0, x)

print(list(fl))