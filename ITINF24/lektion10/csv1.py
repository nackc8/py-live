import csv
from pathlib import Path

file_path = Path(__file__).with_name("inlamningsuppgifter.csv")

p = print

# Testa att den finns
# p("Finns? ", file_path.exists())

with open(file_path) as minfil:
    content = minfil.read()

parsed = csv.
