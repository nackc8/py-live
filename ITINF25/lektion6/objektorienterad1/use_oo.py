import bankaccount

p = print

sven_account = bankaccount.BankAccount("Sven")
sven_account.deposit_to_account(100)

ulla_account = bankaccount.BankAccount("Ulla")
ulla_account.deposit_to_account(10000)

ulla_account.withdraw_from_account(1000)
sven_account.deposit_to_account(1000)

p(sven_account, ulla_account)
