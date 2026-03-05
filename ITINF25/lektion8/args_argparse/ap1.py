import argparse
import sys
from pathlib import Path

# Se am1.py för vad vi översätter till argparse

parser = argparse.ArgumentParser(
    description="What the program does",
    epilog="Text at the bottom of help",
)

#        -c, -C, --complement
#               use the complement of ARRAY1
#        -d, --delete
#               delete characters in ARRAY1, do not translate


parser.add_argument(
    "-c",
    "-C",
    "--complement",
    action="store_true",
    help="use the complement of STRING1",
)

parser.add_argument(
    "-d",
    "--delete",
    action="store_true",
    help="delete characters in STRING1, do not translate",
)


parser.add_argument("filename", metavar="FILENAME", help="the file to process")
parser.add_argument("string1", metavar="STRING1")
parser.add_argument("string2", metavar="STRING2", nargs="?")

parsed_args = parser.parse_args(sys.argv[1:])

if parsed_args.delete and parsed_args.string2:
    parser.error("argument --delete: expected one string")
elif not parsed_args.delete and not parsed_args.string2:
    parser.error("expected 2 arguments")

filename = Path(parsed_args.filename)

if not filename.exists():
    parser.error(f"missing file {filename}")

# Allt är bra! Dags att jobba!

twrap = open(filename, "r")

rad1 = twrap.readline()
rad2 = twrap.readline()
rad3 = twrap.readline()
print(f"""
  rad1: '{rad1}'
  rad2: '{rad2}'
  rad3: '{rad3}'
""")
