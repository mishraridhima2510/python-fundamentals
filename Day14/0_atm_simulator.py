balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

    print("Transaction Successful")
    print("Remaining Balance:", balance)

except ValueError:
    print("Please enter a valid amount.")

except Exception as e:
    print(e)
