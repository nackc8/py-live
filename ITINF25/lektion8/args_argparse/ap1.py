import argparse
import sys

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
parser.add_argument("--foo", nargs="2")

parsed_args = parser.parse_args(sys.argv[1:])

if parsed_args.delete and parsed_args.string2:
    parser.error("argument --delete: expected one string")
elif not parsed_args.delete and not parsed_args.string2:
    pass
#    parser.error("argument expected one string")

print(parsed_args)

print("complement is: ", parsed_args.complement)

print("Program end")
