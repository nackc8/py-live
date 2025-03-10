# Bara för att hitta filen i samma katalog som vår källkod, vi
# tittar på detta senare..
from pathlib import Path

file_path = Path(__file__).with_name("produkter.txt")

finfil = open(file_path)

finfil_rader = finfil.readlines()

# Ta bort radmatningen sist med .strip()
sista_ordet = finfil_rader[-1].strip()


# Vad är bäst?
print(f"Jag gillar {sista_ordet}!")
print("Jag gillar " + sista_ordet + "!")
