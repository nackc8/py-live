p = print
age = 100


def femtio():
    p("femtio:", age)
    age = 9999
    p("femtio:", age)


femtio()
