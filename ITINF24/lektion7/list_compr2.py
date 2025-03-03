lst1 = []
for n in range(0, 10):
    val = 2**n + n
    if val % 2 == 0:
        lst1.append(val)

lst2 = [2**n + n for n in range(0, 10) if 2**n + n % 2 == 0]

# print("lika", lst1, lst2)
