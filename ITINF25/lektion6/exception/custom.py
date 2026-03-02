import sys


class BankAccount:
    # En variabler som tillhör själva klassen
    # class variables
    next_account_id = 1
    accounts = []

    def __init__(self, name):
        self.name = name

        BankAccount.next_account_id

        self.id = BankAccount.next_account_id
        BankAccount.next_account_id += 1
        self.balance = 0
        BankAccount.accounts.append(self)

    def __str__(self):
        return f"[ BankAccount | Id: {self.id}, Name: {self.name}, Balance: {self.balance} ]"

    def deposit_to_account(self, amount):
        if amount < 0:
            print(
                f"Error: Cannot deposit a negative amount to {self.id}",
                file=sys.stderr,
            )
            sys.exit(2)
        self.balance += amount

    def withdraw_from_account(self, amount):
        if amount < 0:
            print(
                f"Error: Cannot withdraw a negative amount from {self.id}",
                file=sys.stderr,
            )
            sys.exit(2)
        self.balance -= amount

    # Dekorator (eng Decorator) för att markera en metod som är
    # klassgemensam. Passar ihop med klassvariabler.
    @classmethod
    def list(cls):
        # I detta fall så är cls = BankAccount
        return cls.accounts.copy()
