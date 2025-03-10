from pathlib import Path

p = print

# / skapar en ny Path med det till höger om / tillagt
file_path = Path.cwd() / "file_from_pathlib.txt"

file_path.touch()

input("Tryck enter för att ta bort filen igen")

# Ger FileNotFoundError om filen inte finns
file_path.unlink()
