class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction(f"Deposit: +${amount}")
            print(f"Successfully deposited ${amount}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__add_transaction(f"Withdrawal: -${amount}")
                print(f"Successfully withdrew ${amount}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")
    
    def get_balance(self):
        return self.__balance
    
    def __add_transaction(self, description):
        """Private method to add transaction to history"""
        self.__transaction_history.append(description)
    
    def get_transaction_history(self):
        """Public method to get transaction history"""
        return self.__transaction_history.copy()
    
    def apply_interest(self, rate):
        """Apply interest to the account"""
        interest = self.__balance * rate / 100
        self.__balance += interest
        self.__add_transaction(f"Interest: +${interest:.2f}")
        print(f"Applied ${interest:.2f} interest")

# Create account
account = BankAccount("AmirKhan", 1000)

# Perform operations
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # Should fail
account.apply_interest(5)

print(f"\nCurrent balance: ${account.get_balance():.2f}")
print("\nTransaction History:")
for transaction in account.get_transaction_history():
    print(f"  {transaction}")