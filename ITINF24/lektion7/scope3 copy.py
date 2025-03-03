p = print
lst = []


def tuut():
    # lst är muterbar
    lst.append("tuut")


tuut()


def boom():
    lst = p("inne i boom()", ["boom"])


boom()

p("utanför direkt i filen", lst)
