#!/usr/bin/env python3
import os
import sys

# För att köra i Linux/MacOS
# 1. Shebang!
# 2. 

def get_filename():
    if len(sys.argv) != 2:
        print("Ange en fil som argument!", file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]

    if not os.path.exists(file):
        print("Ange en existerande fil!", file=sys.stderr)
        sys.exit(2)

    return file


# Vårt program fixar inte situationerna nedan:
#
# ITINF24/lektion10
# $ cat --myskofil.txt
# cat: unrecognized option '--myskofil.txt'
# Try 'cat --help' for more information.
# ITINF24/lektion10
# $ cat -- --myskofil.txt
# Mysko innehåll!
# ITINF24/lektion10


def cat(filename):
    with open(filename, "r") as fp:
        content = fp.read()

    print(content)


file = get_filename()
cat(file)
