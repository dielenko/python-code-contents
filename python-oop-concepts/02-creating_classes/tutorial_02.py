class Dog(object):

    # self represents the object instance (e.g. tim or fred)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1,2,4]

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

tim = Dog('Tim', 10)
fred = Dog('Fred', 15)

fred.change_age(5)

tim.speak()
fred.speak()

tim.add_weight(55)
print(tim.weight)

print(tim.li)
