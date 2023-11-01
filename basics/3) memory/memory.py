name = "John Doe"
print(name)

print(id(name))  # Returns the memory address of the variable

name = "Jane Doe"
print(name)

# Python interpreter will allocate a new memory address for the new value of the variable
print(id(name))
