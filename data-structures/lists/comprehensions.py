fruits = ["apple", "banana", "grape", "orange"]
fruits.append("apple")

fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)

fruits_filtered = [fruit for fruit in fruits if fruit != "apple"]
print(fruits_filtered)
