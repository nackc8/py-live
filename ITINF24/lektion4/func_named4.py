# * betyder att vi kräver namnanrop på parametrarna
# till höger om den..

# / betyder att vi kräver positionella anrop på parametrarna
# till vänster om den..


def myprint(txt, /, *, start="ZZZ"):
    print(start + txt)


def myprint2(txt1, /, txt2, *, start="ZZZ"):
    print(start + txt1 + txt2)


myprint("Hello world", start="Inte zeta")
myprint(txt="Hello world", start="Inte zeta")
