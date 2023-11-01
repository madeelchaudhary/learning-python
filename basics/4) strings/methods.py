greet = "Hello John Doe"

print(greet.upper())
print(greet.lower())
print(greet.title())
print(greet.capitalize())
print(greet.swapcase())

print(greet.count("o"))
print(greet.count("o", 0, 5))
print(greet.strip())
print(greet.strip("H"))

print(greet.replace("John", "Jane"))

print(greet.split())
print(greet.split(" "))

print(greet.find("John"))
print(greet.index("John"))

print(greet.startswith("Hello"))
print(greet.endswith("Doe"))

print(greet.isalpha())

print("John" in greet)
print("Jane" not in greet)
