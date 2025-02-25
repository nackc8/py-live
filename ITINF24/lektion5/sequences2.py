djur = "bisonoxe"

tecken = 1
for bokstav in djur:
    if tecken > 3:
        print(bokstav.upper(), end="")
    else:
        print(bokstav, end="")

    tecken += 1
print()


# https://docs.python.org/3.11/library/stdtypes.html#sequence-types-list-tuple-range
# relevant:
#   x in s
if "BIS" in djur:
    print("BIS-djur!")
