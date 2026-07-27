# Infinite Generator

def infinite():

    number = 1

    while True:
        yield number
        number += 1

generator = infinite()

for _ in range(5):
    print(next(generator))
