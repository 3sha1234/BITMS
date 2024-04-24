class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

#entering the balance
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(initial_balance)

# Example usage
print("Balance:", account.get_balance())

# Deposit
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Withdrawal
withdrawal_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdrawal_amount)

print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())
