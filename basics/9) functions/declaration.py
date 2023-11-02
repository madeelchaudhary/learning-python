def greet(name):
    print("Hello, " + name + ". Good morning!")


greet('Harry')

# If a function doesn't have a return statement, it returns None

print(greet('Harry'))
# print(greet('Harry') + '!')  # Error


def add(a, b):
    return a + b


print(add(5, 6))

# Return multiple values from a function


def calc(a, b):
    return a + b, a - b, a * b, a / b


print(calc(5, 6))
