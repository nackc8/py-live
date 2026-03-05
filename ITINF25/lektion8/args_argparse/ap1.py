import argparse
import sys

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)

parser.parse_args(sys.argv)

print("Program end")
