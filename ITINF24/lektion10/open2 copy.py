import sys

# Vi läser in en fil med en rad som är bredare än 100
myfile = open(
    "/shared/kent/Documents/nackademin/python/py-live/ITINF24/lektion10/langfil.txt"
)

# endast de 100 första tecknen
rad1 = myfile.readline(100)

# läser vidare på samma rad tills radslut
rad2 = myfile.readline(100)

# nu läser den rad 2
rad3 = myfile.readline(100)


input("Press enter...")
