# Class is a blueprint for creating new objects
# Object is an instance of a class

class Person:
    # class attributes are shared by all instances of a class
    greet_message = "Hey"

    def __init__(self, name):
        self.name = name

    def talk(self):
        # self is a reference to the current object
        print(f"Hi, I am {self.name}.")

    # class method is a method that is bound to a class rather than its object
    @classmethod
    def greet(cls):
        print(cls.greet_message)


p1 = Person("John Smith")
p1.talk()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def introduce(self):
        print(f"Hi, my name is {self.name} and I make {self.salary}.")

    def work(self):
        print(f"{self.name} is working.")

    def __str__(self):
        return f"{self.name} makes {self.salary}."


john = Employee("John", 50000)

# Check if an object is an instance of a class
print(isinstance(john, Employee))
print(isinstance(john, Person))

# Check if a class is a subclass of another class
print(issubclass(Employee, Person))
print(issubclass(Person, Employee))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # magic methods
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y

    def __gt__(self, other: object):
        return self.x > other.x and self.y > other.y


point1 = Point(10, 20)
point2 = Point(1, 2)
print(point1 > point2)

gt1 = point1 > point2
