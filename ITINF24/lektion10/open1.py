import sys

# Vi läser in en fil.
myfile = open(
    "/shared/kent/Documents/nackademin/python/py-live/ITINF24/lektion10/produkter.txt"
)

# Läs fyra första tecknen
fyra_forsta = myfile.read(4)

# n, eftersom det var allt som var kvar på raden efter bana
rader = myfile.readline(100)


input("Press enter...")
