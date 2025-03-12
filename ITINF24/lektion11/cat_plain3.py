#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Får inte vara tomt!", file=sys.stderr)
    sys.exit(1)

show_filename = False

for arg in sys.argv[1:]:
    if arg == '-f' or arg == '--show-filename':
        show_filename = True
    print("arg", arg)


with open(filename) as fp:
    content = fp.readlines()

# lite nytt: är samma som att skriva
# if show_filename == True
if show_filename:
    print(filename, ":", sep="", end="\n\n")

for line in content:
    print(line, end="")
