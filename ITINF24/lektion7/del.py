lst1 = ["björn", "anka", "groda", "myra"]

# fel, det blir samma målobjekt
# lst2 = lst1

# Kopia! Fristående!
lst2 = lst1[:]

del lst1[1]
# samma som: lst1.pop(1)
