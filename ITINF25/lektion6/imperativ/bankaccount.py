import sys

bankaccounts = []


def create_account(account_id, name):
    # Ett konto = en lista [account_id: int, name: str, balance: int]
    account = [account_id, name, 0]
    bankaccounts.append(account)


def deposit(account_id, amount):
    for account in bankaccounts:
        if account[0] == account_id:
            account[2] += amount
            break
    else:
        # "else" körs om ingen break har körts

        # 
        print(f"Error: Cannot find account with id {account_id}", file=sys.stderr)
        sys.exit(2)


# Mål
# - Lagra ett kontoid ✔
# - Lagra ett namn ✔
# - Lagra saldo (balance) ✔
# - Insättning (deposit)
# - Uttag (withdraw)
# - Lägg till ett konto ✔
# - Lista konton
