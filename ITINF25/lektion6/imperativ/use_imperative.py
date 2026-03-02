import bankaccount

p = print

bankaccount.create_account(1, "Sven")
bankaccount.deposit_to_account(1, 100)
p(bankaccount.list_accounts())
