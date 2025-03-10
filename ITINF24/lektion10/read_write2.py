# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("nummer.txt")

# Vi ska skriva.
myfile = open(file_path, mode="w")

for _ in range(100):
    myfile.write("More! ")



input("Hello")
