# Custom Iterator

class Numbers:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        raise StopIteration

numbers = Numbers()

for number in numbers:
    print(number)
