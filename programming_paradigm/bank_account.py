class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")