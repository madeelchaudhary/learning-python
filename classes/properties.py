class Person:
    def __init__(self, name: str):
        self.set_name(name)

    def set_name(self, name: str):
        if len(name.split(" ")) != 2:
            raise ValueError("You must provide a first and last name.")
        first_name, last_name = name.split(" ")
        self.__full_name = f"{first_name} {last_name}"

    def get_name(self):
        return self.__full_name

    full_name = property(get_name, set_name)

    def __str__(self):
        return f"Person: {self.__full_name}"


john = Person("John Doe")
print(john.full_name)
john.full_name = "John Smith"
print(john.full_name)


# By using the @property decorator, we can make a method behave like a property.
class Person:
    def __init__(self, name: str):
        # self.name = name
        self.full_name = name

    @property
    def full_name(self):
        return self.name

    @full_name.setter
    def full_name(self, name: str):
        if len(name.split(" ")) != 2:
            raise ValueError("You must provide a first and last name.")
        first_name, last_name = name.split(" ")
        self.name = f"{first_name} {last_name}"

    def __str__(self):
        return f"Person: {self.name}"


john = Person("John Doe")
print(john.full_name)
john.full_name = "John Smith"
print(john.full_name)
