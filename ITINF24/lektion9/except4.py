# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions

# Feltyper:

# TypeError - fel datatyp
# ValueError - rätt typ, men fel värde


class Hund:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError()
        if name == "":
            raise ValueError()

        self.name = name
        # Ger TypeError: can only concatenate str (not "int") to str

    def get_sentence(self):
        # TypeError: can only concatenate str (not "int") to str
        sentence = "Min hund " + self.name + " är gooo!"
        return sentence


p = print

# med raise smäller direkt
hund1 = Hund("")

p(hund1.get_sentence())
