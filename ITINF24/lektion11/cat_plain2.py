#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Får inte vara tomt!", file=sys.stderr)
    sys.exit(1)

# for arg in sys.argv[1:]:
#     print("arg", arg)

show_filename = False
if sys.argv[1] == "-f" or sys.argv[1] == "--show-filename":
    filename = sys.argv[2]
    show_filename = True
else:
    filename = sys.argv[1]


with open(filename) as fp:
    content = fp.readlines()

# 
if show_filename:
    print()

for line in content:
    print(line, end="")
