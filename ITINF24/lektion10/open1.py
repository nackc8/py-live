# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("produkter.txt")

# Vi läser in en fil.
myfile = open(file_path)

# Läs fyra första tecknen
fyra_forsta = myfile.read(4)

# n, eftersom det var allt som var kvar på raden efter bana
# max 100 påverkar inte eftersom vår fil inte har så långa rader
rader = myfile.readline(100)


input("Press enter...")
