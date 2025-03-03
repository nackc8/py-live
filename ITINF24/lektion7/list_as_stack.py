# Använd debuggern för att förstå bättre!

# Den som vill kan gärna uttöka med { } samt
# snygga till koden
def paran_balanced(txt):
    par_stack = []
    for bokstav in txt:
        if bokstav == "(":
            par_stack.append("(")
        if bokstav == ")":
            if len(par_stack) == 0:
                return False
            par_stack.pop()

    return len(par_stack) == 0


result = paran_balanced(")")
print("Testfall pass: ", result == False)


# funktions som svarar sant, om parenteserna matchar
#
# exempel på match: True
#   (hejsan)
#   ()
#   (hejsan(hoppsan))
# exempel på när det inte matchar: False
#   (
#   (hejsan(hoppsan)
#   (hejsan))
