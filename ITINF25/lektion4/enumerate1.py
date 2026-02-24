# enumerate(sek) skapar en tupel för
# varje element i sek. Kan användas för
# index eller radnummer mm.

#
# lst = ["aa", "bb", "cc", "dd"]

# Sätt list() runt den för att se alla element
# res = list(enumerate(lst))

# res2 = enumerate(lst)

# for x in res2:
#     print(x)
#     print(x[1])

kodsnutt = """for x in *.txt; do
    rm \"$x\"
done
"""

kodrad = kodsnutt.splitlines()

# for radnr_rad in enumerate(kodrad, 1):
#     print(radnr_rad[0], ": ", radnr_rad[1], sep="")

# Exakt samma, med unpacking

for radnr, rad in enumerate(kodrad, 1):
    print(radnr, ": ", rad, sep="")
