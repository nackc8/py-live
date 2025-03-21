# Testmetod: doctest
#
# doctest — Test interactive Python examples
#
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
