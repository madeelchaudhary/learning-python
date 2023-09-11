letters = ["a", "b", "c", "d"]

fruits = ["apple", "banana", "orange", "grape"]

# Two dimensional list
matrix = [[0, 1], [2, 3]]

# List Concatenation
combined = letters + fruits

# List Repetition
numbers = [1, 2, 3] * 3

print(numbers)

# List from Iterables
numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)

# Accessing Items
print(letters[0])
print(letters[-1])  # Last item

# Slicing
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])  # Copy of the list

# Modify Lists
letters[0] = "A"
print(letters)

# Step
numbers = list(range(20))
print(numbers[::2])  # Every second item
print(numbers[::-1])  # Reverse the list

# Unpacking "Variables must match the number of items in the list"
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)

# Unpacking with Rest
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other = numbers
print(first, second, other)
