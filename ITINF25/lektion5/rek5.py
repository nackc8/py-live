def badrange(number):
    number = number - 1

    recursive_result = [number]
    if number > 0:
        recursive_result = recursive_result + badrange(number)

    return recursive_result


outer_result = badrange(5)

for x in outer_result:
    print("x:", x)
