# * betyder att vi kräver namnanrop på parametrarna
# till höger om den..


def myprint(txt, *, start="ZZZ"):
    print(start + txt)


myprint("Hello1")
# myprint("Hello2", "AAA") # Förbjudet pga *
myprint("Hello3", start="BBB")
