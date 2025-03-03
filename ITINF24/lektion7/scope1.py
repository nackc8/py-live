p = print
# I samma "scope", variabeln är
# tillgänglig
x = 1
p(x)


def dubbla(t):
    d = d * 2
    d = t * 2
    return d


p(dubbla(10))
# p(d)
# NameError: name 'd' is not defined
# d är en lokal variabel i dubbla
