user = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

user = dict(name="John", age=36, country="Norway")

# Keys can be of any immutable type

# Accessing items
print(user["name"])
print(user.get("name", "Not Found"))

# Changing values
user["name"] = "Jane"
print(user)

user.update({"name": "John"})
print(user)

# Check if key exists
print("name" in user)

# Removing items
user.pop("name", None)
print(user)

user.popitem()
print(user)

del user["age"]
print(user)

user.clear()
print(user)
