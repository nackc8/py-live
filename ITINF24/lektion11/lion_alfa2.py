#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

import lionlogic_alfa2 as logic

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower and with more functionality",
    epilog="End of description",
)

parser.add_argument("filename", help="The filename to show")
values = parser.parse_args(sys.argv[1:])

filepath = Path(values.filename)

if not filepath.exists():
    print("Error: File does not exist: ")

output_list = logic.process(filepath)

for line in output_list:
    print(line)
