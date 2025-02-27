def palindromish(s, g=None):
    pass


print(palindromish("radar", 2) == True)
print(palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3) == True)
print(palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4) == False)
print(palindromish("example", 3) == False)
print(palindromish("naturrutan") == True)
print(palindromish("kajak", 1000) == True)
print(palindromish("solros", 2) == True)
print(palindromish("solros", 3) == False)
