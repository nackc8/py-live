# Fel, eftersom den saknas BASFALL:
# RecursionError: maximum recursion depth exceeded while calling a Python object


def badrange(number):
    print("number:", number)
    badrange(number)


badrange(5)
