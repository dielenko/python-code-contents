class Dog(object):

    # __init__ - constructor or initiliaziation method
    # self represents the object instance (e.g. tim or fred)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def tals(self):
        print('Bark!')


class Cat(Dog):
    # self represents the object instance (e.g. tim or fred)
    def __init__(self, name, age, color):
        # super()__init__ - constructor method which initializes the root class (e.g. Dog) first
        super().__init__(name, age)
        self.color =color

    def talk(self):
        print('Meow!')

tim = Dog('tim', 10)
tim.talk()

tim = Cat('tim', 5, 'blue')
tim.talk()