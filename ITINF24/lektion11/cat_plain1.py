#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Fel antal arg!", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as fp:
    content = fp.readlines()

print("filnamn", filename)
