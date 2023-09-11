nums = [1, 2, 4, 5, 6, 4, 3, 2, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

un_nums = set(nums)
print(un_nums)

un_letters = {'a', 'b', 'c', 'a', 'b', 'c'}
print(un_letters)

# remove item from set
un_letters.remove('a')
print(un_letters)

# add item to set
un_letters.add('d')
print(un_letters)

# check if item is in set
print('d' in un_letters)

# set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
print(set1 | set2)

# intersection
print(set1 & set2)

# difference
print(set1 - set2)

# symmetric difference
print(set1 ^ set2)

# subset
print(set1 <= set2)

# superset
print(set1 >= set2)
