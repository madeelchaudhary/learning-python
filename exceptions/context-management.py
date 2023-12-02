# Context management protocol
# => context managers are objects that allocate and release resources. they implement the context management protocol. they are typically used with the with statement

# -) they implement the __enter__ and __exit__ methods
# __enter__ is called when execution enters the context of the with statement
# __exit__ is called when execution exits the context of the with statement

with open("app.py") as file:
    print("File opened.")

with open("app.py") as file, open("another.txt") as target:
    print("File opened.")
