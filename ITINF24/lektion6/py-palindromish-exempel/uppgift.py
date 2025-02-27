def palindromish(s, g=None):
    pass


palindromish("radar", 2) == True
palindromish([1, 2, 3, 50, 60, 3, 2, 1], 3) == True
palindromish([1, 2, 3, 50, 60, 3, 2, 1], 4) == False
palindromish("example", 3) == False
palindromish("naturrutan") == True
palindromish("kajak", 1000) == True
palindromish("solros", 2) == True
palindromish("solros", 3) == False
