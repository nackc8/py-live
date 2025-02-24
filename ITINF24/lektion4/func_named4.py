# * betyder att vi kräver namnanrop på parametrarna
# till höger om den..

# / betyder att vi kräver positionella anrop på parametrarna
# till vänster om den..


def myprint(txt, /, *, start="ZZZ"):
    print(start + txt)


def myprint2(txt1, /, txt2, *, start="ZZZ"):
    print(start + txt1 + txt2)


# myprint(txt="Hello world", start="Inte zeta") # Förbjuden

# Båda funkar lika bra!
myprint2("Hello ", "world", start="---")
myprint2("Hello ", txt2="world", start="---")
