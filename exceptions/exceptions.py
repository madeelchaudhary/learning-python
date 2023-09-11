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
