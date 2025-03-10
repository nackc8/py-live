# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("nummer.txt")

# Vi använder with för att automatiskt stänga filen

with open(file_path, mode="w") as myfile:
    # Använd gärna en conditional breakpoint: i == 97
    # för att slippa klicka step over manuellt 97 gånger,
    # om vi är ute efter att se de sista snurren i loopen.
    for i in range(100):
        myfile.write("More! ")

input("Hello")
