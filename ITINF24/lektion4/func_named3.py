# vi vill att start ska vara
# valfri...
def myprint(txt, *, start="ZZZ"):
    print(start + txt)


myprint("Hello1")
# myprint("Hello2", "AAA") # Förbjudet pga *
myprint("Hello3", start="BBB")
