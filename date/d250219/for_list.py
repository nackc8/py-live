rng = range(10, 20000000000000000000000000000000)  # funkar eftersom ett tal i taget ges
lst = list(rng)  # funkar inte, då list(..) vill ha alla sifforna i rangen på en gång

for count in lst:
    print(count)

print("slut")
