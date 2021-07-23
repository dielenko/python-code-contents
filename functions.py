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