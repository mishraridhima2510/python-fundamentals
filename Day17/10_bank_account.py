class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):

        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)

account = BankAccount("Ridhima", 5000)

account.deposit(2000)

account.withdraw(1500)

account.display()
