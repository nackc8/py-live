# Fel, eftersom den saknas BASFALL:
# RecursionError: maximum recursion depth exceeded while calling a Python object


def badrange(number):
    print("number:", number)
    # Ett basfall via return
    if number > 3:
        return
    badrange(number)


badrange(5)
