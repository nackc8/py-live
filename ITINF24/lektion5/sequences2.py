djur = "bisonoxe"

tecken = 1
for bokstav in djur:
    if tecken > 3:
        print(bokstav.upper(), end="")
    else:
        print(bokstav, end="")

    tecken += 1
