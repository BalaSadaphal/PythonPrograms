class Person:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def characterisitics(self):
        # print("{} is {} years old".format(self.name, self.age))
        print(f"{self.name} is {self.age} years old")


ravi = Person('Ravi')
ashwin = Person('Ashwin', 32)

ravi.name = 'Rashi'

ravi.characterisitics()
