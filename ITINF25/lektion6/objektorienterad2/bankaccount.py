import sys

# Flyttat in den globala variabeln next_account_id till att vara
# en klassvariabel. En variabel som är gemensam för själva klassen, och inte
# objekten som self är nedan.


class BankAccount:
    # En variabel som tillhör själva klassen
    next_account_id = 1

    def __init__(self, name):
        self.name = name

        BankAccount.next_account_id

        self.id = BankAccount.next_account_id
        BankAccount.next_account_id += 1
        self.balance = 0

    # Exempel på en magisk metod. Just denna gör att objektet skrivs ut
    # som en sträng på ett fint sätt för användaren.
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


# Senare!
# def list_accounts():
#     return bankaccounts.copy()


# Mål
# - Lagra ett kontoid ✔
# - Lagra ett namn ✔
# - Lagra saldo (balance) ✔
# - Insättning (deposit) ✔
# - Uttag (withdraw) ✔
# - Lägg till ett konto ✔
# - Lista konton  ✔
# - Hitta konto  ✔
