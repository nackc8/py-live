import bankaccount

p = print

bankaccount.create_account(1, "Sven")
bankaccount.deposit_to_account(1, 100)

bankaccount.create_account(2, "Ulla")
bankaccount.deposit_to_account(2, 10000)

bankaccount.withdraw_from_account(2, 1000)
bankaccount.deposit_to_account(1, 1000)

p(bankaccount.list_accounts())
