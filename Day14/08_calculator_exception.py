# Safe Calculator

try:
    a = int(input("First Number: "))
    b = int(input("Second Number: "))

    print("Division =", a / b)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
