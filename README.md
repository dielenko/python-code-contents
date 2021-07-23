# Python-Speed-Course
Details: https://www.youtube.com/watch?v=VchuKL44s6E

## Data Types

>**Int**

````python
```
-267236
76373
```
````

>**Float**

````python
```
2727.0
-9.7
```
````

>**String**

````python
```
'hello'
"hello"
'hello"'
'.4.6'
```
````

>**Bool**

````python
```
# Set to 1

True

#Set to 0

False
```
````

## Output and Printing

````python
```
print('Hello World!')
print(4.5)
print('Hello World!',4.5)
print('Hello World!',4.5, end='|')
print('Hello World!',4.5, end='\n')
```
````

## Variables

````python
```
hello = 'tim'
world = 'world'
hello = world
hello = 'no'
print(hello, world)
```
````

> Variables Naming convention is **snake_case**

## Getting User Input

> Default output from the input comes out as STRING

````python
```
name = input('Name: ')
age = input('Age: ')
print('Hello', name, 'you are', age, 'years old')
```
````

## Arithmetic operators

> Division always return Float

````python
```
x = 10
y = 3

result = x + y
print(result)

result = x ** y
print(result)

result = x // y  # Floor division gives us integer result
print(result)

result = x % y  # Procent division
print(result)

B
E
D
M
A
S

num = input('Number: ')
print(int(num) - 5)
print(float(num) - 5)

# Additional information
x1 = 'hello'
y1 = 3
string_by_integer = x1 * y1  # Multiply string by integer

print(string_by_integer)

x2 = 'hello'
y2 = '3'
concatenate_strings = x2 + y2  # Concatenate strings

print(concatenate_strings)
```
````

## String Methods

````python
```
hello = 'hello'
print(type(hello))

hello = 'hello'.upper()
print(hello)

hello = 'heLLo'.lower()
print(hello)

hello = 'hello'.capitalize()
print(hello)

hello = 'hello'.count('l')
print(hello)

hello = 'heLLO World'.lower().count('o')
print(hello)
```
````

## Conditions and conditional operators

````python
```
== - equal operator
!= - not equal operator
<= - less than or equal operator
>= - greater than or equal operator
< - less than
> - greater than operator

# We use ASCII table to compare strings (ordinal value)

x = 'hello'
y = 'hello'

print(x == y)

x = 'hello'
y = 'helo'

print(x != y)

print('a:', ord('a'))
print('Z:', ord('Z'))

print('Is "a" is greater than "Z":', 'a' > 'Z')
```
````

## Chained conditionals

> Keep the order of the operators when evaluate condition

**not** - reverse the boolean output \
**and** - ```True``` if all conditions are true \
**or** - ```True``` if at least one condition is true

````python
```
x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < (x + 2)

result4 = result1 or result2

result4 = result1 or not result2 or result3
print(result4)

print (not (False and True or True))
```
````

## IF / ELSE / ELIF statements

````python
```
if condition:
    statement

x = input('Name: ')

if x == 'Tim':
    print('You are great')
elif x == 'Joe':
    print('Bye Joe')
elif x == 'Sarah':
    print('Random')
else:
    print('No')
```
````

## Collections

> Collection is ordered or unordered group of elements
> List is mutable and ordered

````python
```
x = [4, True, 'hi']
x.append('hello') # add additional element in the list
x.extend([4,5,5]) # extend the list with additional list
x.pop() # remove element from the list
print(len(x))
x[0] = 'hello'
print(x[1])

y = x[:]
print(y)
```
````

> Tuple is immutable and unordered

````python
```
x = (0,0,2,2)
print(x[0])
```
````

## For Loops

````python
```
# stop
for i in range(10):
    print(i)

# start, stop
for i in range(5, 10):
    print(i)

# start, stop, step
for i in range(5, 10, 2):
    print(i)

x = [3,4,42]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)
```
````

## While Loops

> while condition == True: \
>------> go ahead and do something

````python
```
i = 0
while i < 10:
    print('run')
    i += 1

x = 0
while True:
    print('run')
    x += 1
    if x == 10:
        break
```
````

## Slice operator

````python
```
sliced = [start:stop:step]
sliced = x[::-1] # reverse a list
```
````

- Details: https://www.geeksforgeeks.org/python-slice-function/

> A sequence of object of any type(string, bytes, tuple, list or range) or the object which implements __getitem__() and __len__() method then this object can be sliced using slice() method.

- Syntax:

