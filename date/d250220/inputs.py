standard_input = "gUL"  # för "kattens" skull

col = input("Skriv din favoritfärg: ")

col = col.capitalize()

is_ugly = col == "gul"

if is_ugly:
    print("gult är fult!")
else:
    print(col, "är en bra färg!")
