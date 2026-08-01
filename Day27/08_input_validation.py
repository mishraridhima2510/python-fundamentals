# Input Validation Decorator

def validate(func):
    def wrapper(age):
        if age >= 18:
            func(age)
        else:
            print("Invalid Age")
    return wrapper

@validate
def vote(age):
    print("Eligible to Vote")

vote(20)
vote(15)
