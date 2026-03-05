import argparse
import sys

# Se am1.py för vad vi översätter till argparse

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)

parser.parse_args(sys.argv[1:])

print("Program end")
