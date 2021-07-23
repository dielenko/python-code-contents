## Example for Global and Local variables
x = 'tim' # global

def func(name):
    global x # use the global variable (not good idea to be used)
    x = name # local
    
print('x')
func('changed')
print('x')