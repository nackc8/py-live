# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("nummer.txt")

# Vi använder with för att automatiskt stänga filen

with open(file_path, mode="w") as myfile:
    for _ in range(100):
        myfile.write("More! ")

input("Hello")
