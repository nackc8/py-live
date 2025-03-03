def paran_balanced(txt):
    par_stack = []
    for bokstav in txt:
        if bokstav == "(":
            par_stack.append("(")
        if bokstav == ")":
            par_stack.pop()
        print(bokstav, par_stack)

    return len(par_stack) == 0


result = paran_balanced(")")
print("Testfall pass: ", result == True)


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
