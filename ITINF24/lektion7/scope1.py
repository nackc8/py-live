p = print
# I samma "scope", variabeln är
# tillgänglig
x = 1
p(x)


def dubbla(t):
    # d = d * 2
    # UnboundLocalError: cannot access local variable 'd' where it is not associated with a value
    # d sätts på raden under, försvinner
    # efter anropets slut
    d = t * 2
    return d


p(dubbla(10))
# p(d)
# NameError: name 'd' is not defined
# d är en lokal variabel i dubbla

# de variabler som sätts utanför
# funktioner = globala för modulen
