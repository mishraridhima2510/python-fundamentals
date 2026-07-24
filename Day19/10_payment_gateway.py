from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentGateway):

    def pay(self, amount):
        print(f"₹{amount} paid successfully using UPI.")

class CreditCard(PaymentGateway):

    def pay(self, amount):
        print(f"₹{amount} paid successfully using Credit Card.")

upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1200)
