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