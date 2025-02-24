def halvera(tal):
    return tal / 2


def dubbla(tal):
    return tal * 2


def modifiera(tal, fn):
    return fn(tal)


modifiera(5, dubbla)
