# Fel, eftersom den saknas BASFALL:
# RecursionError: maximum recursion depth exceeded while calling a Python object


def badrange(number):
    print("number:", number)
    # Ett basfall då anropet bara sker om man INTE är i basfallet
    if number <= 3:
        badrange(number)


badrange(5)
