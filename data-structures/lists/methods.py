fruits = ["apple", "banana", "grape", "orange"]

# Add Items
fruits.append("mango")
print(fruits)

# Add Items at Specific Index
fruits.insert(0, "lemon")
print(fruits)

# Remove Items
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.clear()
print(fruits)

# Delete Items
del fruits[0:2]
print(fruits)

# Find Items
fruits = ["apple", "banana", "grape", "orange"]
print(fruits.index("banana"))

# Check for Item
print("mango" in fruits)

# Count Items
fruits.append("apple")
print(fruits.count("apple"))

# Mappping
fruits_map = map(lambda fruit: fruit.upper(), fruits)  # returns a map object
print(fruits_map)
fruits_upper = list(fruits_map)
print(fruits_upper)

# Filter
fruits_filter = filter(lambda fruit: fruit != "apple", fruits)
print(fruits_filter)
fruits_filtered = list(fruits_filter)
print(fruits_filtered)

# Zip (Combine Lists)
letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["John", "Eric", "Jessica", "Jane"]
zip_list = zip(letters, numbers, names)  # returns a zip object
print(zip_list)
zip_list = list(zip_list)
print(zip_list)


# Unzip
letters, numbers, names = zip(*zip_list)
