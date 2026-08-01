# Bank Transaction Logger

def transaction(func):
    def wrapper(amount):
        print("Transaction Started")
        func(amount)
        print("Transaction Completed")
    return wrapper

@transaction
def deposit(amount):
    print("Deposited ₹", amount)

deposit(5000)
