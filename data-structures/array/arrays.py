from array import array

# Only use arrays when you need to store a large amount of data of the same type

# Create an array of integers
arr = array('i', [1, 2, 3, 4, 5])

# Create an array of floats
arr = array('f', [1.1, 2.2, 3.3])

# Create an array of strings
arr = array('u', ['a', 'b', 'c'])

# Add elements to an array
arr = array('i', [1, 2, 3])
arr.append(4)
arr.insert(2, 5)
