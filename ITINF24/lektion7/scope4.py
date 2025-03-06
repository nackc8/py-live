p = print
age = 100


def femtio():
    global age
    p("femtio:", age)
    age = 9999
    p("femtio:", age)


femtio()

p("sist", age)
