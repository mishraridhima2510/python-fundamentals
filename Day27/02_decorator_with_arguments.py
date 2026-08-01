# Decorator with Arguments

def decorator(func):
    def wrapper(name):
        print("Welcome")
        func(name)
    return wrapper

@decorator
def greet(name):
    print("Hello", name)

greet("Ridhima")
