class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        self.show_balance()
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds!")
        self.show_balance()
    
    def show_balance(self):
        print(f"Current balance: ${self.balance}")
    
    def transfer(self, amount, to_account):
        if amount <= self.balance:
            self.balance -= amount
            to_account.deposit(amount)
            print(f"Transferred ${amount} to {to_account.account_holder}")
        else:
            print("Transfer failed: Insufficient funds")

# Create accounts
account1 = BankAccount("AmirKhan", 1000)
account2 = BankAccount("Sara", 500)

# Perform operations
account1.deposit(200)
account1.withdraw(300)
account1.transfer(400, account2)