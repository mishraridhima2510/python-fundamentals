# Operator Overloading

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"

money1 = Money(500)
money2 = Money(700)

print(money1 + money2)
