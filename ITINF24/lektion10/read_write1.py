# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("nummer.txt")

# Vi ska skriva.
myfile = open(file_path, mode="w")

for _ in range(1000):
    myfile.write("More! ")

# Skriver inte till disk av ovanstående,
# det måste vara mer utmatning för det.
# Cache i minnet är snabbt.
input("Hello")
