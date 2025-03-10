# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("nummer.txt")

# Vi ska skriva.
myfile = open(file_path, mode="w")

for tal in range(0,10):
    myfile.w


input("Press enter...")
