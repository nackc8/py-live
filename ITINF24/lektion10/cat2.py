import os
import sys


def get_filename():
    if len(sys.argv) != 2:
        print("Ange en fil som argument!", file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]

    if not os.path.exists(file):
        print("Ange en existerande fil!", file=sys.stderr)
        sys.exit(2)

    return file


file = get_filename()

with open(file, "r") as fp:
    content = fp.read()

print(content)
