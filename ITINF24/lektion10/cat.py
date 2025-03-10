import sys
import os

if len(sys.argv) != 2:
    print("Ange en fil som argument!", file=sys.stderr)
    sys.exit(1)

file = sys.argv[1]

os.path.exists(file)

print(sys.argv)
