# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("produkter.txt")

# Vi läser in en fil med en rad som är bredare än 100
myfile = open(file_path)

# endast de 100 första tecknen
rad1 = myfile.readline(100)

# läser vidare på samma rad tills radslut
rad2 = myfile.readline(100)

# nu läser den rad 2
rad3 = myfile.readline(100)


input("Press enter...")
