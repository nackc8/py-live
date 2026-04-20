tree = {
    "a": {
        "aa": 1,
    },
    "b": 2,
    "c": {
        "cc": {
            "ccc": {
                "cccc": 24,
            },
        },
    },
    "d": 123,
}


def deepsum(t):
    total = 0
    for key, value in t.items():
        if isinstance(value, int):
            total = total + value
        else:
            # add total of the value, as it is a dict
            total = total + deepsum(value)

    return total


p = print

p(deepsum(tree))
