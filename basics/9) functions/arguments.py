# Default arguments

def add(a, b=2):
    return a + b


print(add(5))
print(add(5, 6))

# Keyword arguments

print(add(a=5, b=6))
print(add(b=6, a=5))


# Variable length arguments or *args

def addValues(a, b, *more):
    print(a)
    print(b)
    print(more)
    return a + b + sum(more)


print(addValues(5, 6, 7, 8, 9))
print(addValues(5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))


# Keyword variable length arguments or **kwargs

def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="John", Lastname="Wood", Email="johnwood@domain.com",
      Country="Wakanda", Age=25, Phone=9876543210)
