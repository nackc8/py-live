import sys

# Vi läser in en fil med en rad som är bredare än 100
myfile = open(
    "/shared/kent/Documents/nackademin/python/py-live/ITINF24/lektion10/langfil.txt"
)

rader = myfile.readline(101)


input("Press enter...")
