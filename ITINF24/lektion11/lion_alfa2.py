#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

import lionlogic_alfa2 as logic

# Fake för test
sys.argv = ["./lion_alfa2.py", "frukt.txt"]

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower and with more functionality",
    epilog="End of description",
)

parser.add_argument("filename", help="The filename to show")
parser.add_argument(
    "-f",
    "--show-filename",
    action="store_true",
    help="Prints the filename before its contents.",
)
parser.add_argument(
    "-n",
    "--number",
    action="store_true",
    help="Add a line number to the beginning of each line.",
)

values = parser.parse_args(sys.argv[1:])

filepath = Path(values.filename)

if not filepath.exists():
    print(f"error: File does not exist: {filepath}", file=sys.stderr)
    sys.exit(1)

output_list = logic.process([filepath], values.sh)

for line in output_list:
    print(line)
