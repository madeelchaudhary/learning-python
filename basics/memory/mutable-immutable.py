# Immutable Data Types are those that cannot be changed once they are created.
# When immutable data types are modified, Python interpreter will allocate a new memory address for the new value of the variable.
# Immutable Data Types: int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

name = "John Doe"
print(id(name))

name = "Jane Doe"
print(id(name))  # Returns different memory address


# Mutable Data Types are those that can be changed once they are created.
# Mutable Data Types: list, dict, set, bytearray, user-defined classes

fruits = ["apple", "banana", "cherry"]
print(id(fruits))

fruits.append("orange")
print(id(fruits))  # Returns the same memory address
