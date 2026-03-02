from custom_pre import BankAccount

try:
    amount = int(input("How much do you deposit to Ulla? "))
    ulla = BankAccount("Ulla")
    ulla.deposit_to_account(amount)
except ValueError as e:
    if "negative" in str(e):
        print("Du skrev ett negativt tal!")
    else:
        print("Nått är galet")
