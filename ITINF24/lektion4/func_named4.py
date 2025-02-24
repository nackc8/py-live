# * betyder att vi kräver namnanrop på parametrarna
# till höger om den..


def myprint(txt, *, start="ZZZ"):
    print(start + txt)


myprint("Hello world", start="Inte zeta")
