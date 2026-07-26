# Library Management

class Library:

    def __init__(self, books):
        self.books = books

    def __repr__(self):
        return f"Library({self.books} Books)"

library = Library(150)

print(repr(library))
