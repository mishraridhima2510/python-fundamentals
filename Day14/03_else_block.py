# Else Block

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print("Square =", number ** 2)
