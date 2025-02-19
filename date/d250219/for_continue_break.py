sum = 0
for a in range(2, 100):
    udda = a % 2
    if bool(udda):
        sum = sum + a

print("summa", sum)
