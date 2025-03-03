import scope2_called

p = print

result = scope2_called.get_x()

direkt = scope2_called.x

scope2_called.x = 222

result2 = scope2_called.get_x()
