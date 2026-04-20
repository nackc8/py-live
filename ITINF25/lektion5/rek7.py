def badrange(number, res=[]):
    number = number - 1

    res = res.copy()

    res.append(number)

    if number > 0:
        res = res + badrange(number)

    return res


outer_result = badrange(5)

for x in outer_result:
    print("x:", x)
