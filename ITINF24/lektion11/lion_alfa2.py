#!/usr/bin/env python3
import argparse
import sys

import lionlogic_alfa2 as logic

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower and with more functionality",
    epilog="End of description",
)

parser.add_argument("filename", help="The filename to show")
values = parser.parse_args(sys.argv[1:])

output_list = logic.process(values.filename)

for line in output_list:
    print(line)
