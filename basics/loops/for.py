# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

for i in range(1, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

for letter in "Hello":
    print(letter)

# for/else loop
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

for i in range(1, 10):
    print(i)
else:
    print("Loop is completed")

for i in range(1, 10):
    if i == 5:
        break
    print(i)
else:
    print("Loop is completed")
