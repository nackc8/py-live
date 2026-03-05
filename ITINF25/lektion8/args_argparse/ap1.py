import argparse
import sys

# Se am1.py för vad vi översätter till argparse

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)

#        -c, -C, --complement
#               use the complement of ARRAY1
#        -d, --delete
#               delete characters in ARRAY1, do not translate


parser.add_argument("-c", "-C", "--complement", action="store_true")

parser.add_argument("filename")
parser.add_argument("string1")
parser.add_argument("string2")

parsed_args = parser.parse_args(sys.argv[1:])

print(parsed_args)

print("complement is: ", parsed_args.complement)

print("Program end")
