# Bank Balance

class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def display(self):
        print("Balance:", self.__balance)

account = Account(5000)

account.deposit(2000)

account.display()
