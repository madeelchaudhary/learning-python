# while loop is used to iterate over a block of code as long as the test expression (condition) is true.

i = 1
while i < 10:
    print(i)
    i += 1

# while/else loop
i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("Loop is completed")
