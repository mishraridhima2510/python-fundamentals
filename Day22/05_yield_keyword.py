# Yield Keyword

def countdown():

    for number in range(5, 0, -1):
        yield number

for value in countdown():
    print(value)
