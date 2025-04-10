class Wallet:

    def __init__(self, amount):
        self._balance = amount  # Initialize _balance with the starting amount

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive\n")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
            else:
                print("Insufficient Balance\n")
        else:
            print("Withdrawal amount must be positive\n")

    def check_balance(self):
        print(f"Your balance is ${self._balance}\n")
        return self._balance


# Example usage:
wallet = Wallet(1000)  # Create a wallet with $1000
wallet.deposit(500)    # Deposit $500
wallet.withdraw(200)   # Withdraw $200
wallet.check_balance()  # Check balance (should show $1300)