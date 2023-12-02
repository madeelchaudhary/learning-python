# The else block will only run if no exceptions are thrown.
try:
    print("try")
except:
    print("except")
else:
    print("else")

# Output: try else

try:
    print("try")
    raise ValueError
except:
    print("except")
else:
    print("else")

# Output: try except
