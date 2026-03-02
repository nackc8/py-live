import sys

bankaccounts = []

next_account_id = 1


class BankAccount:
    def __init__(self, name):
        # Notera att self.name och name är olika variabler
        self.name = name
        global next_account_id
        self.id = next_account_id
        next_account_id += 1
        self.balance = 0

    def __str__(self):
        return f"[ BankAccount | Id: {self.id}, Name: {self.name} ]"

    def deposit_to_account(self, amount):
        if amount < 0:
            print(
                f"Error: Cannot deposit a negative amount to {self.id}",
                file=sys.stderr,
            )
            sys.exit(2)
        self.balance += amount


def list_accounts():
    return bankaccounts.copy()


def get_account(account_id):
    for account in bankaccounts:
        if account[0] == account_id:
            return account.copy()
    else:
        # "else" körs om ingen break har körts

        # Bash-motsvarighet: echo "Error: Cannot..." >&2
        print(
            f"Error: Cannot find account with id {account_id}",
            file=sys.stderr,
        )
        # Bash-motsvarighet: exit 2
        sys.exit(2)


def withdraw_from_account(account_id, amount):
    if amount < 0:
        print(
            f"Error: Cannot withdraw a negative amount from {account_id}",
            file=sys.stderr,
        )
        sys.exit(2)

    for account in bankaccounts:
        if account[0] == account_id:
            account[2] -= amount
            break
    else:
        # "else" körs om ingen break har körts

        # Bash-motsvarighet: echo "Error: Cannot..." >&2
        print(
            f"Error: Cannot find account with id {account_id} for withdrawal",
            file=sys.stderr,
        )
        # Bash-motsvarighet: exit 2
        sys.exit(2)


# Mål
# - Lagra ett kontoid ✔
# - Lagra ett namn ✔
# - Lagra saldo (balance) ✔
# - Insättning (deposit) ✔
# - Uttag (withdraw) ✔
# - Lägg till ett konto ✔
# - Lista konton  ✔
# - Hitta konto  ✔
