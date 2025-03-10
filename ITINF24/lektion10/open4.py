# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("produkter.txt")


finfil = open(file_path)

hela_filen_i_en_var = finfil.read()

print(hela_filen_i_en_var)
