lst = ["ove", "mohammed", "xi", "eva"]

lst2 = list(enumerate(lst, 1))

print(lst2)

# dålig kod för den som kan enumerate
# men inte len()

length = lst2[-1][0]

print("Length: ", length)
