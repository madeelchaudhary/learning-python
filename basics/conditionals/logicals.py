# Python also supports truthy and falsy values. The following values are considered falsy in Python:
#  1. None
#  2. False
#  3. 0
#  4. 0.0
#  5. ""
#  6. []
#  7. ()
#  8. {}
#  9. set()
#  10. range(0)

text = ""

if not text:
    print("Text is not empty")
else:
    print("Text is empty")

age = 20

if age >= 18 and age <= 65:
    print("Eligible")

if 18 <= age <= 65:
    print("Eligible")

if age < 18 or age > 65:
    print("Not Eligible")
