# Shopping Cart

class Cart:

    def __init__(self, products):
        self.products = products

    def __len__(self):
        return len(self.products)

cart = Cart(["Laptop", "Mouse", "Keyboard"])

print(len(cart))
