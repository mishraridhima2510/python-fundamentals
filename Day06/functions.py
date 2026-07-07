# Day 06 - Functions

def greet():
    print("Hello, World!")

greet()


def add(a, b):
    return a + b

print("Sum:", add(10, 20))


def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(even_or_odd(7))


def maximum(a, b):
    return max(a, b)

print("Maximum:", maximum(15, 9))


def square(n):
    return n * n

print("Square:", square(6))
