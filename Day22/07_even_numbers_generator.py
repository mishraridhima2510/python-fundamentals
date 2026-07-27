# Even Numbers Generator

def even_numbers(limit):

    for number in range(2, limit + 1, 2):
        yield number

for number in even_numbers(10):
    print(number)
