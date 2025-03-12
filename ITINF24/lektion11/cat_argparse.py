#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower but with more functionality",
    epilog="End of description",
)


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
