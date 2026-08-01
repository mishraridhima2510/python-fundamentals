# Multiple Decorators

def star(func):
    def wrapper():
        print("*" * 20)
        func()
        print("*" * 20)
    return wrapper

def hash_symbol(func):
    def wrapper():
        print("#" * 20)
        func()
        print("#" * 20)
    return wrapper

@star
@hash_symbol
def message():
    print("Python")

message()
