# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions


class Hund:
    def __init__(self, namn):
        mening = f"Min hund " + namn + " är gooo!"


# fel 1: Fel typ
hund1 = Hund(34)
