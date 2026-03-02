# TypeError: https://docs.python.org/3/library/exceptions.html#TypeError
# Kort sammanfattning: Fel typ
#
# ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
# Kort sammanfattning: Rätt typ, men fel värde ändå


def greet(full_name):
    if isinstance(full_name, str):
        raise TypeError("The name must be a string")

    parts = full_name.split()
    if len(parts) < 2:
        raise ValueError("The name must have at least two parts")


greet("bosse")
