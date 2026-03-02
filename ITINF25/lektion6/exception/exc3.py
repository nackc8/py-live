def delat_med_ett(divisor):
    try:
        result = 1 / divisor
        return result
    except ZeroDivisionError as e:
        print("We handle ZeroDivisionError", e)
        return 0


# Undantaget "bubblar upp" då det inte fångas, vi
# fångar bara ZeroDivisonError. Men i vårt fall är
# undantaget:
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
res = delat_med_ett("hej")
print(res)
