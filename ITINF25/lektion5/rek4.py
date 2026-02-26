def badrange(number):
    print("number:", number)
    number = number - 1

    if number > 0:
        badrange(number)


badrange(5)
