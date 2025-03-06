aTuple = (100, 200, 300, 400, 500)
# AttributeError: 'tuple' object has no attribute 'pop'
# Ingen pop då tuplens längd inte får ändras
aTuple.pop(2)
print(aTuple)
