# Function Call Counter

def counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Called", count, "times")
        func()

    return wrapper

@counter
def hello():
    print("Hello")

hello()
hello()
hello()
