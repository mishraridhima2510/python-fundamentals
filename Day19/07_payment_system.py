class Payment:

    def pay(self):
        print("Processing Payment")

class UPI(Payment):

    def pay(self):
        print("Payment via UPI")

class Card(Payment):

    def pay(self):
        print("Payment via Card")

upi = UPI()
card = Card()

upi.pay()
card.pay()
