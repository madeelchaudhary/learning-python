try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")

# try/except/else
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# try/except/finally
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    print("This will always run.")

#  Multiple exceptions
try:
    age = int(input("Age: "))
    xfactor = 10 / age
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# except ValueError:
#     print("You didn't enter a valid age.")
except (ValueError, ZeroDivisionError):  # This is the same as above
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

#  Raising exceptions
try:
    raise ValueError("This is a value error")
except ValueError as ex:
    print(ex)

# with blocks
try:
    # This will close the file automatically, even if an exception is thrown
    # you can use this with any object that implements the context manager
    # multiple objects can be used in the same with block by separating them with a comma
    with open("app.py") as file:
        print("File opened.")
except FileNotFoundError:
    print("File not found.")
print("After try block.")
