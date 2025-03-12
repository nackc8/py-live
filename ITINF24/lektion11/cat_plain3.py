#!/usr/bin/env python3
import sys

sys.argv = ["skriptsokvag/skriptnamn", "-f", "frukt.txt"]

if len(sys.argv) < 2:
    print("Får inte vara tomt!", file=sys.stderr)
    sys.exit(1)

show_filename = False

args = sys.argv[1:]
used_args_count = 0
for arg in args:
    if arg == "-f" or arg == "--show-filename":
        show_filename = True
        used_args_count += 1
    elif arg == "--":
        used_args_count += 1
        break
    else:
        break

# Ta bort flaggorna från loopen ovan, och behåll endast
# filnamnen.
filenames = args[used_args_count:]

with open(filename) as fp:
    content = fp.readlines()

# lite nytt: är samma som att skriva
# if show_filename == True
if show_filename:
    print(filename, ":", sep="", end="\n\n")

for line in content:
    print(line, end="")
