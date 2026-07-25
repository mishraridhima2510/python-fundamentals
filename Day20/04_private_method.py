# Private Method

class Bank:

    def __balance(self):
        print("Current Balance: ₹10000")

    def show(self):
        self.__balance()

bank = Bank()

bank.show()
