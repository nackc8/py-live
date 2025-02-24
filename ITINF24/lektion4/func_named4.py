# * betyder att vi kräver namnanrop på parametrarna
# till höger om den..

# / betyder att vi kräver positionella anrop på parametrarna
# till vänster om den..


def myprint(txt, /, *, start="ZZZ"):
    print(start + txt)


myprint("Hello world", start="Inte zeta")
myprint(txt="Hello world", start="Inte zeta")
