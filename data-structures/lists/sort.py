numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# sorted function  "returns a new array"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(numbers))

# sort list of tuples/object
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    item[1]


print(sorted(items, key=sort_item))

print(sorted(items, key=lambda item: item[1]))  # lambda function
