first_name = "john"
last_name = "doe"

print(f"Hello {first_name} {last_name}")
print(F"Hello {first_name.title()} {last_name.title()}")

age = 32

print("Hello {} {}, you are {} years old.".format(first_name, last_name, age))
print("Hello {0} {1}, you are {2} years old.".format(
    first_name, last_name, age))
print("Hello {first_name} {last_name}, you are {age} years old.".format(
    first_name="John", last_name="Doe", age=32))
