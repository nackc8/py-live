def paran_match(txt):
    par_stack = []
    for bokstav in txt:
        if bokstav == "(":
            par_stack.append("(")
        print(bokstav)
    return False


print(paran_match("(hejsan)") == True)
# print(paran_match("(") == False)


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
