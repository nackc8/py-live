# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions


class Hund:
    def __init__(self, namn):
        pass
        # Ger TypeError: can only concatenate str (not "int") to str

    def get_sentence(self):
        sentence = f"Min hund " + namn + " är gooo!"
        return sentence


# fel 1: Fel typ
hund1 = Hund(34)
hund1.get_sentence()
