from custom_pre import BankAccount

amount = int(input("How much do you deposit to Ulla? "))

ulla = BankAccount("Ulla")
ulla.deposit_to_account(amount)
