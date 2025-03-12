#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Får inte vara tomt!", file=sys.stderr)
    sys.exit(1)

show_filename = False
show_linenumbers = False

# -n, --number

args = sys.argv[1:]
used_args_count = 0
for arg in args:
    if arg == "-f" or arg == "--show-filename":
        show_filename = True
        used_args_count += 1
    elif arg == "-n" or arg == "--number":
        show_linenumbers = True
        used_args_count += 1
    # -- separerar flaggor från filnamn
    elif arg == "--":
        used_args_count += 1
        break
    else:
        break

# Ta bort flaggorna från loopen ovan, och behåll endast filnamnen.
filenames = args[used_args_count:]

if len(filenames) == 0:
    print("Hörru! Ange minst ett filnamn", file=sys.stderr)
    sys.exit(1)

for filename in filenames:
    with open(filename) as fp:
        contentlines = fp.readlines()

    # lite nytt: är samma som att skriva
    # if show_filename == True
    if show_filename:
        print(filename, ":", sep="", end="\n\n")

    # alt sätt: (med unboxing av tupeln)
    # for lineno, line in enumerate(contentlines, 1):

    for lineno_line_tuple in enumerate(contentlines, 1):
        lineno = lineno_line_tuple[0]
        line = lineno_line_tuple[1]
        if show_linenumbers:
            print(lineno, line, end="")
        else:
            print(line, end="")
