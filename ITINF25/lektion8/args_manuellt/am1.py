import sys

if len(sys.argv) != 3:
    print(
        "Please add exactly three arguments to the script",
        # Utmatning till stderr
        file=sys.stderr,
        # Mata ut det direkt
        flush=True,
    )
    sys.exit(1)

print("arg 0: " + sys.argv[0])
print("arg 1: " + sys.argv[1])
print("arg 2: " + sys.argv[2])