````python
```
slice(stop)
slice(start, stop, step)

# Parameters:
# start: Starting index where the slicing of object starts.
# stop: Ending index where the slicing of object stops.
# step: It is an optional argument that determines the increment between each index for slicing.

# Return Type: Returns a sliced object containing elements in the given range only.

x = [0,1,2,3,4,5,6,7,8]

y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"

sliced = x[0:4:2]

sliced = y[::-1]

print(sliced)
```
````

## Sets Data Type

- Details: https://www.geeksforgeeks.org/python-set-method/

> Set is extremely fast to look up for elements than the other typical methods for searching \
> Set, a term in mathematics for a sequence consisting of distinct language is also extended in its language by Python and can easily be made using set(). \
> set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set. 

- Syntax : set(iterable)

> Parameters : Any iterable sequence like list, tuple or dictionary. \
> Returns : An empty set if no element is passed. Non-repeating element iterable modified as passed as argument. \
> Don’t worry if you get an unordered list from the set. Sets are unordered. Use sorted(set(sampleList)) to get it sorted

````python
```
x = set()
s = {4,32,2,2}
s.add(5)
s.remove(2)
print(s)

s1 = {4,32,2,2}
s2 = {3,4,22,1}

print(s1.union(s2))

## Dictionary Data Type

x = {'key': 4}

x['key2'] = 5
x[2] = [2,2,1,1]

print(x)

print('key' in x)

print(x.keys())
print(x.values())


print(list(x.keys()))
print(list(x.values()))

del x['key']
print(x)

for key, value in x.items():
    print(key, value)

for key in x:
    print(key, x[key])
```
````

## Comprehensions

- Details: https://www.geeksforgeeks.org/comprehensions-in-python/

> Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:

- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Comprehensions

````python
```
#The following is the basic structure of a list comprehension:

output_list = [output_exp for var in input_list if (var satisfies this condition)]

# Note that list comprehension may or may not contain an if condition. List comprehensions can contain multiple for (nested list comprehensions).

# Constructing output list WITHOUT Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
	if var % 2 == 0:
		output_list.append(var)

print("Output List using for loop:", output_list)

# Using List comprehensions for constructing output list
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:", list_using_comp)

# When use Dictionary:
x = {i:0 for i in range(10) if i % 2 == 0}
print(x)

# When use Set:
x = {i for i in range(10) if i % 2 == 0}
print(x)

# When use Tuple:
x = tuple(i for i in range(10) if i % 2 == 0)
print(x)
```
````

## Functions

````python
```
def func1(x, y):
    print('Run', x, y)
    def func2():
        print('hi')
    func2()

print(func1(5,6))

def func3(x, y):
    print('Run', x, y)
    return x * y, 5

print(func3(5,6))

def func4(x, y):
    print('Run', x, y)
    return x * y, x / y

r1, r2 = func4(5, 6)
print(r1, r2)

def func5(x, y, z=None):
    print('Run', x, y, z)
    return x * y, x / y

r1, r2 = func5(5, 6, 7)
print(r1, r2)

def func(x):
    def func2():
        print(x)
        
    return func2

print(func(3)())

def func(x):
    def func2():
        print(x)
        
    return func2

x = func(3)
x()
```
````

## Unpack operator / *ARGS and **KWARGS

````python
```
def func(*args, **kwargs):
    pass

x= [1, 23, 34, 45]
print(x)
print(*x) # Used to pair a list

def func(x, y):
    print(x,y)
    
func(**{'x': 2, 'y' :5}) # Used to pair a dictionary

def func(*args, **kwargs):
    print(args,kwargs)

func(1,2,3,4,5,one=0, two=1)
```
````

## Scope and Global

````python
```
# Example for Global and Local variables
x = 'tim' # global

def func(name):
    global x # use the global variable (not good idea to be used)
    x = name # local
    
print('x')
func('changed')
print('x')
```
````

## Exceptions

````python
```
# build-in
raise Exception('Bad')

raise FileExistsError('')
```
````

## Handling Exceptions

````python
```
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')
```
````

## Lambda

> It is one line anonymous function

````python
```
x = lambda x: x + 5

print(x(2))
```
````

## Map and Filter

````python
```
# Example of Map
x = [1, 2, 3, 4, 5]

mp = map(lambda i: i + 2, x)

print(list(mp))

# Example of Filter
x = [1, 2, 3, 4, 5]

fl = filter(lambda i: i % 2 == 0, x)

print(list(fl))
```
````

## F Strings

> New in Python 3.6

````python
```
tim = 89
x = f'hello {6 + 8} {tim}'

print(x)
print(f'hi {7+10} {tim}')
```
````
