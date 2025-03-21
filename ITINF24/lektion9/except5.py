# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions

# Feltyper:

# TypeError - fel datatyp
# ValueError - rätt typ, men fel värde
# Alla errors/exceptions ärver av Exception


class InvalidDogNameError(ValueError):
    pass


class DogNameTypeError(TypeError):
    pass


class Dog:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if name == "":
            raise InvalidDogNameError("Empty name not allowed")

        self.name = name
        # Ger TypeError: can only concatenate str (not "int") to str

    def get_sentence(self):
        # TypeError: can only concatenate str (not "int") to str
        sentence = "Min hund " + self.name + " är gooo!"
        return sentence


p = print

# med raise smäller direkt
try:
    hund1 = Dog("")
except InvalidDogNameError:
    hund1 = Dog("123")
except DogNameTypeError:
    hund1 = Dog("999")

p(hund1.get_sentence())
