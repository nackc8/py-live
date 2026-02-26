# Global - den står utan indentering
x = 4


def x_reader():
    # variabler som sätts är lokala som standard
    y = 123
    print(x, y)


x_reader()
