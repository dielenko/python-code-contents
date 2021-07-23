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
