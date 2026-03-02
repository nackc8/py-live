from custom import BankAccount, NegativeAmountError

try:
    amount = int(input("How much do you deposit to Ulla? "))
    ulla = BankAccount("Ulla")
    ulla.deposit_to_account(amount)
except NegativeAmountError:
    print("PROGNOSIS NEGATIVE!")
