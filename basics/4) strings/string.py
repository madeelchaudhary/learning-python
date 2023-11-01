book = "C Programming Language by Brian W. Kernighan and Dennis M. Ritchie"

# Print the length of the string
print(len(book))

# Indexing
print(book[0])
print(book[1])
print(book[-1])  # Negative indexing

# Slicing
print(book[0:3])
print(book[4:11])
print(book[4:])
print(book[:11])
print(book[:])  # Print the entire string


# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# String Replication
print("Hello " * 3)

# Escape Characters
print("Hello \"World\"")
print("Hello \nWorld")
print("Hello \tWorld")
print("Hello \\World")
