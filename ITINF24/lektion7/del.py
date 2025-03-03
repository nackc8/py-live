lst1 = ["björn", "anka", "groda", "myra", "hund", "katt", "krokodil"]

# fel, det blir samma målobjekt
lst2 = lst1

# Kopia! Fristående!
lst2 = lst1[:]
lst3 = lst1[:]

# del lst1[1]
# samma som: lst1.pop(1)

# tilldela en ny del i lst3
lst3[2:4] = ["hej!!!", "Hallå!!!", "Fler!!"]
