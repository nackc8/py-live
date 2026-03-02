# TypeError: https://docs.python.org/3/library/exceptions.html#TypeError
# Kort sammanfattning: Fel typ
#
# ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
# Kort sammanfattning: Rätt typ, men fel värde ändå


def greet(full_name):
    parts = full_name.split()
    if (len(parts) < 2):
        raise 
