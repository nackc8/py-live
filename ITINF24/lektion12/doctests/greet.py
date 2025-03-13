# Testmetod: doctest
#
# doctest — Test interactive Python examples
#
def greet(name=None):
    """Greets a fellow or named person"""
    if name is None:
        return "Hello stranger!"
    else:
        return f"Hello {name}!"


print(greet.__doc__)
