from sys import getsizeof
# generator object does not store all the values in memory, it yields one value at a time

square = (x * x for x in range(10))

print('generator:', square)

print('first item:', next(square))

# or you can use a for loop to iterate over the generator object

for num in square:
    print(num)

# get size of generator object
print('size of generator object:', getsizeof(square))
