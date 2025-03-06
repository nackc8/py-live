import scope2_called

p = print

result = scope2_called.get_x()

direkt = scope2_called.x

scope2_called.x = 333

result2 = scope2_called.get_x()


def hundra():
    return 100


# vi byter ut funktionen
scope2_called.get_x = hundra

result3 = scope2_called.get_x()
