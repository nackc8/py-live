# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions

# Feltyper:

# TypeError - fel datatyp


class Hund:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError()

        self.name = name
        # Ger TypeError: can only concatenate str (not "int") to str

    def get_sentence(self):
        # TypeError: can only concatenate str (not "int") to str
        sentence = "Min hund " + self.name + " är gooo!"
        return sentence


# med raise smäller direkt
hund1 = Hund(34)
# (innan raise smäller sent) fel 1: Fel typ
hund1.get_sentence()
