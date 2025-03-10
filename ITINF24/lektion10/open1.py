import sys

# Vi läser in en fil.
myfile = open(
    "/shared/kent/Documents/nackademin/python/py-live/ITINF24/lektion10/produkter.txt"
)

# Läs fyra första tecknen
fyra_forsta = myfile.read(4)

rader = myfile.readline()


input("Press enter...")
