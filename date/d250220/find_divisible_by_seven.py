lst = [2, 7, 9, 15, 14, 19]

hit = None

for num in lst:
    if num % 13 == 0:
        hit = num

print("hit:", hit)
