user = ("John", "Doe", 30)
print(type(user))

point = (1, 2, 3)
point = 1, 2, 3
point = 1,

# Tuple concatenation
point = (1, 2) + (3, 4)
print(point)

# Tuple repetition
point = (1, 2) * 3
print(point)

# Tuple from iterable
point = tuple([1, 2])
print(point)
letters = tuple("Hello World")
print(letters)

# Accessing elements
print(user[0])

# Slicing
print(user[0:2])
print(user[0:])
print(user[:2])
print(user[:])

# Tuples are immutable

# Unpacking
point = (1, 2, 3)
x, y, z = point
print(x, y, z)

# Swapping variables
x = 10
y = 11
x, y = y, x
print(x, y)
