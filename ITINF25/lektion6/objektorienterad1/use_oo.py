import bankaccount

p = print

sven = bankaccount.BankAccount("Sven")
sven.deposit_to_account(100)

ulla = bankaccount.BankAccount("Ulla")
ulla.deposit_to_account(10000)

ulla.withdraw_from_account(1000)
sven.deposit_to_account(1000)

p(sven, ulla)
