#!/usr/bin/env python3
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower and with more functionality",
    epilog="End of description",
    add_help=True,
)

parser.parse_args(sys.argv[1:])


# for filename in filenames:
#     with open(filename) as fp:
#         contentlines = fp.readlines()

#     if show_filename:
#         print(filename, ":", sep="", end="\n\n")

#     for lineno_line_tuple in enumerate(contentlines, 1):
#         lineno = lineno_line_tuple[0]
#         line = lineno_line_tuple[1]
#         if show_linenumbers:
#             print(lineno, line, end="")
#         else:
#             print(line, end="")
