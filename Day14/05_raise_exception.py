# Raise Exception

age = int(input("Enter age: "))

if age < 18:
    raise Exception("Age must be at least 18.")

print("Access Granted")
