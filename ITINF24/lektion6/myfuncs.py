def gnumber(num):
    while num > 100:
        num = num / 2.3
    return num


n = gnumber(9000)
print("Mitt gnumber:", gnumber)
# med f-sträng
print(f"Mitt gnumber: {gnumber}")
