class Student:
    # Below is static/ class variable can be accessed with in
    # the class by self and outside by Class name or object name
    school = 'No School yet'

    def __init__(self, name, years_old, brand):
        self.name = name
        self.age = years_old
        self.laptop = self.Laptop(brand)

    def show(self):
        print(f"{self.name} who is {self.age} years old "
              f"belongs to {self.school} owns a laptop with {self.laptop.toString()}")

    @classmethod
    def modify_school(cls, school):
        cls.school = school

    @staticmethod
    def info():
        print("This is student class's static method")

    class Laptop:
        def __init__(self, brand, cpu='Intel', memory=8):
            self.brand = brand
            self.cpu = cpu
            self.memory = memory

        def toString(self):
            return f'Brand=> {self.brand}, CPU=>{self.cpu}, Memory=>{self.memory}'


ravi = Student('Ravi', 21, 'HP')
ravi.info()
ravi.modify_school('New School')
ravi.show()
ravi.laptop.memory = 16
ravi.show()

