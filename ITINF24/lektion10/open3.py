import sys

finfil = open(
    "/shared/kent/Documents/nackademin/python/py-live/ITINF24/lektion10/produkter.txt"
)

finfil_rader = finfil.readlines()

# Ta bort radmatningen sist med .strip()
# sista_ordet = finfil_rader[-1].strip()

sista_ordet = finfil_rader[-1]

print(f"Jag gillar " + sista_ordet + "!")
