class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # decorators
    # cls - means the name of the class (e.g. Dog)
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""

        for _ in range(n):
            print("Bark!")

# classmethod
jim = Dog('Jim')
print(Dog.num_dogs())

# staticmethod
Dog.bark(5)