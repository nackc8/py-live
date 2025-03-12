#!/usr/bin/env python3
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="Lion",
    description="Like Cat, but slower and with more functionality",
    epilog="End of description",
)

parser.add_argument("filename")
values = parser.parse_args(sys.argv[1:])

print("filename:", values.filename)
