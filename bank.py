# bank.py
class InsufficientFunds(Exception):
    """Raised when a withdrawal is larger than the balance."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(f"balance is only {self.balance}")
        self.balance -= amount

    def add_interest(self, rate):
        self.balance = self.balance * (1 + rate)
