bankaccounts = []


def create_account(account_id, name):
    # Ett konto = en lista [account_id: int, name: str, balance: int]
    account = [account_id, name, 0]
    bankaccounts.append(account)


def deposit(account_id, amount):
    for a in bankaccounts:
        pass


# Mål
# - Lagra ett kontoid ✔
# - Lagra ett namn ✔
# - Lagra saldo (balance) ✔
# - Insättning (deposit)
# - Uttag (withdraw)
# - Lägg till ett konto ✔
# - Lista konton
