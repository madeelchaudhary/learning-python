class Animal:
    def __init__(self, color: str, legs: int, sound: str = "roar"):
        self.color = color
        self.legs = legs
        self.sound = sound

    def eat(self):
        print("nom nom nom")

    def speak(self):
        print(self.sound)

    def __str__(self):
        return f"{self.color} animal with {self.legs} legs that says {self.sound}."


class Dog(Animal):
    def __init__(self, color: str, legs: int):
        super().__init__(color, legs, "woof")
        self.name = "dog"

    def __str__(self):
        return f"{self.color} {self.name} with {self.legs} legs that says {self.sound}."


jack = Dog("brown", 4)
jack.eat()
jack.speak()
print(jack)
print(isinstance(jack, Animal))
print(isinstance(jack, Dog))
print(isinstance(jack, object))


class Lion(Animal):
    def __init__(self, color: str, legs: int):
        # call the parent constructor, otherwise parent attributes will not be available
        super().__init__(color, legs, "roar")
        self.name = "lion"

    # override the eat method
    def eat(self):
        print("chomp chomp chomp")

    def __str__(self):
        return f"{self.color} {self.name} with {self.legs} legs that says {self.sound}."


# Multi lever inheritance may cause problems, don't nest too many classes as it increases complexity


# Multiple inheritance

class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")


c = C()
print(C.__mro__)  # method resolution order
