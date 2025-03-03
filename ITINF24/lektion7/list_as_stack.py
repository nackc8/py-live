def paran_match(s):
    return False


print(paran_match("(hejsan)") == True)
print(paran_match("(") == False)


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
