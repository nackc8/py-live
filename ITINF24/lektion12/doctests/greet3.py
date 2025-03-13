# Testmetod: doctest
#
# doctest — Test interactive Python examples
#
"""
Fantastic module that greets people, or GREATS people.

You can even uppercase greetings!
>>> upperize(greet())
'HELLO STRANGER!'
"""


def greet(name=None):
    """Greets a fellow or named person

    >>> greet("Urban")
    'Hello Urban!'

    >>> greet()
    'Hello stranger!'
    """
    if name is None:
        return "Hello stranger!"
    else:
        return f"Hello {name}!"


def upperize(msg):
    """
    For people who don't like to use .upper()

    >>> upperize("hello")
    'HELLO'
    """
    return msg.upper()


if __name__ == "__main__":
    import doctest

    # Verbose skriver ut de som går bra också
    doctest.testmod(verbose=True)
