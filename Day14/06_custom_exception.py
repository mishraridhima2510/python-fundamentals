# Custom Exception

class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

try:
    if age < 18:
        raise InvalidAgeError("Invalid Age")

    print("Eligible")

except InvalidAgeError as e:
    print(e)
