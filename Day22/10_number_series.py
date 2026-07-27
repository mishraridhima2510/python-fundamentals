# Number Series Generator

def series(start, end):

    while start <= end:
        yield start
        start += 1

for number in series(1, 10):
    print(number)
