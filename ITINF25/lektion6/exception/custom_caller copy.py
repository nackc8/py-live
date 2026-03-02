from custom import BankAccount

try:
    amount = int(input("How much do you deposit to Ulla? "))
    ulla = BankAccount("Ulla")
    ulla.deposit_to_account(amount)
except ValueError as e:
    print("Du skrev ett negativt tal!")
