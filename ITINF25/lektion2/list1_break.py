checkout_list = [30, 100, 20, 5, 5, 90]

customer_wallet = 200
total = 0
for grocery in checkout_list:
    if customer_wallet < total + grocery:
        break  # AVBRYT NU!
    total = total + grocery
    print("Sliding total:", total)

print("---------")
print("Final total", total)
