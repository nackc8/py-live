#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Får inte vara tomt!", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

for arg in sys.argv:
    print("arg", arg)

with open(filename) as fp:
    content = fp.readlines()

for line in content:
    print(line, end="")
