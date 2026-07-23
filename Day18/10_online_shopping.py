class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

class Electronics(Product):

    def display(self):

        print("Product:", self.name)
        print("Price: ₹", self.price)

item = Electronics("Laptop", 65000)

item.display()
