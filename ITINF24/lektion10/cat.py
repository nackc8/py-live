import sys

if len(sys.argv) != 2:
    print("Ange en fil som argument!", file=sys.stderr)
    sys.exit(1)



print(sys.argv)
