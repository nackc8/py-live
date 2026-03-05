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


parser.add_argument("-c", "-C", "--complement")

parsed_args = parser.parse_args(sys.argv[1:])

print(parsed_args)

print("Program end")
