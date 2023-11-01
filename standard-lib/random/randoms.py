import random
import string

ran_fl = random.random()
print(ran_fl)

ran_int = random.randint(1, 10)
print(ran_int)

ran_choice = random.choice([1, 2, 3, 4, 5])
print(ran_choice)

ran_choices = random.choices([1, 2, 3, 4, 5], k=2)
ran_choices = random.choices('abcdefghijkl', k=2)

# random password
password = random.choices(string.ascii_letters + string.digits, k=8)

# shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
