standard_input = "gUL"  # för "kattens" skull

col = input("Skriv din favoritfärg: ")

col = col.capitalize()  # "normalisera" texten i variabeln

is_ugly = col == "Gul"

if is_ugly:
    print("gult är fult!")
else:
    print(col, "är en bra färg!")
