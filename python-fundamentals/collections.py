# List - ordered collection
x = [4, True, 'hi']
x.append('hello') # add additional element in the list
x.extend([4,5,5]) # extend the list with additional list
x.pop() # remove element from the list
print(len(x))
x[0] = 'hello'
print(x[1])

y = x[:]
print(y)


# Tuple

x = (0,0,2,2)
print(x[0])