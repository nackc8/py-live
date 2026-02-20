checkout_list = [30, 100, 20, 5, 5, 90]

customer_wallet = 200
total = 0
for grocery in checkout_list:
    next_total = total + grocery
    if customer_wallet < next_total:
        break  # AVBRYT NU!
    total = next_total
    print("Sliding total:", total)

print("---------")
print("Final total", total)
