def dela(a, b):
    return a / b


# samma! Funktioner def:ade enligt ovan kan anropas med positionella argument eller namngivna
print("Rad", "1", dela(5, 2), sep=": ")
print(
    "Rad:\n------",
    "2",
    dela(b=2, a=5),
    sep="\n   ",
    end="\n------",
)
